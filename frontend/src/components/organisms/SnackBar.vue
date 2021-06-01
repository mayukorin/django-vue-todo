<template>
    <v-snackbar v-model="snac" timeout="4000" top color="success" >
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
            if (this.$store.state.message.info != "") {
                this.openSnackBar();
            }
            return this.$store.state.message;
        }
    }
};
</script>