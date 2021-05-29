<template>
    <v-container class="my-5">
        <v-row justify="center">
            <v-col cols="8">
                <UserProfileCard />
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import UserProfileCard from '@/components/organisms/UserProfileCard';
export default {
    components: {
        UserProfileCard
    },
}
</script>