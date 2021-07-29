<template>
  <v-card class="login-card px-3">
    <v-card-title>
      <span class="headline">todo-app</span>
    </v-card-title>
    <v-card-text>
      <LoginForm :onlogin="handleLogin" />
      <v-divider class="mb-3"></v-divider>
      アカウントをお持ちではない方は
      <Button @click="goUserCreatePage()">アカウント新規登録</Button>
    </v-card-text>
  </v-card>
</template>

<script>
import Button from "@/components/atoms/Button";
export default {
  name: "LoginCard",
  components: {
    LoginForm,
    Button,
  },
  methods: {
    handleLogin(authInfo) {
      return this.$store.dispatch("auth/login", authInfo).then(() => {
        console.log("Login succeeded.");
        this.$store.dispatch("message/setKeepInfoMessage", {
          message: "サインインしました．",
        });
        const next = this.$route.query.next || "/";
        this.$router.replace(next);
      });
    },
    goUserCreatePage() {
      this.$router.replace("/user-create");
    },
  },
};
</script>
