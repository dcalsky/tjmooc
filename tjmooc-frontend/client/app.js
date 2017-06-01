import Vue from 'vue'
import { sync } from 'vuex-router-sync'
import '../theme/index.css'
import ElementUI from 'element-ui'
import App from './components/App'
import router from './router'
import store from './store'
sync(store, router)

Vue.use(ElementUI)

const app = new Vue({
  router,
  store,
  ...App
})

export { app, router, store }
