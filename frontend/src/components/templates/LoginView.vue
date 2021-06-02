<template>
  <div id="login-view">
    <v-container class="my-5">
      <v-row justify="center">
        <v-col cols="8">
          <LoginCard />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import LoginCard from "@/components/organisms/LoginCard";
export default {
  name: "LoginView",
  components: {
    LoginCard,
  },
};
</script>
