<template>
  <div class="pos-receipt">
    <div class="header">
      <h1>Receipt</h1>
    </div>
    <p>Thank you for your order!</p>
    <p>Order Number: #12345</p>
    <p>Date: {{ new Date().toLocaleDateString() }}</p>
    <p>Time: {{ new Date().toLocaleTimeString() }}</p>

    <h2>Items Ordered:</h2>
    <ul>
      <li v-for="(item, index) in groupedOrder" :key="index">
        {{ item.label }} <span v-if="item.quantity > 1">x{{ item.quantity }}</span> - £{{ item.totalPrice.toFixed(2) }}
      </li>
    </ul>

    <h2>Total: £{{ total.toFixed(2) }}</h2>

    <ReceiptButton isServed="true" @serve-clicked="$emit('serve-clicked')"/>
  </div>
</template>


<script>
import ReceiptButton from './ReceiptButton.vue';

export default {
  name: 'POSReceipt',
  components: {
    ReceiptButton
  },

  props: {
    order: {
      type: Array,
      default: () => []
    }
  },
  computed: {
  total() {
    return this.order.reduce((sum, item) => sum + item.price, 0);
  },
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
   }
  }

};
</script>


<style scoped>
.pos-receipt {
  padding: 20px;
  background-color: #ded7d7;
  font-family: Arial, sans-serif;
  max-width: 30%;
  min-width: 30%;
  text-align: center;
  border: 2px solid #ccc;
  border-radius: 5px;
  margin: 20px auto;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  align-items: center;

}

.header {
  margin-bottom: 20px;
  width: 100%;
  }

h1 {
  font-size: 2rem;
  color: #333;
  font-weight: bold;
}

h2 {
  font-size: 1.5rem;
  color: #666;
  font-weight: bold;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  padding: 5px 0;
}

.receipt-button {
  margin-top: auto;
  padding-bottom: 20px;
  padding-top: 20px;
}
</style>