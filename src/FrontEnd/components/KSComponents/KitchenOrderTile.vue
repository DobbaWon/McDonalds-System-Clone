<template>
  <div
    class="kitchen-order-tile"
    :class="{ empty: !order }"
  >
    <div v-if="order" class="order-content">
      <h3>Order #{{ order.id }}</h3>

      <ul>
        <li v-for="(item, index) in parsedItems" :key="index">
          {{ item.quantity }} × {{ item.label }} — ${{ item.totalPrice.toFixed(2) }}
        </li>
      </ul>

      <div class="order-footer">
        <button class="complete-order-button" @click="$emit('complete', order.id)">
          Complete Order
        </button>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'KitchenOrderTile',
  props: {
    order: {
      type: Object,
      default: null
    }
  },
  computed: {
    parsedItems() {
      if (!this.order || !this.order.items) return []
      try {
        return JSON.parse(this.order.items)
      } catch (err) {
        console.error('Invalid JSON in order.items:', err)
        return []
      }
    }
  }
}
</script>

<style scoped>
.kitchen-order-tile {
  width: 800px;
  min-height: 400px;
  background-color: #ffffff;
  border: 2px dashed #ccc;
  border-radius: 12px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
  transition: background-color 0.3s ease;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  font-size: 1.4rem;
}

.kitchen-order-tile.empty {
  background-color: #444;
  border-color: #666;
}

.complete-order-button {
  background-color: #4CAF50; /* Green */
  color: white;
  padding: 10px 20px;
  border: 3px solid #4CAF50;
  border-radius: 15px;
  cursor: pointer;
  font-size: 1.2rem;
  font-weight: bold;
  margin-top: auto;
  padding-top: 20px;
}
.order-content {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.order-footer {
  margin-top: auto;
  display: flex;
  justify-content: center;
  padding-top: 20px;
}
</style>
