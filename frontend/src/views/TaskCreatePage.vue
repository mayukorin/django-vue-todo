<template>
    <div id="task-create-page">
        <!--
        <GlobalHeader/>
        <GlobalMessage/>
        -->
        <v-container class="grid-list-md" style="height: 900px;">
            <v-layout row warp align-center justify-center fill-height>
                <v-flex xs12 sm8 lg4 md5>
                    <v-card class="task-create-card">
                        <v-card-title>
                            <span class="headline">Task Create</span>
                        </v-card-title>

                        <v-spacer/>

                        <v-card-text>
                            <v-layout row fill-height justify-center align-center v-if="loading">
                                <v-progress-circular :size="50" color="primary" indeterminate />
                            </v-layout>

                            <v-form v-else ref="form" v-model="valid" lazy-validation>
                                <v-container>
                                    <v-text-field
                                        v-model="form.title"
                                        :counter="255"
                                        :rules="rules.title"
                                        label="タスク名"
                                        maxlength="255"
                                        required
                                    />
                                    <v-textarea
                                    v-model="form.content"
                                    label="詳細"
                                    ></v-textarea>
                                    <vue-ctk-date-time-picker label="日時を選択" v-model="form.deadline" format="YYYY/MM/DD hh:mm"></vue-ctk-date-time-picker>
                                </v-container>
                                <v-btn class="pink white--text" :disabled="!valid" @click="taskCreate">登録</v-btn>
                            </v-form>

                        </v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>
<script src="https://cdn.jsdelivr.net/npm/vue-ctk-date-time-picker@2.4.0/dist/vue-ctk-date-time-picker.umd.min.js"></script>
<script>
//import GlobalHeader from "@/components/GlobalHeader.vue";
//import GlobalMessage from "@/components/GlobalMessage.vue";
import api from "@/services/api";
import VueCtkDateTimePicker from 'vue-ctk-date-time-picker';
import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css';


export default {
    name: 'TaskCreate',
    components: {
        //GlobalHeader,
        //GlobalMessage,
        'vue-ctk-date-time-picker': VueCtkDateTimePicker,
    },
    data: () => ({
        form: {
            title: '',
            content: '',
            deadline: null,
        },
        valid:true,
        loading:false,
        rules: {
            title: [
                v => !!v || 'タスク名を入力してください',
            ],
        }
    }),
    methods: {
        taskCreate: function() {
            console.log(this.form.deadline);
            api({
                method: "post",
                url: "/task/create/",
                data: {
                    title: this.form.title,
                    content: this.form.content,
                    deadline: this.form.deadline,
                }
            }).then(response => {
                console.log(response.data);
                this.$store.dispatch("message/setInfoMessage", {
                      message: "新しいタスクを登録しました．"
                });
                this.$store.dispatch("message/setIsShowTrue");
            });
        }
    }
};
</script>
