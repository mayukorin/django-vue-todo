<template>
    <nav>
        <v-snackbar v-model="isShow.is_show" timeout="4000" top :color="isShow.color" >
            <div v-show="isShow.info">
                <span>{{ isShow.info }}</span>
                <v-btn text color="white" @click="isShowFalse">Close</v-btn>
            </div>
            <div v-show="isShow.error">
                <span>{{ isShow.error }}</span>
                <v-btn text color="white" @click="isShowFalse">Close</v-btn>
            </div>
            <div v-show="isShow.warnings.length > 0">
                <span>
                    <p v-for="warning in isShow.warnings" :key="warning">
                        {{ warning }}
                    </p>
                </span>
                <v-btn text color="white" @click="isShowFalse">Close</v-btn>
            </div>
        </v-snackbar>
        <v-app-bar flat app>
            <v-app-bar-nav-icon class="grey--text" @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-toolbar-title class="text-uppercase grey--text">
                <span class="font-weight-light">Todo</span>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn v-if="isLoggedIn" text color="grey" @click="Logout">
                <span>Sign Out</span>
                <v-icon right>mdi-exit-to-app</v-icon>
            </v-btn>
            <v-btn v-else text color="grey" @click="Login">
                <span>Sign In</span>
                <v-icon right>mdi-exit-to-app</v-icon>
            </v-btn>
        </v-app-bar>
        <v-navigation-drawer app v-model="drawer" class="primary">
            <v-row v-if="isLoggedIn">
                <v-col class="text-center mt-4 mb-3">
                    <task-create-popup />
                </v-col>
            </v-row>
            <v-list v-if="isLoggedIn">
                <v-list-item router to="/user-edit">
                    <v-list-item-icon>
                        <v-icon class="white--text">mdi-account</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title class="white--text">Account Edit</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
            <v-list v-else>
                <v-list-item router to="/user-create">
                    <v-list-item-icon>
                        <v-icon class="white--text">mdi-account</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title class="white--text">Account Create</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </nav>
</template>
<script>
import TaskCreatePopup from './TaskCreatePopup.vue';
export default {
    components: { TaskCreatePopup },
    data() {
        return {
            snac: true,
            drawer: false,
        }
    },
    methods: {
        Logout: function() {
            this.$store.dispatch("auth/logout");
            this.$store.dispatch("message/setInfoMessage", {
                message: "ログアウトしました．"
            });
            this.$store.dispatch("message/setIsShowTrue");
            this.$router.replace("/login");
        },
        Login: function() {
            this.$router.replace("/login");
        },
        isShowFalse: function() {
            this.$store.dispatch("message/setIsShowFalse");
        }
    },
    computed: {
        isLoggedIn: function() {
            return this.$store.state.auth.isLoggedIn;
        },
        isShow: {
            get() {
                console.log(this.$store.state.message);
                return this.$store.state.message;
            },
            set() {
                return this.$store.dispatch("message/setIsShowFalse");
            }
        },
        /*
        message: function() {
            //this.snackbarr = true;
            if (this.$store.state.message.info) {
                console.log("bbb");
                this.snackbarInfo = true;
            }
            
            return this.$store.state.message;
        },
        snackbarInfo: function() {
            console.log("okk");
            if (this.snack) {
                return this.$store.state.message.info;
            } else {
                return "";
            }
        },
        snackbarr: {
            get: function() {
                return this.snackbarInfo;
            },
            set: function(value) {
                console.log("okkk");
                this.snackbarInfo = value;
            }
        },
        */
    }
};
</script>
