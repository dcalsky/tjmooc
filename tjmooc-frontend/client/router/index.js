import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
import Account from '../views/account/account.vue'
import AccountRegister from '../views/account/register/register'
import AccountLogin from '../views/account/login/login'
import Course from '../views/course/course.vue'
import CourseDisplay from '../views/course/display.vue'
import CourseList from '../views/course/list.vue'
import About from '../views/About.vue'
import Copyright from '../views/Copyright.vue'
import Forum from '../views/forum/forum.vue'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    }, {
      path: '/about',
      name: 'about',
      component: About
    }, {
      path: '/copyright',
      component: Copyright
    }, {
      path: '/account',
      component: Account,
      children: [
        {
          path: 'register',
          component: AccountRegister,
          name: 'register'
        }, {
          path: 'login',
          component: AccountLogin,
          name: 'login'
        }]
    }, {
      path: '/profile',
      name: 'profile',
      component: Home
    }, {
      path: '/course',
      component: Course,
      name: 'course',
      children: [
        {
          path: 'display/:courseId',
          component: CourseDisplay
        },
        {
          path: 'list',
          component: CourseList
        }
      ] },
    {
      path: '/bbs',
      component: Forum,
      name: 'bbs'
    }
  ]
})
