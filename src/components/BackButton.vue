<template>
  <router-link :to="to" class="back-button">
    {{ label }}
  </router-link>
</template>

<script>
export default {
  name: 'BackButton',
  props: {
    label: String,
    to: String
  }
}
</script>

<style scoped>
.back-button {
  display: inline-block;
  padding: 1rem 2rem;
  font-size: 1.5rem;
  font-weight: bold;
  background-color: #42b983;
  color: white;
  text-decoration: none;
  border-radius: 8px;
  transition: background-color 0.3s ease;
}
.back-button:hover {
  background-color: #369f6e;
}
</style>