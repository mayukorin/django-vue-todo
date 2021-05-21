<template>
  <v-card min-width="400" class="my-2" @click="taskEdit(task.pk)">
    <v-row align="center">
      <v-col cols="2" xl="1" lg="1" md="1" sm="1" class="text-center pr-0">
        <v-icon x-large>mdi-checkbox-marked-circle-outline</v-icon>
      </v-col>
      <v-col>
        <v-card-title>{{ task.title }}</v-card-title>
        <v-card-subtitle>{{ task.deadline }}</v-card-subtitle>
        <v-card-text>
          <div style="white-space:pre;">{{ task.content }}</div>
        </v-card-text>
      </v-col>
    </v-row>
    </v-card>
</template>
<script>
export default {
    props:["task"],
    methods: {
      taskEdit: function(task_pk) {
        this.$router.push({ name: 'TaskEdit', params: { task_pk: task_pk}});
      }
    }
}
</script>
