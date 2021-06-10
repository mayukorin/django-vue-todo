<template>
  <v-card>
    <UserProfileList :user-info="getUserInfo" />
  </v-card>
</template>
<script>
import UserProfileList from "@/components/molecules/UserProfileList";
export default {
  name: "UserProfileCard",
  components: {
    UserProfileList,
  },
  methods: {
    goUpdatePage: function (next_url) {
      this.$router.replace(next_url);
    },
  },
  computed: {
    getUserInfo() {
      return this.$store.state.auth;
    },
  },
};
</script>
