<template>
  <div class="header">
    <h1>Point of Sale</h1>
  </div>
  <BackButton label="Back" to="/POSHome" />

  <div class="point-of-sale">
    <POSMenu @item-selected="addItemToOrder" />
    <POSReceipt @serve-clicked="handleServeClicked" :order="order" v-if="isReceiptVisible" />
    <POSOrder @serve-clicked="handleServeClicked" :order="order" v-if="!isReceiptVisible" />
  </div>
</template>


<script>
import BackButton from '../components/BackButton.vue';
import ItemButton from '../components/ItemButton.vue';
import POSMenu from '../components/POSMenu.vue';
import POSReceipt from '../components/POSReceipt.vue';
import POSOrder from '../components/POSOrder.vue';

export default {
  name: 'PointOfSale',
  components: {
    BackButton,
    POSMenu,
    POSReceipt,
    ItemButton,
    POSOrder
  },
  data() {
    return {
      order: [],
      isReceiptVisible: false
    };
  },
  methods: {
  addItemToOrder(item) {
    this.order.push(item);
  },
  handleServeClicked() {
    this.isReceiptVisible = !this.isReceiptVisible;
  }
}

};
</script>

<style scoped>
.point-of-sale {
  padding: 20px;
  background-color: #f8f8f8;
  font-family: Arial, sans-serif;
  max-width: 100%;
  display: flex;
}
</style>
