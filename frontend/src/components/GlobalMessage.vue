<template>
    <div>
        <v-container class="grid-list-md" style="height: 300px;">
            <v-layout row warp align-center justify-center fill-height>
                <v-flex xs12 sm8 lg4 md5>
                    <v-alert type="error" v-show="message.error">
                        {{ message.error }}
                    </v-alert>
                    <v-alert type="warning" v-show="message.warnings.length > 0">
                        <p v-for="warning in message.warnings" :key="warning">
                            {{ warning }}
                        </p>
                    </v-alert>
                    <v-alert type="success" v-show="message.info">
                        {{ message.info }}
                    </v-alert>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>
<script>
export default {
    computed: {
        message: function() {
            return this.$store.state.message;
        }
    }
}
</script>
