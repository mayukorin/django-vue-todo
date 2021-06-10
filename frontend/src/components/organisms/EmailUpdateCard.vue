<template>
  <v-card>
    <v-card-title>
      <span class="headline">メールアドレスの変更</span>
    </v-card-title>
    <v-card-text>
      <EmailUpdateForm :email="getEmailInfo" :onUpdate="handleUpdate" />
      <router-link class="my-3" to="/user-profile"
        >ユーザ情報一覧へ戻る</router-link
      >
    </v-card-text>
  </v-card>
</template>
<script>
import EmailUpdateForm from "@/components/molecules/EmailUpdateForm";
export default {
  name: "EmailUpdateCard",
  components: {
    EmailUpdateForm,
  },
  methods: {
    handleUpdate(userInfo) {
      return this.$store.dispatch("auth/emailUpdate", userInfo).then(() => {
        this.$store.dispatch("message/setInfoMessage", {
          message: "メールアドレスを変更しました．",
        });
        this.$router.replace("/user-profile");
      });
    },
  },
  computed: {
    getEmailInfo() {
      return this.$store.state.auth.email;
    },
  },
};
</script>
