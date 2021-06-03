<template>
    <v-expansion-panel class="task caution">
            <v-expansion-panel-header>
                <v-row>
                    <v-col cols="12" md="8">
                        <div class="caption grey--text">Task title</div>
                        <div>{{ task.title }}</div>
                    </v-col>
                    <v-col cols="6" md="2">                  
                        <TaskEditPopup :task="task" />
                    </v-col>
                    <v-col cols="6" md="2"  @click="taskDelete">
                        <div class="caption grey--text">delete</div>
                        <v-icon>mdi-delete</v-icon>
                    </v-col>
                </v-row>
            </v-expansion-panel-header>
            <v-expansion-panel-content class="px-4 grey--text">
                <div v-if="task.deadline" class="foot-weight-bold">do by {{ task.deadline }}</div>
                <div v-else class="foot-weight-bold">no deadline</div>
                <div>{{ task.content }}</div>
        </v-expansion-panel-content>
    </v-expansion-panel>
</template>

<script>
import TaskEditPopup from "@/components/organisms/TaskEditPopup";
export default {
  name: 'TaskPanel',
  components: {
      TaskEditPopup
  },
  props: {
      task: {
          type: Object
      }
  },
  methods: {
      taskDelete: function() {
          console.log(this.task.pk);
          return this.$store.dispatch('task/deleteTask', this.task)
                .then(() => {
                    console.log("Task Delete succeeded.");
                });

      }
  }
};
</script>