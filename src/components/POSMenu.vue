<template>
  <div class="pos-menu">
    <div class="header">
      <h1>Menu</h1>
      <button @click="outageItems" :class="['outage-button', isOutage ? 'outage-on' : 'outage-off']">"Outage Toggle"</button>
    </div>

    <MenuPopUpBox v-if ="isColdDrinkPopupOpen"
      :menuItems="[{
        id: 1,
        label: 'Coca-Cola',
        price: 1.99,
        isDisabled: disabledItems.includes('Coca-Cola')
      }, {
        id: 2,
        label: 'Sprite',
        price: 1.99,
        isDisabled: disabledItems.includes('Sprite')
      }, {
        id: 3,
        label: 'Fanta',
        price: 1.99,
        isDisabled: disabledItems.includes('Fanta')
      }, {
        id: 4,
        label: 'Oasis',
        price: 1.99,
        isDisabled: disabledItems.includes('Oasis')
      }, {
        id: 5,
        label: 'Dr Pepper',
        price: 1.99,
        isDisabled: disabledItems.includes('Dr Pepper')
      },
      ]"
      menuSummary="Cold Drinks"
      @close="isColdDrinkPopupOpen = false"
      @select="handleAddItem"
    />

    <MenuPopUpBox v-if ="isHotDrinkPopupOpen"
      :menuItems="[{
        id: 1,
        label: 'Coffee',
        price: 1.99,
        isDisabled: disabledItems.includes('Coffee')
      }, {
        id: 2,
        label: 'Tea',
        price: 1.99,
        isDisabled: disabledItems.includes('Tea')
      }, {
        id: 3,
        label: 'Hot Chocolate',
        price: 2.49,
        isDisabled: disabledItems.includes('Hot Chocolate')
      }, {
        id: 4,
        label: 'Latte',
        price: 2.99,
        isDisabled: disabledItems.includes('Latte')
      }, {
        id: 5,
        label: 'Cappuccino',
        price: 2.99,
        isDisabled: disabledItems.includes('Cappuccino')
      },
      ]"
      menuSummary="Hot Drinks"
      @close="isHotDrinkPopupOpen = false"
      @select="handleAddItem"
    />

    <MenuPopUpBox v-if ="isIcedDrinkPopupOpen"
      :menuItems="[{
        id: 1,
        label: 'Iced Coffee',
        price: 2.49,
        isDisabled: disabledItems.includes('Iced Coffee')
      }, {
        id: 2,
        label: 'Iced Latte',
        price: 2.99,
        isDisabled: disabledItems.includes('Iced Latte')
      }, {
        id: 3,
        label: 'Iced Mocha',
        price: 3.49,
        isDisabled: disabledItems.includes('Iced Mocha')
      }, {
        id: 4,
        label: 'Iced Tea',
        price: 1.99,
        isDisabled: disabledItems.includes('Iced Tea')
      }, {
        id: 5,
        label: 'Iced Chocolate',
        price: 2.99,
        isDisabled: disabledItems.includes('Iced Chocolate')
      },
      ]"
      menuSummary="Iced Drinks"
      @close="isIcedDrinkPopupOpen = false"
      @select="handleAddItem"
    />

    <MenuPopUpBox v-if ="isMilkshakePopupOpen"
      :menuItems="[{
        id: 1,
        label: 'Chocolate Milkshake',
        price: 2.99,
        isDisabled: disabledItems.includes('Chocolate Milkshake')
      }, {
        id: 2,
        label: 'Strawberry Milkshake',
        price: 2.99,
        isDisabled: disabledItems.includes('Strawberry Milkshake')
      }, {
        id: 3,
        label: 'Vanilla Milkshake',
        price: 2.99,
        isDisabled: disabledItems.includes('Vanilla Milkshake')
      }, {
        id: 4,
        label: 'Oreo Milkshake',
        price: 3.49,
        isDisabled: disabledItems.includes('Oreo Milkshake')
      }, {
        id: 5,
        label: 'Mint Chocolate Milkshake',
        price: 3.49,
        isDisabled: disabledItems.includes('Mint Chocolate Milkshake')
      },
      ]"
      menuSummary="Milkshakes"
      @close="isMilkshakePopupOpen = false"
      @select="handleAddItem"
    />

    <h2>Core Items</h2>
    <div class="item-button-row">
      <ItemButton label="Big Mac" :price="5.99" :is-disabled="disabledItems.includes('Big Mac')" @add-to-order="handleAddItem" />
      <ItemButton label="Quarter Pounder" :price="6.49" :is-disabled="disabledItems.includes('Quarter Pounder')" @add-to-order="handleAddItem" />
      <ItemButton label="Double Quarter Pounder" :price="7.99" :is-disabled="disabledItems.includes('Double Quarter Pounder')" @add-to-order="handleAddItem" />
      <ItemButton label="Chicken Sandwich" :price="4.99" :is-disabled="disabledItems.includes('Chicken Sandwich')" @add-to-order="handleAddItem" />
      <ItemButton label="Filet-O-Fish" :price="5.49" :is-disabled="disabledItems.includes('Filet-O-Fish')" @add-to-order="handleAddItem" />
      <ItemButton label="McCrispy" :price="6.49" :is-disabled="disabledItems.includes('McCrispy')" @add-to-order="handleAddItem" />
      <ItemButton label="McSpicy" :price="6.49" :is-disabled="disabledItems.includes('McSpicy')" @add-to-order="handleAddItem" />
    </div>

    <h2>Saver Items</h2>
    <div class="item-button-row">
      <ItemButton label="Cheeseburger" :price="1.99" :is-disabled="disabledItems.includes('Cheeseburger')" @add-to-order="handleAddItem" />
      <ItemButton label="Double Cheeseburger" :price="2.49" :is-disabled="disabledItems.includes('Double Cheeseburger')" @add-to-order="handleAddItem" />
      <ItemButton label="Hamburger" :price="3.49" :is-disabled="disabledItems.includes('Hamburger')" @add-to-order="handleAddItem" />
      <ItemButton label="Mayo Chicken" :price="3.99" :is-disabled="disabledItems.includes('Mayo Chicken')" @add-to-order="handleAddItem" />
    </div>

    <h2>Vegetarian Options</h2>
    <div class="item-button-row">
      <ItemButton label="Vegetable Deluxe" :price="4.99" :is-disabled="disabledItems.includes('Vegetable Deluxe')" @add-to-order="handleAddItem" />
      <ItemButton label="Veggie Dippers" :price="3.99" :is-disabled="disabledItems.includes('Veggie Dippers')" @add-to-order="handleAddItem" />
      <ItemButton label="Spicy Veggie Wrap" :price="5.49" :is-disabled="disabledItems.includes('Spicy Veggie Wrap')" @add-to-order="handleAddItem" />
      <ItemButton label="McPlant" :price="4.49" :is-disabled="disabledItems.includes('McPlant')" @add-to-order="handleAddItem" />
    </div>

    <h2>Sides</h2>
    <div class="item-button-row">
      <ItemButton label="French Fries" :price="1.99" :is-disabled="disabledItems.includes('French Fries')" @add-to-order="handleAddItem" />
      <ItemButton label="Apple Slices" :price="1.49" :is-disabled="disabledItems.includes('Apple Slices')" @add-to-order="handleAddItem" />
      <ItemButton label="Side Salad" :price="2.49" :is-disabled="disabledItems.includes('Side Salad')" @add-to-order="handleAddItem" />
      <ItemButton label="Mozzarella Sticks" :price="3.49" :is-disabled="disabledItems.includes('Mozzarella Sticks')" @add-to-order="handleAddItem" />
      <ItemButton label="Chicken Nuggets" :price="4.99" :is-disabled="disabledItems.includes('Chicken Nuggets')" @add-to-order="handleAddItem" />
    </div>

    <h2>Drinks</h2>
    <div class="item-button-row">
      <PopUpButton label="Cold Drinks" @pop-up-clicked="handlePopUpClicked('Cold Drinks')"/>
      <PopUpButton label="Hot Drinks" @pop-up-clicked="handlePopUpClicked('Hot Drinks')"/>
      <PopUpButton label="Iced Drinks" @pop-up-clicked="handlePopUpClicked('Iced Drinks')"/>
      <PopUpButton label="Milkshakes" @pop-up-clicked="handlePopUpClicked('Milkshakes')"/>
    </div>
    
    <h2>Desserts</h2>
    <div class="item-button-row">
      <ItemButton label="Apple Pie" :price="1.49" :is-disabled="disabledItems.includes('Apple Pie')" @add-to-order="handleAddItem" />
      <ItemButton label="Sundae" :price="2.49" :is-disabled="disabledItems.includes('Sundae')" @add-to-order="handleAddItem" />
      <ItemButton label="McFlurry" :price="3.49" :is-disabled="disabledItems.includes('McFlurry')" @add-to-order="handleAddItem" />
      <ItemButton label="Cookies" :price="1.99" :is-disabled="disabledItems.includes('Cookies')" @add-to-order="handleAddItem" />
      <ItemButton label="Brownie" :price="2.99" :is-disabled="disabledItems.includes('Brownie')" @add-to-order="handleAddItem" />
    </div>

    <h2>Extras</h2>
    <div class="item-button-row">
      <ItemButton label="Ketchup" :price="0.00" :is-disabled="disabledItems.includes('Ketchup')" @add-to-order="handleAddItem" />
      <ItemButton label="Mustard" :price="0.00" :is-disabled="disabledItems.includes('Mustard')" @add-to-order="handleAddItem" />
      <ItemButton label="Mayonnaise" :price="0.00" :is-disabled="disabledItems.includes('Mayonnaise')" @add-to-order="handleAddItem" />
      <ItemButton label="BBQ Sauce" :price="0.00" :is-disabled="disabledItems.includes('BBQ Sauce')" @add-to-order="handleAddItem" />
      <ItemButton label="Sweet and Sour Sauce" :price="0.00" :is-disabled="disabledItems.includes('Sweet and Sour Sauce')" @add-to-order="handleAddItem" />
      <ItemButton label="Hot Sauce" :price="0.00" @add-to-order="handleAddItem" />
    </div>
  </div>
  
