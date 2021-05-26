<template>
  <v-card class="login-card px-3">
    <v-card-title>
      <span class="headline">task-create</span>
    </v-card-title>
    <v-card-text>
      <TaskCreateForm :onCreate="handleCreate" />
    </v-card-text>
  </v-card>
</template>

<script>
import TaskCreateForm from "@/components/molecules/TaskCreateForm";
export default {
  name: 'TaskCreateCard',
  components: {
    TaskCreateForm,
  },
  methods: {
    handleCreate(taskInfo) {
      return this.$store.dispatch('task/addTask', taskInfo)
        .then(() => {
          console.log("Task Create succeeded.");
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