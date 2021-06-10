<template>
  <div>
    <v-row class="ma-0 pa-3">
      <v-col cols="12" md="10">
        <div class="caption grey--text">メールアドレス</div>
        <div class="black--text">{{ User.email }}</div>
      </v-col>
      <v-col cols="4" md="2">
        <v-btn
          depressed
          class="success white--text"
          @click="goUpdatePage('/email-update')"
          >編集</v-btn
        >
      </v-col>
    </v-row>
    <v-divider></v-divider>
    <v-row class="ma-0 pa-3">
      <v-col cols="12" md="10">
        <div class="caption grey--text">ユーザ名</div>
        <div class="black--text">{{ User.username }}</div>
      </v-col>
      <v-col cols="4" md="2">
        <v-btn
          depressed
          class="success white--text"
          @click="goUpdatePage('/username-update')"
          >編集</v-btn
        >
      </v-col>
    </v-row>
    <v-divider></v-divider>
    <v-row class="ma-0 pa-3">
      <v-col cols="12" md="10">
        <div class="caption grey--text">パスワード</div>
      </v-col>
      <v-col cols="4" md="2">
        <v-btn
          depressed
          class="success white--text"
          @click="goUpdatePage('/password-update')"
          >編集</v-btn
        >
      </v-col>
    </v-row>
  </div>
</template>
<script>
export default {
  name: "UserProfileList",
  data() {
    return {
      User: {
        email: "",
        username: "",
      },
    };
  },
  props: {
    UserInfo: {
      type: Object,
      required: true,
    },
  },
  created() {
    this.User.email = this.UserInfo.email;
    this.User.username = this.UserInfo.username;
  },
  methods: {
    goUpdatePage: function (next_url) {
      console.log("aaaa");
      this.$router.replace(next_url);
    },
  },
};
</script>
