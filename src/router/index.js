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
    component: () => import('../views/AnHuiRenewView.vue')
  },
  {
    path: '/anhuirenew',
    name: 'anhuirenew',
    component: () => import('../views/AnHuiRenewView.vue')
  },
  {
    path: '/anhuisun',
    name: 'anhuisun',
    component: () => import('../views/AnHuiSunView.vue')
  },

  {
    path: '/anhuiwater',
    name: 'anhuiwater',
    component: () => import('../views/AnHuiWaterView.vue')
  },
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router

