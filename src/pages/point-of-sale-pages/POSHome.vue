<template>
  <div class="header">
    <BackButton label="Home" to="/" />

    <div class="header-titles">
      <h1>Point of Sale Home</h1>
      <h2>Select an option below:</h2>
    </div>
  </div>

  <div class="button-row">
    <PageButton label="Default POS" to="/PointOfSale" />
    <PageButton label="Drive Thru Speaker POS" to="/DriveThruSpeakerPOS" />
    <PageButton label="Drive Thru Cashier POS" to="/DriveThruCashierPOS" />
  </div>
</template>


<script>
import BackButton from '../../components/BackButton.vue';
import PageButton from '../../components/PageButton.vue';

export default {
  name: 'POSHome',
  components: {
    BackButton,
    PageButton
  }
};
</script>

<style scoped>
.header-titles {
  display: flex;
  flex-direction: column;
}

</style>