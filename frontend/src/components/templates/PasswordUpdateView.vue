<template>
    <v-container class="my-5">
        <v-row justify="center">
            <v-col cols="12" md="8">
                <PasswordUpdateCard />
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import PasswordUpdateCard from '@/components/organisms/PasswordUpdateCard';
export default {
    name: 'PasswordUpdateView',
    components: {
        PasswordUpdateCard
    },
}
</script>