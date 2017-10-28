// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

import 'normalize-css/normalize.css'
import 'font-awesome/css/font-awesome.css'
import '../theme/index.css'
import Vue from 'vue'
import ElementUI from 'element-ui'
import App from './views/App.vue'
import router from './router'
import store from './store'
import { sync } from 'vuex-router-sync'

sync(store, router)

Vue.config.productionTip = false

Vue.use(ElementUI)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
