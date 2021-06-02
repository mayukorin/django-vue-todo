<template>
    <v-app-bar flat app>
        <v-app-bar-nav-icon class="grey--text" @click="handleDrawer"></v-app-bar-nav-icon>
        <v-toolbar-title class="text-uppercase grey--text">
            <span class="font-weight-light">Todo</span>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-menu offset-y>
            <template v-slot:activator="{ on, attrs }">
                <v-btn text v-bind="attrs" v-on="on" color="grey">
                    <v-icon left>mdi-chevron-down</v-icon>
                    <span>Menu</span>
                </v-btn>
            </template>
            <v-list v-if="isLoggedIn">
                <v-list-item router to="/">
                    <v-list-item-content>
                        <v-list-item-title>Task List</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item router to="/user-profile">
                    <v-list-item-content>
                        <v-list-item-title>Account Profile</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
            <v-list v-else>
                <v-list-item router to="/user-create">
                    <v-list-item-content>
                        <v-list-item-title>Account Create</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-menu>
        <v-btn v-if="isLoggedIn" text color="grey" @click="Logout">
            <span>Sign out</span>
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
            this.$store.dispatch('auth/logout');
            this.$store.dispatch('message/setInfoMessage', {
                message: 'ログアウトしました．'
            });
            this.$router.replace('/login');
        },
        Login() {
            this.$router.replace('/login');
        },
        handleDrawer() {
            this.$emit('handleDrawer');
        }
    },
    computed: {
        isLoggedIn() {
            return this.$store.state.auth.isLoggedIn;
        }
    }
};
</script>
