<template>
  <v-card class="login-card px-3">
    <v-card-title>
      <span class="headline">todo-app</span>
    </v-card-title>
    <v-card-text>
      <LoginForm :onlogin="handleLogin" />
    </v-card-text>
  </v-card>
</template>

<script>
import LoginForm from "@/components/molecules/LoginForm";
export default {
  name: "LoginCard",
  components: {
    LoginForm,
  },
  methods: {
    handleLogin(authInfo) {
      return this.$store.dispatch('auth/login', authInfo)
        .then(() => {
          console.log("Login succeeded.");
          this.$store.dispatch("message/setKeepInfoMessage", {
            message: "ログインしました．"
          });
          const next = this.$route.query.next || "/";
          this.$router.replace(next);
        });
    },
  },
};
</script>