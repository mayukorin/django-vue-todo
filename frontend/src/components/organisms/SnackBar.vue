<template>
    <v-container>
        <v-row class="ma-0">
            <v-col cols="12" md="6">
                <v-snackbar v-model="snac" timeout="4000" top :color="getMessage.color" >
                    <SnackBarMessage @close="closeSnackBar()" :message="getMessage"/>
                </v-snackbar>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import SnackBarMessage from '@/components/molecules/SnackBarMessage';
export default {
    name: 'SnackBar',
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
            if (this.$store.state.message.info != '' || this.$store.state.message.error != '' || this.$store.state.message.warnings.length > 0) {
                this.openSnackBar();
            }
            return this.$store.state.message;
        }
    }
};
</script>