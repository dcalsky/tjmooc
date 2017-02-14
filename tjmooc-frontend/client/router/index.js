import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
import Account from '../views/account/account.vue'
import AccountRegister from '../views/account/register/register'
import AccountLogin from '../views/account/login/login'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/account',
      component: Account,
      children: [
        {
          path: 'register',
          component: AccountRegister,
        },
        {
          path: 'login',
          component: AccountLogin,
        },
      ]
    }
  ]
})
