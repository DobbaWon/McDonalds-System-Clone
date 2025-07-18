<template>
  <router-link :to="to" class="page-button">
    {{ label }}
  </router-link>
</template>

<script>
export default {
  name: 'PageButton',
  props: {
    label: String,
    to: String
  }
}
</script>

<style scoped>
.page-button {
  display: inline-block;
  padding: 1.5rem 3rem;
  font-size: 2.2rem;
  font-weight: bold;
  background-color: #42b983;
  color: white;
  text-decoration: none;
  border-radius: 12px;
  transition: 0.3s ease;
  width: 25rem;
  text-align: center;
  line-height: 25rem;
  margin-left: 10rem;
  margin-top: 6rem;
}
.page-button:hover {
  background-color: #369f6e;
}
</style>
