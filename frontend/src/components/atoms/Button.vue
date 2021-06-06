<template> 
  <v-btn text class="success mx-0 mt-3" @click="handleClick">
    <slot />
  </v-btn>
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