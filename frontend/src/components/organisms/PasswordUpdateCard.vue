<template>
  <v-card>
    <v-card-title>
      <span class="headline">パスワードの変更</span>
    </v-card-title>
    <v-card-text>
      <PasswordUpdateForm :on-update="handleUpdate" />
      <router-link class="my-3" to="/user-profile"
        >ユーザ情報一覧へ戻る</router-link
      >
    </v-card-text>
  </v-card>
</template>
<script>
import PasswordUpdateForm from "@/components/molecules/PasswordUpdateForm";
export default {
  name: "PasswordUpdateCard",
  components: {
    PasswordUpdateForm,
  },
  methods: {
    handleUpdate(userInfo) {
      return this.$store.dispatch("auth/passwordUpdate", userInfo).then(() => {
        this.$store.dispatch("message/setInfoMessage", {
          message: "パスワードを変更しました．",
        });
        this.$router.replace("/user-profile");
      });
    },
  },
};
</script>
