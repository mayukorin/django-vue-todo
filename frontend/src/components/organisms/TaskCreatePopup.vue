<template>
    <v-dialog max-width="600px" v-model="dialog">
        <template v-slot:activator="{ on, attrs }">
            <v-btn text v-bind="attrs" v-on="on" class="success">Add new tasks</v-btn>
            <!--<addTaskPopupButton v-bind="attrs" v-on="on" />-->
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
