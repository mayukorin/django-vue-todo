<template>
<!--
    <v-dialog max-width="600px" v-model="dialog">
        <template v-slot:activator="{ on, attrs }">
            <div v-bing="attrs" v-on="on">
                <div class="caption grey--text">edit</div>
                <v-icon>mdi-pencil</v-icon>
            </div>
        </template>
-->
    <div>
        <!-- @click.stopにいれればいける -->
        <div @click.stop="taskEdit()">
                <div class="caption grey--text">edit</div>
                <v-icon>mdi-pencil</v-icon>
        </div>
        <v-dialog v-model="dialog" max-width="600px">
            <v-card>
                <v-card-title>
                    <h2>Edit a Task</h2>
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
                        <v-btn class="success"  @click="taskUpdate">更新</v-btn>
                    </v-form>
                </v-card-text>
            </v-card>
        </v-dialog>
    </div>
</template>
<script>
import api from "@/services/api";
import {format, parseISO } from 'date-fns'


export default {
    name: 'TaskEdit',
    props: ['taskPk'],
    data: () => ({
        dialog: false,
        form: {
            title: '',
            content: '',
            deadline: format(parseISO(new Date().toISOString()), 'yyyy-MM-dd'),
            pk: null,
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
        taskUpdate: function() {
            api({
                method: "patch",
                url: "/task/update/" + this.form.pk + "/",
                data: {
                    title: this.form.title,
                    content: this.form.content,
                    deadline: this.form.deadline
                }
            }).then(response => {
                console.log(response.data);
                this.$store.dispatch("tasks/setUpdateFlagTrue");//taskを更新するように
                this.$store.dispatch("message/setKeepInfoMessage", {
                    message: "タスクを更新しました"
                });
                this.dialog = false;
            })
        },
        taskEdit() {
            console.log("ok");
            console.log(this.taskPk);
            api({
                method: "get",
                url: "/task/edit/" + this.taskPk + "/"
            }).then(response => {
                this.form.title = response.data.title;
                this.form.content = response.data.content;
                this.form.deadline = response.data.deadline;
                this.form.pk = response.data.pk;
                this.dialog = true;
            })
        }
    },
    computed: {
        formattedDate() {
            return this.form.deadline ? format(parseISO(this.form.deadline), 'yyyy/MM/dd') : ''
        }
    }
};
</script>
