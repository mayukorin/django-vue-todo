<template>
    <v-container class="my-5">
        <v-row justify="center">
            <v-col cols="12" md="8">
                <EmailUpdateCard />
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import EmailUpdateCard from '@/components/organisms/EmailUpdateCard';
export default {
    name: 'EmailUpdateView',
    components: {
        EmailUpdateCard
    },
}
</script>