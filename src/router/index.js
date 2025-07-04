import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import POSHome from '../pages/point-of-sale-pages/POSHome.vue'
import PointOfSale from '../pages/point-of-sale-pages/PointOfSale.vue'
import DriveThruSpeakerPOS from '../pages/point-of-sale-pages/DriveThruSpeakerPOS.vue'
import DriveThruCashierPOS from '../pages/point-of-sale-pages/DriveThruCashierPOS.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/POSHome', component: POSHome },
  { path: '/PointOfSale', component: PointOfSale },
  { path: '/DriveThruSpeakerPOS', component: DriveThruSpeakerPOS },
  { path: '/DriveThruCashierPOS', component: DriveThruCashierPOS },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
