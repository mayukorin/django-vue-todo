<template>
    <v-dialog max-width="600px" v-model="dialog">
        <template v-slot:activator="{ on, attrs }">
            <v-btn text v-bind="attrs" v-on="on" class="success">Add new tasks</v-btn>
        </template>
        <v-card>
            <v-card-title>
                <h2>Add a new Task</h2>
            </v-card-title>
            <v-card-text>
                <v-form class="px-3" ref="form">
                    
                    <v-text-field
                        v-model="form.title"
                        :counter="255"
                        :rules="rules.title"
                        label="タスク名"
                        maxlength="255"
                        required
                        prepend-icon="mdi-folder"
                    />
                    <v-textarea
                        v-model="form.content"
                        label="詳細"
                        prepend-icon="mdi-pencil"
                    ></v-textarea>
                    <v-menu 
                        ref="menu"
                        offset-y 
                        min-width="auto"
                        transition="scale-transition"
                    >
                        
                        <template v-slot:activator="{ on, attrs }">
                            <v-text-field :value="formattedDate"  v-bind="attrs" v-on="on"  label="Due date" prepend-icon="mdi-calendar" readonly>
                            </v-text-field>
                        </template>
                        <v-date-picker 
                            v-model="form.deadline"
                            scrollable
                        >
                        </v-date-picker>
                    </v-menu>
                    <v-btn class="success"  @click="taskCreate">登録</v-btn>
                </v-form>
            </v-card-text>
        </v-card>
    </v-dialog>
</template>
<script>
import api from "@/services/api";
import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css';
import {format, parseISO } from 'date-fns'

export default {
    name: 'TaskCreate',
    data: () => ({
        form: {
            title: '',
            content: '',
            deadline: format(parseISO(new Date().toISOString()), 'yyyy-MM-dd'),
        },
        valid:true,
        loading:false,
        rules: {
            title: [
                v => !!v || 'タスク名を入力してください',
            ],
        },
        dialog: false,
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
                //this.$store.dispatch("tasks/addTask", response.data);
                //console.log(this.$store.state.tasks.tasks);
                this.$store.dispatch("tasks/setUpdateFlagTrue");//taskを更新するように
                this.$store.dispatch("message/setKeepInfoMessage", {
                    message: "新しいタスクを登録しました．"
                });
                this.dialog = false;
            });
            
        }
    },
    computed: {
        formattedDate() {
            return this.form.deadline ? format(parseISO(this.form.deadline), 'yyyy/MM/dd') : ''
        }
    }
};
</script>
