<template>
  <button :class="{ disabled: isDisabled }" @click="handleClick" :disabled="isDisabled">
    <h1>{{ label }}</h1>
  </button>
</template>
<script>
export default {
  name: 'PopUpButton',
  props: {
    label: {
      type: String,
      required: true
    },
    isDisabled: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    handleClick() {
      if (!this.isDisabled) {
        this.$emit('pop-up-clicked', this.label);
      }
    }
  }
};
</script>

<style scoped>
button {
  background-color: rgb(201, 197, 197);
  border: 2px solid rgb(61, 60, 60);
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
  width: 175px;
  height: 125px;
  margin-left: 20px;
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
