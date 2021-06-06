<template>
  <div id="home-view">
    <h1 class="subtitle-1 grey--text">Tasks</h1>
    <v-container class="my-5">
        <TaskCreatePopupPlusButton />
        <TaskListPanels />
    </v-container>
  </div>
</template>

<script>
import TaskListPanels from '@/components/organisms/TaskListPanels';
import TaskCreatePopupPlusButton from '@/components/organisms/TaskCreatePopupPlusButton';
export default {
    name: 'HomeView',
    components: {
        TaskListPanels,
        TaskCreatePopupPlusButton
    },
};
</script>
