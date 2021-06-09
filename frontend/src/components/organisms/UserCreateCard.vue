<template>
  <v-card class="login-card px-3">
    <v-card-title>
      <span class="headline">todo-app</span>
    </v-card-title>
    <v-card-text>
      <UserCreateForm :on-sign-in="handleSignin" />
    </v-card-text>
  </v-card>
</template>

<script>
import UserCreateForm from "@/components/molecules/UserCreateForm";
export default {
  name: 'UserCreateCard',
  components: {
    UserCreateForm
  },
  methods: {
    handleSignin(userInfo) {
      return this.$store.dispatch('auth/signup', userInfo)
        .then(() => {
          console.log("signin and login succeeded.");
          
          this.$store.dispatch('message/setKeepInfoMessage', {
            message: 'ユーザ登録が完了し，ログインしました．'
          });
          const next = this.$route.query.next || '/';
          this.$router.replace(next);
        });
    },
  },
};
</script>