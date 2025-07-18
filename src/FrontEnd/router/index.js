import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import PointOfSale from '../pages/PointOfSale.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/PointOfSale', component: PointOfSale },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
