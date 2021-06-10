<template>
  <v-container class="my-5">
    <v-row justify="center">
      <v-col cols="12" md="8">
        <UserNameUpdateCard />
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import UserNameUpdateCard from "@/components/organisms/UserNameUpdateCard";
export default {
  name: "UserNameUpdateView",
  components: {
    UserNameUpdateCard,
  },
};
</script>
