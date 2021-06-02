<template>
    <v-container class="my-5">
        <v-row justify="center">
            <v-col cols="8">
                <PasswordUpdateCard />
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import PasswordUpdateCard from '@/components/organisms/PasswordUpdateCard';
export default {
    components: {
        PasswordUpdateCard
    },
}
</script>