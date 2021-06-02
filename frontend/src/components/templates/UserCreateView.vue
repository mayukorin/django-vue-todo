<template>
  <div id="user-create-view">
    <v-container class="my-5">
      <v-row justify="center">
        <v-col cols="8">
          <UserCreateCard />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import UserCreateCard from "@/components/organisms/UserCreateCard";
export default {
  name: "UserCreateView",
  components: {
    UserCreateCard,
  },
};
</script>