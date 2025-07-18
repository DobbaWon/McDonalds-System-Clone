<template>
  <div class="kitchen-screen">
    <div class="header">
      <h1>Kitchen Screen</h1>
      <BackButton label="Back" to="/" />
    </div>

    <h2 v-if="orders.length > 6">{{ orders.length - 6}} Pending Orders</h2>

  <div class="orders-grid">
    <KitchenOrderTile
      v-for="(order, index) in visibleOrders"
      :key="'order-' + order.id"
      :order="order"
      @complete="completeOrder"
    />

  </div>

  </div>
</template>

<script>
import BackButton from '../components/BackButton.vue';
import KitchenOrderTile from '../components/KSComponents/KitchenOrderTile.vue';

export default {
  name: 'KitchenScreen',
  components: {
    BackButton,
    KitchenOrderTile
  },
  data() {
    return {
      orders: [],
      intervalId: null
    }
  },
  computed: {
    visibleOrders() {
      return this.orders.slice(0, 6)
    },
    emptyTileCount() {
      return 6 - this.visibleOrders.length
    }
  },
  methods: {
    async fetchOrders() {
      try {
        const response = await fetch('http://localhost:5000/orders')
        const data = await response.json()
        this.orders = data
        console.log('Fetched orders:', this.orders)
      } catch (error) {
        console.error('Error fetching orders:', error)
      }
    },

    async completeOrder(orderId) {  // <-- move here inside methods!
      try {
        const response = await fetch(`http://localhost:5000/orders/${orderId}`, {
          method: 'DELETE'
        });
        if (!response.ok) {
          throw new Error('Failed to complete order');
        }
        await this.fetchOrders(); // Refresh orders after deletion
      } catch (error) {
        console.error('Error completing order:', error);
      }
    }
  },
  mounted() {
    this.fetchOrders()
    this.intervalId = setInterval(this.fetchOrders, 5000)
  },
  beforeUnmount() {
    clearInterval(this.intervalId)
  }
}

</script>

<style scoped>
.kitchen-screen {
  padding: 20px;
  background-color: #f8f8f8;
  font-family: Arial, sans-serif;
  max-width: 100%;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.orders-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(2, auto);
  gap: 20px;
}
</style>
