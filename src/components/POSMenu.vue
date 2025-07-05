<template>
  <div class="item-button-row">
    <h2>Core Items</h2>
    <ItemButton label="Big Mac" price="5.99"/>
    <ItemButton label="Quarter Pounder" price="6.49"/>
    <ItemButton label="Double Quarter Pounder" price="7.99"/>
    <ItemButton label="Chicken Sandwich" :price="4.99"/>
    <ItemButton label="Filet-O-Fish" :price="5.49"/>
    <ItemButton label="McCrispy" :price="6.49"/>
    <ItemButton label="McSpicy" :price="6.49"/>
  </div>

  <div class="item-button-row">
    <h2>Saver Items</h2>
    <ItemButton label="Cheeseburger" :price="1.99"/>
    <ItemButton label="Double Cheeseburger" :price="2.49"/>
    <ItemButton label="Hamburger" :price="3.49"/>
    <ItemButton label="Mayo Chicken" :price="3.99"/>
  </div>

  <div class="item-button-row">
    <h2>Vegetarian Options</h2>
    <ItemButton label="Vegetable Deluxe" :price="4.99"/>
    <ItemButton label="Veggie Dippers" :price="3.99"/>
    <ItemButton label="Spicy Veggie Wrap" :price="5.49"/>
    <ItemButton label="McPlant" :price="4.49"/>
  </div>

  <div class="item-button-row">
    <h2>Sides</h2>
    <ItemButton label="French Fries" :price="1.99"/>
    <ItemButton label="Apple Slices" :price="1.49"/>
    <ItemButton label="Side Salad" :price="2.49"/>
    <ItemButton label="Mozzarella Sticks" :price="3.49"/>
    <ItemButton label="Chicken Nuggets" :price="4.99"/>
  </div>

  <div class="item-button-row">
    <h2>Drinks</h2>
    <ItemButton label="Coke" price="1.99"/>
    <ItemButton label="Diet Coke" price="1.99"/>
    <ItemButton label="Sprite" :price="1.99"/>
    <ItemButton label="Fanta" :price="1.99"/>
    <ItemButton label="Iced Coffee" :price="2.49"/>
    <ItemButton label="Milkshake" :price="3.49"/>
  </div>
  
  <div class="item-button-row">
    <h2>Desserts</h2>
    <ItemButton label="Apple Pie" :price="1.49"/>
    <ItemButton label="Sundae" :price="2.49"/>
    <ItemButton label="McFlurry" :price="3.49"/>
    <ItemButton label="Cookies" :price="1.99"/>
    <ItemButton label="Brownie" :price="2.99"/>
  </div>

  <div class="item-button-row">
    <h2>Extras</h2>
    <ItemButton label="Ketchup" price="0.00"/>
    <ItemButton label="Mustard" :price="0.00"/>
    <ItemButton label="Mayonnaise" :price="0.00"/>
    <ItemButton label="BBQ Sauce" :price="0.00"/>
    <ItemButton label="Sweet and Sour Sauce" :price="0.00"/>
    <ItemButton label="Hot Sauce" :price="0.00"/>
  </div>

</template>

<script>
import ItemButton from './ItemButton.vue';
export default {
  name: 'POSMenu',
  components: {
    ItemButton
  }
};
</script>

<style scoped>
</style>