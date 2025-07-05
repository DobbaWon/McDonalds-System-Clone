<template>
  <BackButton label="Back" to="/POSHome" />
  <POSMenu />
  <POSReceipt />
</template>

<script>
import BackButton from '../../components/BackButton.vue';
import ItemButton from '../../components/ItemButton.vue';
import POSMenu from '../../components/POSMenu.vue';
import POSReceipt from '../../components/POSReceipt.vue';

export default {
  name: 'PointOfSale',
  components: {
    BackButton,
    POSMenu,
    POSReceipt,
    ItemButton
  }
};
</script>

<style scoped>
</style>
