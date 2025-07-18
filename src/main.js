import { createApp } from 'vue'
import App from './FrontEnd/App.vue'
import router from './FrontEnd/router'
import './FrontEnd/assets/styles.css'

createApp(App).use(router).mount('#app')
