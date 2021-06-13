<template>
  <v-expansion-panel class="task caution">
    <v-expansion-panel-header>
      <v-row>
        <v-col cols="12" md="7">
          <div class="caption grey--text">タイトル</div>
          <div>{{ task.title }}</div>
        </v-col>
        <v-col cols="6" md="2">
          <TaskEditPopup :task="task" />
        </v-col>
        <v-col cols="6" md="2" @click="taskDelete">
          <div class="caption grey--text">削除</div>
          <v-icon>mdi-delete</v-icon>
        </v-col>
      </v-row>
    </v-expansion-panel-header>
    <v-expansion-panel-content style="display: block" class="px-4 grey--text">
      <div v-if="task.deadline" class="foot-weight-bold">
        {{ formattedDate }} まで
      </div>
      <div v-else class="foot-weight-bold">期限なし</div>
      <div style="white-space: pre-line">
        {{ task.content }}
      </div>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import TaskEditPopup from "@/components/organisms/TaskEditPopup";
import { format, parseISO } from "date-fns";
export default {
  name: "TaskPanel",
  components: {
    TaskEditPopup,
  },
  props: {
    task: {
      type: Object,
    },
  },
  methods: {
    taskDelete: function () {
      return this.$store.dispatch("task/deleteTask", this.task).then(() => {
        console.log("Task Delete succeeded.");
        this.$store.dispatch("message/setInfoMessage", {
          message: "タスクを1件削除しました",
        });
      });
    },
  },
  computed: {
    formattedDate() {
      return this.task.deadline
        ? format(parseISO(this.task.deadline), "yyyy/MM/dd")
        : "";
    },
  },
};
</script>
<style scoped>
.on-hover {
  border: 3px solid;
  border-color: grey;
}
</style>
