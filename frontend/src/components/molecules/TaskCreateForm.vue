<template>
  <v-form class="px-3" ref="form">
    <v-text-field
      v-model="form.title"
      :counter="255"
      :rules="rules.title"
      label="タスク名"
      maxlength="255"
      prepend-icon="mdi-folder"
    />
    <v-textarea
      v-model="form.content"
      label="詳細"
      prepend-icon="mdi-pencil"
    ></v-textarea>
    <v-menu ref="menu" offset-y min-width="auto" transition="scale-transition">
      <template v-slot:activator="{ on, attrs }">
        <v-text-field
          :value="formattedDate"
          v-bind="attrs"
          v-on="on"
          label="締め切り"
          prepend-icon="mdi-calendar"
          readonly
        >
        </v-text-field>
      </template>
      <v-date-picker
        v-model="form.deadline"
        scrollable
        locale="jp-ja"
        :day-format="(date) => new Date(date).getDate()"
      >
      </v-date-picker>
    </v-menu>
    <Button @click="handleClick">作成</Button>
  </v-form>
</template>
<script>
import Button from "@/components/atoms/Button";
import "vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css";
import { format, parseISO } from "date-fns";

export default {
  name: "TaskCreateForm",
  components: {
    Button,
  },
  props: {
    onCreate: {
      type: Function,
      required: true,
    },
  },
  data() {
    return {
      form: {
        title: "",
        content: "",
        deadline: null,
      },
      valid: true,
      rules: {
        title: [(v) => !!v || "タスク名を入力してください"],
      },
    };
  },
  methods: {
    handleClick() {
      if (!this.$refs.form.validate()) {
        return;
      }
      this.onCreate({
        title: this.form.title,
        content: this.form.content,
        deadline: this.form.deadline,
      });
    },
  },
  computed: {
    formattedDate() {
      return this.form.deadline
        ? format(parseISO(this.form.deadline), "yyyy/MM/dd")
        : "";
    },
  },
};
</script>
