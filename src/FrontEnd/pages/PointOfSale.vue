<template>
  <div class="header">
    <h1>Point of Sale</h1>
  </div>
  <BackButton label="Back" to="/" />

  <div class="point-of-sale">
    <POSMenu ref="posMenuRef" @item-selected="addItemToOrder" />
    <POSReceipt @serve-clicked="handleServeClicked" :order="order" v-if="isReceiptVisible" />
    <POSOrder @serve-clicked="handleServeClicked" @remove-item="removeItemFromOrder" :order="order" v-if="!isReceiptVisible" />
    <div class="order-served-notification" v-if="isOrderNotificationVisible">
      <p>ORDER SERVED</p>
    </div>
  </div>
</template>


<script>
import BackButton from '../components/BackButton.vue';
import ItemButton from '../components/POSComponents/ItemButton.vue';
import POSMenu from '../components/POSComponents/POSMenu.vue';
import POSReceipt from '../components/POSComponents/POSReceipt.vue';
import POSOrder from '../components/POSComponents/POSOrder.vue';

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
      isReceiptVisible: false,
      isEditingOrder: false,
      isOrderNotificationVisible: false
    };
  },
  methods: {
    addItemToOrder(item) {
      if (this.isReceiptVisible) {
        this.isReceiptVisible = false;
        this.order = [];
      }
      this.order.push(item);
    },
    handleServeClicked() {
      this.callPOSMenuMethod();
      if (this.isReceiptVisible) {
        this.isEditingOrder = true;
      }
      else{
        if (this.isEditingOrder){ // If we are editing an order, we want to send the updated order, and delete the previous one
          fetch('http://localhost:5000/orders/latest', {
            method: 'DELETE',
          })
          .then(response => response.json())
          .then(data => {
            console.log('Order deleted successfully:', data);
          })
          .catch(error => {
            console.error('Error deleting order:', error);
          });
        }
        this.sendOrderToServer();
        this.orderServedNotification();
        this.isEditingOrder = false;
      }
      this.isReceiptVisible = !this.isReceiptVisible;
    },
    sendOrderToServer() {
      fetch('http://localhost:5000/orders', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          price: this.groupedOrder.reduce((total, item) => total + item.totalPrice, 0),
          items: this.groupedOrder
        })
      })
      .then(response => response.json())
      .then(data => {
        console.log('Order sent to server:', data);
      })
      .catch(error => {
        console.error('Error sending order to server:', error);
      });
    },
    callPOSMenuMethod() {
      this.$refs.posMenuRef.closePopUps();
    },
    removeItemFromOrder(itemLabel) {
      const index = this.order.findIndex(item => item.label === itemLabel);
      if (index !== -1) {
        this.order.splice(index, 1);
      }
    },
    orderServedNotification() {
      this.isOrderNotificationVisible = true;
      setTimeout(() => {
        this.isOrderNotificationVisible = false;
      }, 2000); // Notification will disappear after 2 seconds
    }
  },
  computed: {
    groupedOrder() {
      const map = new Map();

      for (const item of this.order) {
        const key = item.label;

        if (map.has(key)) { // If the item already exists, update its quantity and total price
          const existing = map.get(key);
          existing.quantity += 1;
          existing.totalPrice += item.price;
        } else {
          map.set(key, {
            label: item.label,
            price: item.price,
            quantity: 1,
            totalPrice: item.price
          });
        }
      }
      return Array.from(map.values());
    },
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
.order-served-notification {
  position: fixed;
  background-color: #4CAF50;
  color: white;
  padding: 10px;
  border-radius: 5px;
  width: 500px;
  height: 400px;
  text-align: center;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 0.9;
  transition: opacity 0.5s ease-in-out;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  font-size: 3rem;
  text-emphasis: bold;
}
</style>
