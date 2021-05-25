<template>
    <v-expansion-panels accordion>
        <TaskPanel v-for="task in taskList" :key="task.pk" :task="task"/>
    </v-expansion-panels>
</template>
<script>
import TaskPanel from '@/components/organisms/TaskPanel';
export default {
    name: 'TaskListPanel',
    components: {
        TaskPanel
    },
    created: function() {
        this.taskList = this.$store.dispatch('task/fetchList');
    },
    computed: {
        taskList() {
            return this.$store.state.task.tasks;
        }
    }
};
</script>