<template>
  <v-card class="login-card px-3">
    <v-card-title>
      <span class="headline">task-update</span>
    </v-card-title>
    <v-card-text>
      <TaskEditForm :onUpdate="handleUpdate" :task="task"/>
    </v-card-text>
  </v-card>
</template>

<script>
import TaskEditForm from "@/components/molecules/TaskEditForm";
export default {
  name: 'TaskEditCard',
  props: {
      task: {
          type: Object,
          required: true
      }
  },
  components: {
    TaskEditForm,
  },
  methods: {
    handleUpdate(taskInfo) {
      return this.$store.dispatch('task/updateTask', taskInfo)
        .then(() => {
          console.log("Task Update succeeded.");
          this.$emit('dialog-false')
          /*
          this.$store.dispatch("message/setKeepInfoMessage", {
            message: "ログインしました．"
          });
          */
        });
    },
  },
};
</script>