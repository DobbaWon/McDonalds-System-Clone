<template>
  <div class= "header">
  <h1>Welcome to my McDonalds System Clone</h1>
  </div>

  <div class="button-row">
    <PageButton label="Point Of Sale Pages" to="/POSHome" />
    <PageButton label="Not in use yet"/>
    <PageButton label="Not in use yet"/>
    <PageButton label="Not in use yet"/>    
  </div>

  <div class="button-row">
    <PageButton label="Not in use yet"/>
    <PageButton label="Not in use yet"/>
    <PageButton label="Not in use yet"/>
    <PageButton label="Not in use yet"/>
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
