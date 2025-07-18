<template>
  <button @click="$emit('serve-clicked')" class="receipt-button">
    <span v-if="isServed">Go Back</span>
    <span v-else>Serve Order</span>
  </button>
</template>

<script>
export default {
  name: 'ReceiptButton',
  props: {
    isServed: {
      type: Boolean,
      default: false
    }
  }
};
</script>

<style scoped>
.receipt-button {
  background-color: #4CAF50; /* Green */
  color: white;
  padding: 10px 20px;
  border: 3px solid #4CAF50;
  border-radius: 15px;
  width: 400px;
  height: 200px;
  cursor: pointer;
  font-size: 2.5rem;
  font-weight: bold;
}
</style>