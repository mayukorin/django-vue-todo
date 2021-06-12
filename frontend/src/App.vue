<template>
  <v-app :style="{ background: '#F5F5F5' }">
    <Navbar />
    <v-main class="mx-4 mb-4">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import Navbar from "@/components/organisms/Navbar";

export default {
  name: "App",
  components: { Navbar },
};
</script>
