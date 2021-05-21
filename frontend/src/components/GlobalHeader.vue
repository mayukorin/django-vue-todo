<template>
  <header>
      <v-navigation-drawer app v-model="drawer" temporary>
        <v-list
        nav
        dense
        >
          <v-list-item-group
            v-model="group"
            active-class="deep-purple--text text--accent-4"
          >
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-home</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Home</v-list-item-title>
            </v-list-item>

            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-account</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Account</v-list-item-title>
            </v-list-item>

            <v-list-item v-if="isLoggedIn" @click="clickLogout">
              <v-list-item-icon>
                <v-icon>mdi-logout</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item>

            <v-list-item v-else @click="clickLogin">
              <v-list-item-icon>
                <v-icon>mdi-login</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Login</v-list-item-title>
            </v-list-item>

            <v-list-item v-if="isLoggedIn" @click="clickAddTask">
              <v-list-item-icon>
                <v-icon>mdi-pen-plus</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Add Task</v-list-item-title>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
      <v-app-bar
          color="deep-purple accent-4"
          dense
          dark
          app
      >
        <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>
        <v-toolbar-title>To do</v-toolbar-title>
      </v-app-bar>
  </header>
</template>

<script>
  export default {
    computed: {
      isLoggedIn: function() {
        return this.$store.state.auth.isLoggedIn;
      }
    },
    methods: {
      clickLogout: function() {
        this.$store.dispatch("auth/logout");
        this.$store.dispatch("message/setInfoMessage", {
          message: "ログアウトしました．"
        });
        this.$router.replace("/login");
      },
      clickLogin: function() {
        if (this.$route.path != "/login") {
          this.$router.replace("/login");
        }
      },
      clickAddTask: function() {
        if (this.$route.path != "/task-create") {
          this.$router.replace("/task-create");
        }
      }
    },
    data: () => ({
      drawer: false,
      group: null,
    }),
  }
</script>