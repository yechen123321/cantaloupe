import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomeView.vue')
  },
  {
    path: '/firstcity',
    name: 'firstcity',
    component: () => import('../views/AnHuiCityView.vue')
  },
  {
    path: '/anhui',
    name: 'anhui',
    component: () => import('../views/AnHuiCityView.vue')
  },

]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router

