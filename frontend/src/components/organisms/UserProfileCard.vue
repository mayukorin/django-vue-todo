<template>
    <v-card>
        <UserProfileList :UserInfo="GetUserInfo"/>
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
