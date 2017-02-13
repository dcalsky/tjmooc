import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
import Account from '../views/Account'
import AccountLogin from '../components/account/register/register'

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
          component: AccountLogin,
        },
        {
          path: 'login',
          component: Home,
        },
      ]
    }
  ]
})
