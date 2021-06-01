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
                .then(() => {
                    this.$store.dispatch("message/setInfoMessage", {
                        message: "ユーザ名を変更しました．"
                    });
                    this.$router.replace("/user-profile");
                });
        }
    },
    computed: {
        getUserNameInfo() {
            return this.$store.state.auth.username
        }
    }

}
</script>