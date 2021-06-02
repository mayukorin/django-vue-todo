<template>
    <v-snackbar v-model="snac" timeout="4000" top :color="getMessage.color" >
        <SnackBarMessage @close="closeSnackBar()" :message="getMessage"/>
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
        openSnackBar() {
            this.snac = true;
        }
        
    },
    computed: {
        getMessage() {
            if (this.$store.state.message.info != "" || this.$store.state.message.error != "" || this.$store.state.message.warnings.length > 0) {
                this.openSnackBar();
            }
            console.log("ok");
            console.log(this.$store.state.message);
            return this.$store.state.message;
        }
    }
};
</script>