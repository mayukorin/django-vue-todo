<template>
    <v-card>
        <v-card-title>
            <span class="headline">Username Update Page</span>
        </v-card-title>
        <v-card-text>
            <UserNameUpdateForm :username="getUserNameInfo" :onUpdate="handleUpdate" />
        </v-card-text>
    </v-card>
</template>
<script>
import UserNameUpdateForm from "@/components/molecules/UserNameUpdateForm.vue";
export default {
    components: {
        UserNameUpdateForm
    },
    methods: {
        handleUpdate(userInfo) {
            return this.$store.dispatch('auth/userNameUpdate', userInfo)
        }
    },
    computed: {
        getUserNameInfo() {
            console.log(this.$store.state.auth.username);
            return this.$store.state.auth.username
                .then(() => {
                    this.$router.replace("/user-profile");
                })
        }
    }

}
</script>