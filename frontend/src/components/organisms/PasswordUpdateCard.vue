<template>
     <v-card>
        <v-card-title>
            <span class="headline">Password Update Page</span>
        </v-card-title>
        <v-card-text>
            <PasswordUpdateForm :onUpdate="handleUpdate" />
        </v-card-text>
    </v-card>
</template>
<script>
import PasswordUpdateForm from "@/components/molecules/PasswordUpdateForm.vue";
export default {
    components: {
        PasswordUpdateForm
    },
    methods: {
        handleUpdate(userInfo) {
            return this.$store.dispatch('auth/passwordUpdate', userInfo)
                .then(() => {
                    this.$router.replace("/user-profile");
                });
        }
    }
}
</script>