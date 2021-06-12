<template>
  <div>
    <div v-if="message.info">
      <v-row class="ma-2">
        <v-col cols="12" md="9">
          {{ message.info }}
        </v-col>
        <v-col cols="2" md="3">
          <v-btn text color="white" @click="close">Close</v-btn>
        </v-col>
      </v-row>
    </div>
    <div v-if="message.error">
      <v-row class="ma-2">
        <v-col cols="12" md="9">
          {{ message.error }}
        </v-col>
        <v-col cols="2" md="3">
          <v-btn text color="white" @click="close">Close</v-btn>
        </v-col>
      </v-row>
    </div>
    <div v-if="message.warnings.length > 0">
      <v-row class="ma-2">
        <v-col cols="12" md="9">
          <p v-for="warning in message.warnings" :key="warning">
            {{ warning }}
          </p>
        </v-col>
        <v-col cols="2" md="3">
          <v-btn text color="white" @click="close">Close</v-btn>
        </v-col>
      </v-row>
    </div>
  </div>
</template>
<script>
export default {
  name: "SnackBarMessage",
  props: {
    message: {
      type: Object,
    },
  },
  methods: {
    close() {
      this.$emit("close");
    },
  },
};
</script>
