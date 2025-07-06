<template>
  <button @click="handleClick" :class="{ disabled: isDisabled } " :disabled="isDisabled">
      <h1>{{ label }}</h1>
      <h2>{{ price }}</h2>
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
  background-color: rgb(201, 197, 197);
  border: 2px solid rgb(61, 60, 60);
  border-radius: 5px;
  border-width: 2px;
  cursor: pointer;
  text-align: center;
  width: 175px;
  height: 175px;
  margin: 20px;
}

button.disabled {
  background-color: black;
  cursor: not-allowed;
}

h1 {
  font-size: 1.5rem;
  margin: 0;
}
h2 {
  font-size: 1.3rem;
  margin: 0;
}
</style>
