<template>
    <div>
        <div v-if="message.info">
            <v-row class="ma-0">
                <v-col cols="8">
                    {{ message.info }}
                </v-col>
                <v-col cols="4">
                    <v-btn text color="white" @click="close">Close</v-btn>
                </v-col>
            </v-row>
        </div>
        <div v-if="message.error">
            <span>{{ message.error }}</span>
            <v-btn text color="white" @click="close">Close</v-btn>
        </div>
        <div v-if="message.warnings.length > 0">
            <span>
                <p v-for="warning in message.warnings" :key="warning">
                    {{ warning }}
                </p>
            </span>
            <v-btn text color="white" @click="close">Close</v-btn>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        message: {
            type:Object
        }
    },
    methods: {
        close() {
            this.$emit('close');
        }
    }
};
</script>
