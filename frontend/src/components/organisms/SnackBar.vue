<template>
    <v-snackbar v-model="snac" timeout="4000" top :color="isShow.color" >
        <SnackBarMessage @close="closeSnackBar()" :message="getMessage()"/>
    </v-snackbar>
</template>
<script>
import SnackBarMessage from '@/components/molecules/SnackBarMessage';
export default {
    components: { SnackBarMessage },
    data() {
        return {
            snac: false,
        }
    },
    methods: {
        closeSnackBar() {
            this.snac = false;
        },
        
    },
    computed: {
        getMessage() {
            if (this.$store.state.message.info != "") this.snac = true;
            return this.$store.state.message;
        }
    }
};
</script>