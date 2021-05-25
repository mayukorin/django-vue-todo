<template>
  <div id="home-view">
    <v-subheader class="grey--text">Tasks</v-subheader>
    <v-container class="my-5">
        <TaskListPanels />
    </v-container>
  </div>
</template>

<script>
import TaskListPanels from '@/components/organisms/TaskListPanels';
export default {
    name: 'HomeView',
    components: {
        TaskListPanels,
    },
};
</script>
