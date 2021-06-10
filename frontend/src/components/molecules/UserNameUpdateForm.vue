<template>
  <v-form class="px-3" ref="form" v-model="valid">
    <v-text-field
      label="ユーザ名"
      v-model="form.username"
      :rules="rules.username"
      :counter="70"
      maxlength="70"
      prepend-icon="mdi-account"
    >
    </v-text-field>
    <v-text-field
      label="パスワード"
      v-model="form.checkPassword"
      :rules="rules.password"
      maxlength="20"
      prepend-icon="mdi-lock"
      type="password"
    >
    </v-text-field>
    <Button @click="handleClick">更新</Button>
  </v-form>
</template>
<script>
import Button from "@/components/atoms/Button";

export default {
  name: "UserNameUpdateForm",
  components: {
    Button,
  },
  props: {
    onUpdate: {
      type: Function,
      required: true,
    },
    username: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      form: {
        username: "",
        checkPassword: "",
      },
      valid: true,
      rules: {
        username: [(v) => !!v || "ユーザ名を入力してください"],
        password: [(v) => !!v || "パスワードを入力してください"],
      },
    };
  },
  methods: {
    handleClick() {
      if (!this.$refs.form.validate()) {
        return;
      }
      this.onUpdate({
        username: this.form.username,
        confirm_password: this.form.checkPassword,
      });
    },
  },
  created() {
    this.form.username = this.username;
  },
};
</script>
