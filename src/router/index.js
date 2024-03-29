import {createRouter, createWebHashHistory} from 'vue-router'

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
        path: '/dataanalysis',
        name: 'dataanalysis',
        component: () => import('../views/DataAnalysisView.vue')
    },
    {
        path: '/anhuiwater',
        name: 'anhuiwater',
        component: () => import('../views/AnHuiWaterView.vue')
    },
    {
        path: '/anhuiwind',
        name: 'anhuiwind',
        component: () => import('../views/AnHuiWindView.vue')
    },
    {
        path: '/anhuilimit',
        name: 'anhuilimit',
        component: () => import('../views/AnHuiLimitView.vue')
    },
    {
        path: '/sunenergy',
        name: 'sunenergy',
        component: () => import('../views/SunEnergyView.vue')
    },
    {
        path: '/waterconser',
        name: 'waterconser',
        component: () => import('../views/WaterConserView.vue')
    },
    {
        path: '/windenergy',
        name: 'windenergy',
        component: () => import('../views/WindEnergyView.vue')
    },
    {
        path: '/thermalpower',
        name: 'thermalpower',
        component: () => import('../views/ThermalPowerView.vue')
    },
    {
        path: '/beijing',
        name: 'beijing',
        component: () => import('../views/BeiJingRenewView.vue')
    },
]

const router = createRouter({
    history: createWebHashHistory(process.env.BASE_URL),
    routes
})

export default router

