import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '@/assets/font/font.css';
import Element from 'element-plus'
import "echarts-gl";

createApp(App).use(store).use(router).use(Element).mount('#app')
