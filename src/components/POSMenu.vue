<template>
  <div class="pos-menu">
    <div class="header">
      <h1>Menu</h1>
    </div>

    <h2>Core Items</h2>
    <div class="item-button-row">
      <ItemButton label="Big Mac" :price="5.99" @add-to-order="handleAddItem" />
      <ItemButton label="Quarter Pounder" :price="6.49" @add-to-order="handleAddItem" />
      <ItemButton label="Double Quarter Pounder" :price="7.99" @add-to-order="handleAddItem" />
      <ItemButton label="Chicken Sandwich" :price="4.99" @add-to-order="handleAddItem" />
      <ItemButton label="Filet-O-Fish" :price="5.49" @add-to-order="handleAddItem" />
      <ItemButton label="McCrispy" :price="6.49" @add-to-order="handleAddItem" />
      <ItemButton label="McSpicy" :price="6.49" @add-to-order="handleAddItem" />
    </div>

    <h2>Saver Items</h2>
    <div class="item-button-row">
      <ItemButton label="Cheeseburger" :price="1.99" @add-to-order="handleAddItem" />
      <ItemButton label="Double Cheeseburger" :price="2.49" @add-to-order="handleAddItem" />
      <ItemButton label="Hamburger" :price="3.49" @add-to-order="handleAddItem" />
      <ItemButton label="Mayo Chicken" :price="3.99" @add-to-order="handleAddItem" />
    </div>

    <h2>Vegetarian Options</h2>
    <div class="item-button-row">
      <ItemButton label="Vegetable Deluxe" :price="4.99" @add-to-order="handleAddItem" />
      <ItemButton label="Veggie Dippers" :price="3.99" @add-to-order="handleAddItem" />
      <ItemButton label="Spicy Veggie Wrap" :price="5.49" @add-to-order="handleAddItem" />
      <ItemButton label="McPlant" :price="4.49" @add-to-order="handleAddItem" />
    </div>

    <h2>Sides</h2>
    <div class="item-button-row">
      <ItemButton label="French Fries" :price="1.99" @add-to-order="handleAddItem" />
      <ItemButton label="Apple Slices" :price="1.49" @add-to-order="handleAddItem" />
      <ItemButton label="Side Salad" :price="2.49" @add-to-order="handleAddItem" />
      <ItemButton label="Mozzarella Sticks" :price="3.49" @add-to-order="handleAddItem" />
      <ItemButton label="Chicken Nuggets" :price="4.99" @add-to-order="handleAddItem" />
    </div>

    <h2>Drinks</h2>
    <div class="item-button-row">
      <ItemButton label="Coke" :price="1.99" @add-to-order="handleAddItem" />
      <ItemButton label="Diet Coke" :price="1.99" @add-to-order="handleAddItem" />
      <ItemButton label="Sprite" :price="1.99" @add-to-order="handleAddItem" />
      <ItemButton label="Fanta" :price="1.99" @add-to-order="handleAddItem" />
      <ItemButton label="Iced Coffee" :price="2.49" @add-to-order="handleAddItem" />
      <ItemButton label="Milkshake" :price="3.49" @add-to-order="handleAddItem" />
    </div>
    
    <h2>Desserts</h2>
    <div class="item-button-row">
      <ItemButton label="Apple Pie" :price="1.49" @add-to-order="handleAddItem" />
      <ItemButton label="Sundae" :price="2.49" @add-to-order="handleAddItem" />
      <ItemButton label="McFlurry" :price="3.49" @add-to-order="handleAddItem" />
      <ItemButton label="Cookies" :price="1.99" @add-to-order="handleAddItem" />
      <ItemButton label="Brownie" :price="2.99" @add-to-order="handleAddItem" />
    </div>

    <h2>Extras</h2>
    <div class="item-button-row">
      <ItemButton label="Ketchup" :price="0.00" @add-to-order="handleAddItem" />
      <ItemButton label="Mustard" :price="0.00" @add-to-order="handleAddItem" />
      <ItemButton label="Mayonnaise" :price="0.00" @add-to-order="handleAddItem" />
      <ItemButton label="BBQ Sauce" :price="0.00" @add-to-order="handleAddItem" />
      <ItemButton label="Sweet and Sour Sauce" :price="0.00" @add-to-order="handleAddItem" />
      <ItemButton label="Hot Sauce" :price="0.00" @add-to-order="handleAddItem" />
    </div>
  </div>
  
</template>

<script>
import ItemButton from './ItemButton.vue';
export default {
  name: 'POSMenu',
  components: {
    ItemButton
  },
  methods: {
  handleAddItem(item) {
    this.$emit('item-selected', item);
  }
}

};
</script>

<style scoped>
.pos-menu {
  padding: 20px;
  background-color: #ffdbdb;
  font-family: Arial, sans-serif;
  max-width: 70%;
  min-width: 70%;
  border: 2px solid #ccc;
  border-radius: 5px;
  margin: 20px auto;
}

.item-button-row {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}
.h2 {
  margin-top: 20px;
  margin-bottom: 10px;
  font-size: 1.5rem;
  color: #333;
  font-weight: bold;
  margin-left: 200px;
}
</style>