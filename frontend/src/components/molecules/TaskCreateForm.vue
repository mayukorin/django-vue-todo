<template>
    <v-form class="px-3" ref="form">
        <v-text-field
            v-model="form.title"
            :counter="255"
            :rules="rules.title"
            label="タスク名"
            maxlength="255"
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
        <Button @click="handleClick">作成</Button>
    </v-form>
</template>
<script>
import Button from '@/components/atoms/Button';
import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css';
import {format, parseISO } from 'date-fns'

export default {
    name: 'TaskCreateForm',
    components: {
        Button
    },
    props: {
        onCreate: {
            type: Function,
            required: true
        }
    },
    data: () => ({
        form: {
            title: '',
            content: '',
            deadline: format(parseISO(new Date().toISOString()), 'yyyy-MM-dd'),
        },
        valid:true,
        rules: {
            title: [
                v => !!v || 'タスク名を入力してください',
            ],
        },
    }),
    methods: {
        handleClick() {
            if (!this.$refs.form.validate()) { return };
            this.onCreate({ title: this.form.title, content: this.form.content, deadline: this.form.deadline})
            /*
                .then(() => {
                    this.form.title = '';
                    this.form.content = '';
                    this.form.deadline = format(parseISO(new Date().toISOString()), 'yyyy-MM-dd');
                })
                */
        }
    },
    computed: {
        formattedDate() {
            return this.form.deadline ? format(parseISO(this.form.deadline), 'yyyy/MM/dd') : ''
        }
    }
};
</script>
