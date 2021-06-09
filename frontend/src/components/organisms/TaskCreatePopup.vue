<template>
    <v-dialog max-width="600px" v-model="dialog">
        <template v-slot:activator="{ on, attrs }">
            <v-btn text v-bind="attrs" v-on="on" class="success">タスク新規作成</v-btn>
        </template>
        <TaskCreateCard @dialogFalse="dialogFalse" />
    </v-dialog>
</template>
<script>
import TaskCreateCard from '@/components/organisms/TaskCreateCard';
export default {
    name: 'TaskCreatePopup',
    components: {
        TaskCreateCard,
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
