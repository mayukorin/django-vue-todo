<template>
  <v-form ref="form" v-model="valid">
        <v-text-field
            v-model="form.email"
            :counter="70"
            label="メールアドレス"
            :rules="rules.email"
            maxlength="70"
            prepend-icon="mdi-email"
        />
        <v-text-field
            v-model="form.username"
            :counter="70"
            label="ユーザ名"
            :rules="rules.username"
            maxlength="70"
            prepend-icon="mdi-account"
        />
        <v-text-field
            type="password"
            v-model="form.password"
            :counter="20"
            label="パスワード"
            :rules="rules.password"
            maxlength="20"
            prepend-icon="mdi-lock"
        />
    <Button @click="handleClick">登録</Button>
</v-form>
</template>
<script>
import Button from '@/components/atoms/Button';
// メールアドレスのフォーマット
const REGEX_EMAIL = /.+@.+/;
export default {
    name: 'UserCreateForm',
    props: {
        onsignin: {
            type: Function,
            required: true
        }
    },
    components: {
        Button
    },
    data: () => ({
        form: {
            email: '',
            username: '',
            password: '',
        },
        components: {
            Button
        },
        valid:true,
        rules: {
            email: [
                v => !!v || 'メールアドレスを入力してください',
                v => REGEX_EMAIL.test(v) || 'メールアドレスの形式が間違っています',
            ],
            username: [
                v => !!v || 'ユーザ名を入力してください',
            ],
            password: [
                v => !!v || 'パスワードを入力してください',
            ]

        }
    }),
    methods: {
        handleClick() {
            if (!this.$refs.form.validate()) { return };
            return this.onsignin({ email: this.form.email, username: this.form.username, password: this.form.password });
        }
    }
};
</script>

