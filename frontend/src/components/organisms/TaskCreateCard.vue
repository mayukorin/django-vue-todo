<template>
  <v-card class="login-card px-3">
    <v-card-title>
      <span class="headline">タスク新規作成</span>
    </v-card-title>
    <v-card-text>
      <TaskCreateForm :on-create="handleCreate" />
    </v-card-text>
  </v-card>
</template>

<script>
import TaskCreateForm from "@/components/molecules/TaskCreateForm";
export default {
  name: "TaskCreateCard",
  components: {
    TaskCreateForm,
  },
  methods: {
    handleCreate(taskInfo) {
      return this.$store.dispatch("task/addTask", taskInfo).then(() => {
        console.log("Task Create succeeded.");
        this.$emit("dialogFalse");
        this.$store.dispatch("message/setInfoMessage", {
          message: "新しいタスクを登録しました．",
        });
      });
    },
  },
};
</script>
