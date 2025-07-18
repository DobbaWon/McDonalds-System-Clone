<template>
  <div class= "header">
  <h1>Welcome to my McDonalds System Clone</h1>
  </div>

  <div class="button-row">
    <PageButton label="Point Of Sale Page" to="/PointOfSale" />
    <PageButton label="Kitchen Screen Page" to="/KitchenScreen" />
  </div>
</template>

<script>
import PageButton from '../components/PageButton.vue'

export default {
  name: 'Home',
  components: { PageButton }
}
</script>

<style scoped>
</style>
