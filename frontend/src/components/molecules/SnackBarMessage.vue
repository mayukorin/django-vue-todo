<template>
    <div>
        <div v-if="message.info">
            <span>{{ message.info }}</span>
            <v-btn text color="white" @click="close">Close</v-btn>
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
