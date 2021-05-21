<template v-cloak>
  <div id="home-page" v-bind:class="updateFlag">
    <v-subheader class="grey--text">Tasks</v-subheader>
    <v-container class="my-5">
        <v-expansion-panels accordion>
            <v-expansion-panel v-for="task in tasks" :key="task.pk" class="task caution">
                <v-expansion-panel-header>
                    <v-row>
                        <v-col cols="12" md="8">
                            <div class="caption grey--text">Task title</div>
                            <div>{{ task.title }}</div>
                        </v-col>
                        <v-col cols="6" md="2">                  
                            <Task-edit-popup v-bind:task-pk="task.pk" />
                        </v-col>
                        <v-col cols="6" md="2">
                            <div class="caption grey--text">delete</div>
                            <v-icon>mdi-delete</v-icon>
                        </v-col>
                    </v-row>
                </v-expansion-panel-header>
                <v-expansion-panel-content class="px-4 grey--text">
                    <div class="foot-weight-bold">do by {{ task.deadline }}</div>
                    <div>{{ task.content }}</div>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-expansion-panels>
    </v-container>
  </div>
</template>
<script>

import api from "@/services/api";
import TaskEditPopup from '@/components/TaskEditPopup.vue';

export default {
    
  components: {
      TaskEditPopup
  },
  data()  {
        return {
            selectedItem: 1,
            tasks: [],
        }
    },
    created() {
        api({
                method: "get",
                url: "/task/list/",
            }).then(response => {
                //this.$store.dispatch("tasks/setTasks", response.data);
                this.tasks = response.data;
                //this.update_flag = this.$store.state.tasks.update_flag;
                if (this.$store.state.message.show_flag) {
                    this.$store.dispatch("message/setIsShowTrue");
                    this.$store.dispatch("message/setShowFlagFalse");
                }
        });
    },
    computed: {
        updateFlag: function() {
            return this.$store.state.tasks.update_flag;
        }
    },
    /*
    mouted() {
        this.$store.watch(
            (state, getters) => getters.update_flag,
            (newValue, oldValue) => {
                console.log(newValue);
                console.log(oldValue);
            }
        )
    },
    */
    watch: {
        updateFlag(newValue, oldValue) {
            console.log(newValue, oldValue);
            if (newValue == true) {
                api({
                        method: "get",
                        url: "/task/list/",
                    }).then(response => {
                        console.log("ok");
                        this.tasks = response.data;
                        this.$store.dispatch("tasks/setUpdateFlagFalse");
                        this.$store.dispatch("message/setIsShowTrue");
                });
            }
        }
    }
    /*
    beforeRouteEnter: function(to, from, next) {
        
        api({
                method: "get",
                url: "/task/list/",
            }).then(response => {
                next(function (vm) {
                    vm.tasks = response.data;
                    console.log(response.data);
                    
                })
        });
        
    },
    */
    
};
</script>
<style>
    .task.caution{
        border-left: 4px solid tomato;
    }
</style>


