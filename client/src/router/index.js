import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Information from '../views/Information.vue'
import Car from '../views/NewCar.vue'
import car_route from './car'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard
    },
    {
      path: '/information',
      name: 'information',
      component: Information
    },
    {
      path: '/loai_xe/:id',
      name: 'loai_xe',
      component: Dashboard
    },
    ...car_route
  ]
})

export default router
