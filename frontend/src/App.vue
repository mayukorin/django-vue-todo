<template>
  <v-app :style="{ background: '#F5F5F5' }">
    <Navbar />
    <v-main class="mx-4 mb-4">
      <!--
      <v-alert type="success" v-show="message.info" v-model="isShow">
        {{ message.info }}
        <v-btn text color="white" @click="isShowFalse">Close</v-btn>
      </v-alert>
      -->
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar'

export default {
  name: 'App',
  components: { Navbar },
  computed: {
    message: function(){
      console.log("ok");
      return this.$store.state.message;
    },
    isShow: function() {
      console.log(this.$store.state.message.is_show);
      return this.$store.state.message.is_show;
    } 
  },
  methods: {
    isShowFalse: function() {
      console.log("okk");
      this.$store.dispatch("message/setIsShowFalse");
    }
  }
}
</script>

