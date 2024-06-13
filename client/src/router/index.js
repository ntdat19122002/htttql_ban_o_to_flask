import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Contact from '../views/Contact.vue'
import car_route from './car'
import admin_route from './admin'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard
    },
    {
      path: '/loai_xe/:id',
      name: 'loai_xe',
      component: Dashboard
    },
    {
      path: '/contact/:id',
      name: 'contact',
      component: Contact
    },
    ...admin_route,
    ...car_route
  ]
})

export default router
