<template> 
  <v-row justify="center">
    <v-btn text class="success mx-0 my-3 button" @click="handleClick">
      <slot />
    </v-btn>
  </v-row>
</template>

<script>
export default {
  name: 'Button',
  methods: {
    handleClick() {
      this.$emit('click');
    },
  },
};
</script>
<style scoped>
  .button {
    text-align: center;
  }
</style>