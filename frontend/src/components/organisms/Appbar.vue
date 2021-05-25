<template>
    <v-app-bar flat app>
        <v-app-bar-nav-icon class="grey--text" @click="handleDrawer"></v-app-bar-nav-icon>
        <v-toolbar-title class="text-uppercase grey--text">
            <span class="font-weight-light">Todo</span>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn v-if="true" text color="grey" @click="Logout">
            <span>Sign Out</span>
            <v-icon right>mdi-exit-to-app</v-icon>
        </v-btn>
        <v-btn v-else text color="grey" @click="Login">
            <span>Sign In</span>
            <v-icon right>mdi-exit-to-app</v-icon>
        </v-btn>
    </v-app-bar>
</template>
<script>
export default {
    methods: {
        Logout() {
            console.log("logout");
        },
        Login() {
            console.log("login");
        },
        handleDrawer() {
            this.$emit('handleDrawer');
        }
    },
};
</script>
