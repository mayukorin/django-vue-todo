<template>
    <v-container class="my-5">
        <v-row justify="center">
            <v-col cols="8">
                <EmailUpdateCard />
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import EmailUpdateCard from '@/components/organisms/EmailUpdateCard';
export default {
    components: {
        EmailUpdateCard
    },
}
</script>