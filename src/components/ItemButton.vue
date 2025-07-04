<template>
  <button @click="handleClick" :class="{ disabled: isDisabled } " :disabled="isDisabled">
    <span>{{ label }}</span>
    <span v-if="price !== undefined" class="price">${{ price.toFixed(2) }}</span>
  </button>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      required: true
    },
    price: {
      type: Number,
      required: true,
      default: 0
    },
    isDisabled: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    handleClick() {
      this.$emit('click');
    }
  }
};
</script>

<style scoped>
button {
  background-color: #f0c040;
  border: none;
  border-radius: 5px;
  color: white;
  cursor: pointer;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

button.disabled {
  background-color: black;
  cursor: not-allowed;
}
</style>
