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
      <li>Burger - $5.99</li>
      <li>Fries - $2.49</li>
      <li>Coke - $1.99</li>
    </ul>

    <h2>Total: $10.47</h2>
  </div>
</template>

<script>
export default {
  name: 'POSReceipt',
  components: {
  }
};
</script>

<style scoped>
.pos-receipt {
  padding: 20px;
  background-color: #f8f8f8;
  font-family: Arial, sans-serif;
  max-width: 30%;
  min-width: 30%;
  text-align: center;
  border: 2px solid #ccc;
  border-radius: 5px;
  margin: 20px auto;
}

.header {
  margin-bottom: 20px;
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
</style>