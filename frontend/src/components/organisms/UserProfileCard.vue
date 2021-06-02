<template>
    <v-card>
        <v-card-title>
            <span class="headline">User Profile Page</span>
        </v-card-title>
        <v-card-text>
            <UserProfileList :UserInfo="GetUserInfo"/>
        </v-card-text>
    </v-card>
</template>
<script>
import UserProfileList from '@/components/molecules/UserProfileList';
export default {
    components: {
        UserProfileList
    },
    methods: {
        GoUpdatePage: function(next_url) {
            this.$router.replace(next_url);
        }
    },
    computed: {
        GetUserInfo() {
            console.log(this.$store.state.auth);
            return this.$store.state.auth;
        }
    }
}
</script>
