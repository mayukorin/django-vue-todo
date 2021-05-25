<template>
  <v-form  ref="form">
    <v-text-field
      v-model="form.email"
      label="メールアドレス"
      :rules="rules.email"
      prepend-icon="mdi-email"
    />
    <v-spacer></v-spacer>
    <v-text-field
      v-model="form.password"
      label="パスワード"
      :rules="rules.password"
      prepend-icon="mdi-lock"
    />
    <Button @click="handleClick">ログイン</Button>
  </v-form>
</template>

<script>
import Button from '@/components/atoms/Button';
// メールアドレスのフォーマット
const REGEX_EMAIL = /.+@.+/;

export default {
  name: "LoginForm",
  components: {
    Button,
  },
  props: {
    onlogin: {
      type: Function,
      required: true,
    },
  },
  data() {
    return {
        form: {
            email: '',
            password: '',
        },
        rules: {
            email: [
                (v) => !!v || 'メールアドレスを入力してください',
                (v) => REGEX_EMAIL.test(v) || 'メールアドレスの形式が間違っています',
            ],
            password: [
                (v) => !!v || 'パスワードを入力してください'
            ],
        },
    };
  },
  methods: {
    handleClick(ev) {
        console.log(ev);
        if (!this.$refs.form.validate()) return;
        // ok と出力されるはず
        console.log(this.onlogin({ email: this.form.email, password: this.form.password }));
        /*
        this.onlogin({ email: this.form.email, password: this.form.password})
            .catch(err => {
                console.log(err);
            })
            .then(() => {
                console.log('ログイン完了')
            })
        */
    },
  },
};
</script>