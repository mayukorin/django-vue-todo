<template>
    <v-dialog max-width="600px" v-model="dialog">
        <template v-slot:activator="{ on, attrs }">
            <v-btn
                class="ma-2"
                fab
                dark
                text
                color="success"
                v-bind="attrs"
                v-on="on"
            >
                <v-icon dark>
                    mdi-plus
                </v-icon>
            </v-btn>
        </template>
        <TaskCreateCard @dialog-false="dialogFalse" />
    </v-dialog>
</template>
<script>
import TaskCreateCard from '@/components/organisms/TaskCreateCard';
//import addTaskPopupButton from '@/components/atoms/addTaskPopupButton';
export default {
    name: 'TaskCreatePopup',
    components: {
        TaskCreateCard,
        //addTaskPopupButton
    },
    data: () => ({
        dialog: false,
    }),
    methods: {
        dialogFalse() {
            this.dialog = false;
        }
    },
};
</script>