<template>
  <div class="menu-popup-box">
    <div class="header">
      <h2>{{ menuSummary }}</h2>
      <button @click="closeMenu">Close</button>
    </div>
    <ul class="menu-items">
      <div class="item-button-row">
        <div v-for="item in menuItems" :key="item.id">
          <ItemButton
            :label="item.label"
            :price="item.price"
            @add-to-order="selectItem(item)"
          />
        </div>
      </div>
    </ul>
  </div>
</template>

<script>
import ItemButton from './ItemButton.vue';

export default {
  name: 'MenuPopUpBox',
  components: {
    ItemButton
  },
  props: {
    menuItems: {
      type: Array,
      required: true
    },
    menuSummary: {
      type: String,
      default: ''
    }
  },
  methods: {
    closeMenu() {
      this.$emit('close');
    },
    selectItem(item) {
      this.$emit('select', item);
      this.closeMenu();
    }
  }
};
</script>

<style scoped>
.menu-popup-box {
  position: absolute;
  top: 900px;
  left: 35%;
  width: 50%;
  height: 40%;
  transform: translate(-50%, -50%);
  background-color: white;
  border: 2px solid rgb(61, 60, 60);
  border-radius: 10px;
  padding: 20px;
  z-index: 1000;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

.item-button-row {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 20px;
  margin-left: -20px;
}

.header h2 {
  margin: 0;
  font-size: 1.5rem;
}
.header button {
  background-color: rgb(201, 197, 197);
  border: 2px solid rgb(61, 60, 60);
  border-radius: 5px;
  cursor: pointer;
  padding: 10px;
}

</style>