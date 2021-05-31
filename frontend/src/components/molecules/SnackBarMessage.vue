<template>
    <div>
        <span>{{ message.info }}</span>
        <v-btn text color="white" @click="close">Close</v-btn>
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
