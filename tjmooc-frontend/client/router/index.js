import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
import About from '../views/About.vue'
import Copyright from '../views/Copyright.vue'
import VideoUpload from '../views/video/upload.vue'

// Account
const Account = r => require.ensure([], () => r(require('../views/account/account.vue')), 'account')
const AccountRegister = r => require.ensure([], () => r(require('../views/account/register/register')), 'account')
const AccountLogin = r => require.ensure([], () => r(require('../views/account/login/login')), 'account')

// Course
const Course = r => require.ensure([], () => r(require('../views/course/course.vue')), 'course')
const CourseDisplay = r => require.ensure([], () => r(require('../views/course/display.vue')), 'course')
const CourseList = r => require.ensure([], () => r(require('../views/course/list.vue')), 'course')
const CourseAdd = r => require.ensure([], () => r(require('../views/course/add.vue')), 'course')

// Forum
const Forum = r => require(['../views/forum/forum.vue'], r)

// Manage
const Manage = r => require(['../views/manage/manage.vue'], r)

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
      path: '/video',
      name: 'video',
      component: VideoUpload
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
          name: 'login',
        }
      ]
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
        },
        {
          path: 'add',
          component: CourseAdd
        }
      ]
    },
    {
      path: '/manage',
      component: Manage,
      name: 'manage'
    },
    {
      path: '/bbs',
      component: Forum,
      name: 'bbs'
    }
  ]
})
