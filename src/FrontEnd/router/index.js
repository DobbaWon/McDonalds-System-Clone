import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import PointOfSale from '../pages/PointOfSale.vue'
import KitchenScreen from '../pages/KitchenScreen.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/PointOfSale', component: PointOfSale },
  { path: '/KitchenScreen', component: KitchenScreen },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
