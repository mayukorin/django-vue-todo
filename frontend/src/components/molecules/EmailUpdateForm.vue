<template>
    <v-form class="px-3" ref="form" v-model="valid">
        <v-text-field 
            label="メールアドレス"
            v-model="form.email"
            :rules="rules.email"
            :counter="70"
            maxlength="70"
            prepend-icon="mdi-email"
        >
        </v-text-field>
        <v-text-field 
            label="パスワード"
            v-model="form.checkPassword"
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
// メールアドレスのフォーマット
const REGEX_EMAIL = /.+@.+/;

export default {
    name: 'EmailUpdateForm',
    components: {
        Button
    },
    props: {
        onUpdate: {
            type: Function,
            required: true
        },
        email: {
            type:  String,
            required: true
        }
    },
    data () {
        return {
            form: {
                email: '',
                checkPassword: ''
            },
            valid:true,
            rules: {
                email: [
                    v => !!v || 'メールアドレスを入力してください',
                    (v) => REGEX_EMAIL.test(v) || 'メールアドレスの形式が間違っています',
                ],
                password: [
                    v => !!v || 'パスワードを入力してください'
                ]
            },
        }
    },
    methods: {
        handleClick() {
            if (!this.$refs.form.validate()) { return };
            this.onUpdate({ email: this.form.email, confirm_password: this.form.checkPassword})
        }
    },
    created() {
        this.form.email = this.email;
    }
};
</script>