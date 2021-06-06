<template>
    <v-form class="px-3" ref="form" v-model="valid">
        <v-text-field 
            label="現在のpassword"
            v-model="form.checkPassword"
            :rules="rules.password"
            maxlength="20"
            prepend-icon="mdi-lock"
        >
        </v-text-field>
        <v-text-field 
            label="新しいpassword"
            v-model="form.newPassword"
            :rules="rules.password"
            maxlength="20"
            prepend-icon="mdi-lock"
        >
        </v-text-field>
        <Button @click="handleClick">更新</Button>
    </v-form>
</template>
<script>
import Button from '@/components/atoms/Button';

export default {
    name: 'PasswordUpdateForm',
    components: {
        Button
    },
    props: {
        onUpdate: {
            type: Function,
            required: true
        }
    },
    data () {
        return {
             form: {
                newPassword: '',
                checkPassword: ''

            },
            valid:true,
            rules: {
                password: [
                    v => !!v || 'パスワードを入力してください'
                ]
            },
        }
    },
    methods: {
        handleClick() {
            if (!this.$refs.form.validate()) { return };
            this.onUpdate({ confirm_password: this.form.checkPassword, new_password: this.form.newPassword})
        }
    },
};
</script>