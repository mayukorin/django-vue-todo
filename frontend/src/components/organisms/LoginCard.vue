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
      // this.$store.dispatch('login', authInfo) とか
      console.log(authInfo);
      return "ok";
    },
  },
};
</script>