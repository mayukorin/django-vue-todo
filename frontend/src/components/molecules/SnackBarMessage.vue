<template>
    <div>
        <div v-if="message.info">
            <v-row class="ma-0">
                <v-col cols="12" md="10">
                    {{ message.info }}
                </v-col>
                <v-col cols="2" md="2">
                    <v-btn text color="white" @click="close">Close</v-btn>
                </v-col>
            </v-row>
        </div>
        <div v-if="message.error">
            <v-row class="ma-0">
                <v-col cols="12" md="10">
                    {{ message.error }}
                </v-col>
                <v-col cols="2" md="2">
                    <v-btn text color="white" @click="close">Close</v-btn>
                </v-col>
            </v-row>
        </div>
        <div v-if="message.warnings.length > 0">
            <v-row class="ma-0">
                <v-col cols="12" md="10">
                    <p v-for="warning in message.warnings" :key="warning">
                        {{ warning }}
                    </p>
                </v-col>
                <v-col cols="2" md="2">
                    <v-btn text color="white" @click="close">Close</v-btn>
                </v-col>
            </v-row>
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
