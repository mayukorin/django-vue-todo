<template>
    <v-list>
        <v-list-item>
            <v-list-item-content>
                <v-list-item-subtitle>email</v-list-item-subtitle>
                <v-list-item-title>{{ User.email }}</v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
                <v-btn depressed class="success white--text" @click="GoUpdatePage('/email-update')">編集</v-btn>
            </v-list-item-action>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item>
            <v-list-item-content>
                <v-list-item-subtitle>username</v-list-item-subtitle>
                <v-list-item-title>{{ User.username }}</v-list-item-title>
            </v-list-item-content>
            <v-list-item-action>
                <v-btn depressed class="success white--text" @click="GoUpdatePage('/username-update')">編集</v-btn>
            </v-list-item-action>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item>
            <v-list-item-content>
                <v-list-item-subtitle>password</v-list-item-subtitle>
            </v-list-item-content>
            <v-list-item-action>
                <v-btn depressed class="success white--text" @click="GoUpdatePage('/password-update')">編集</v-btn>
            </v-list-item-action>
        </v-list-item>
    </v-list>
</template>
<script>

export default {
    data() {
        return {
            User: {
                email: '',
                username: ''
            }
        }
    },
    props: {
        UserInfo: {
            type: Object,
            required: true
        }
    },
    created() {
        this.User.email = this.UserInfo.email;
        this.User.username = this.UserInfo.username;
    },
    methods: {
        GoUpdatePage: function(next_url) {
            this.$router.replace(next_url);
        }
    }
}
</script>