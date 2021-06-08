<template>
    <div id="profile">
        <h1 class="subtitle-1 grey--text">Profile</h1>
        <v-container class="my-5">
            <UserProfileCard />
        </v-container>
    </div>
</template>
<script>
import UserProfileCard from '@/components/organisms/UserProfileCard';
export default {
    name: 'UserProfileView',
    components: {
        UserProfileCard
    },
}
</script>