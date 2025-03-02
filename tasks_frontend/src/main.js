import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import { Api } from '@/services/api' 
import { Auth } from './services/auth'

const app = createApp(App)
app.config.globalProperties.$api = new Api()
app.config.globalProperties.$auth = new Auth()
app.use(router)
app.use(createPinia())

app.mount('#app')
