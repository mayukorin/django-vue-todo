<template>
  <v-card class="login-card px-3">
    <v-card-title>
      <span class="headline">タスク編集</span>
    </v-card-title>
    <v-card-text>
      <TaskEditForm :on-update="handleUpdate" :task="task" />
    </v-card-text>
  </v-card>
</template>

<script>
import TaskEditForm from "@/components/molecules/TaskEditForm";
export default {
  name: "TaskEditCard",
  props: {
    task: {
      type: Object,
      required: true,
    },
  },
  components: {
    TaskEditForm,
  },
  methods: {
    handleUpdate(taskInfo) {
      return this.$store.dispatch("task/updateTask", taskInfo).then(() => {
        console.log("Task Update succeeded.");
        this.$emit("dialogFalse");
        this.$store.dispatch("message/setInfoMessage", {
          message: "タスクを編集しました．",
        });
      });
    },
  },
};
</script>