</template>

<script>
import ItemButton from './ItemButton.vue';
import MenuPopUpBox from './MenuPopUpBox.vue';
import PopUpButton from './PopUpButton.vue';
export default {
  name: 'POSMenu',
  components: {
    ItemButton,
    MenuPopUpBox,
    PopUpButton
  },
  methods: {
    handleAddItem(item) {
      if (this.isOutage) {
        if (this.disabledItems.includes(item.label)) {
          this.disabledItems = this.disabledItems.filter(i => i !== item.label);
        } else {
          this.disabledItems.push(item.label);
        }
      } else {
        this.$emit('item-selected', item);
      }
    },
    closePopUps(){
      this.isColdDrinkPopupOpen = false;
      this.isHotDrinkPopupOpen = false;
      this.isIcedDrinkPopupOpen = false;
      this.isMilkshakePopupOpen = false;
    },
    handlePopUpClicked(menuType) {
      this.closePopUps();
      switch (menuType) {
        case 'Cold Drinks':
          this.isColdDrinkPopupOpen = !this.isColdDrinkPopupOpen;
          break;
        case 'Hot Drinks':
          this.isHotDrinkPopupOpen = !this.isHotDrinkPopupOpen;
          break;
        case 'Iced Drinks':
          this.isIcedDrinkPopupOpen = !this.isIcedDrinkPopupOpen;
          break;
        case 'Milkshakes':
          this.isMilkshakePopupOpen = !this.isMilkshakePopupOpen;
          break;
      }
    },
    outageItems() {
      this.isOutage = !this.isOutage;
    }
  },
  data() {
    return {
      isColdDrinkPopupOpen: false,
      isHotDrinkPopupOpen: false,
      isIcedDrinkPopupOpen: false,
      isMilkshakePopupOpen: false,
      isOutage: false,
      disabledItems: []
    };
  },
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
.outage-on, .outage-off {
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

.outage-on {
  background-color: green;
}

.outage-off {
  background-color: #ff0000;
}


</style>