<template>
  <v-navigation-drawer app v-model="drawer" class="primary">
    <v-row v-if="isLoggedIn">
      <v-col class="text-center mt-4 mb-3">
        <TaskCreatePopup />
      </v-col>
    </v-row>
    <v-list v-if="isLoggedIn">
      <v-list-item router to="/">
        <v-list-item-icon>
          <v-icon class="white--text">mdi-clipboard-list</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title class="white--text">タスク一覧</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item router to="/user-profile">
        <v-list-item-icon>
          <v-icon class="white--text">mdi-account</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title class="white--text"
            >ユーザ情報一覧</v-list-item-title
          >
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <v-list v-else>
      <v-list-item router to="/user-create">
        <v-list-item-icon>
          <v-icon class="white--text">mdi-account</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title class="white--text"
            >アカウント新規登録</v-list-item-title
          >
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>
<script>
import TaskCreatePopup from "@/components/organisms/TaskCreatePopup";

export default {
  name: "Drawer",
  components: {
    TaskCreatePopup,
  },
  props: {
    drawerNotification: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      drawer: false,
    };
  },
  computed: {
    isLoggedIn() {
      return this.$store.state.auth.isLoggedIn;
    },
  },
  watch: {
    drawerNotification() {
      this.drawer = !this.drawer;
    },
  },
};
</script>
