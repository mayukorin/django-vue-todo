<template>
    <v-container class="my-5">
        <v-row justify="center">
            <v-col cols="8">
                <UserNameUpdateCard />
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import UserNameUpdateCard from '@/components/organisms/UserNameUpdateCard';
export default {
    components: {
        UserNameUpdateCard
    },
}
</script>