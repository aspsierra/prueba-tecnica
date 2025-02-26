import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { Api } from '@/services/api' 

const app = createApp(App)
app.config.globalProperties.$api = new Api()
app.use(router)

app.mount('#app')
