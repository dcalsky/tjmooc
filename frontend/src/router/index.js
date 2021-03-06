import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/home/index.vue'
import About from '../views/About.vue'
import Copyright from '../views/Copyright.vue'
import Notfound from '../views/404.vue'

// Account
const Account = r => require.ensure([], () => r(require('../views/account/account.vue')), 'account')
const AccountRegister = r => require.ensure([], () => r(require('../views/account/register/register.vue')), 'account')
const AccountLogin = r => require.ensure([], () => r(require('../views/account/login/login.vue')), 'account')

// // Course
const Course = r => require.ensure([], () => r(require('../views/course')), 'course')
// const CourseDisplay = r => require.ensure([], () => r(require('views/course/display')), 'course')
// const CourseList = r => require.ensure([], () => r(require('views/course/list')), 'course')
// const CourseAdd = r => require.ensure([], () => r(require('views/course/add')), 'course')
//
// // Forum
const Forum = r => require(['../views/forum/forum'], r)
const ForumList = r => require(['../views/forum/forum-list'], r)
const ForumDetail = r => require(['../views/forum/floors'], r)
const PostDetail = r => require(['../views/forum/post'], r)
//
// Manage
const Manage = r => require(['../views/manage'], r)
const ManageAfterclass = r => require(['../views/manage/afterclass.vue'], r)
const ManageCourse = r => require(['../views/manage/course.vue'], r)

Vue.use(Router)

const router = new Router({
  mode: 'hash',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: {
        scrollTop: 0
      }
    },
    {
      path: '/about',
      name: 'about',
      component: About,
      meta: {
        scrollTop: 0
      }
    }, {
      path: '/copyright',
      component: Copyright,
      meta: {
        scrollTop: 0
      }
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
        }
      ],
      meta: {
        scrollTop: 0
      }
    }, {
      path: '/profile',
      name: 'profile',
      component: Home,
      meta: {
        scrollTop: 0
      }
    },
    {
      path: '/course/:courseId',
      component: Course,
      name: 'course',
      meta: {
        scrollTop: 0
      }
      //   children: [
      //     {
      //       path: 'display/:courseId',
      //       component: CourseDisplay
      //     },
      //     {
      //       path: 'list',
      //       component: CourseList
      //     },
      //     {
      //       path: 'add',
      //       component: CourseAdd
      //     }
      //   ]
    },
    {
      path: '/manage',
      component: Manage,
      name: 'manage',
      children: [
        {
          path: 'course',
          name: 'manage-course',
          component: ManageCourse
        },
        {
          path: 'afterclass',
          name: 'manage-afterclass',
          component: ManageAfterclass
        }
      ],
      meta: {
        scrollTop: 0
      }
    },
    {
      path: '/bbs',
      component: Forum,
      name: 'bbs',
      children: [
        {
          path: '/',
          component: ForumList,
          name: 'forumList'
        }, {
          path: 'forum/:forumId',
          component: ForumDetail,
          name: 'forumDetail'
        }, {
          path: 'post/:postId',
          component: PostDetail,
          name: 'postDetail'
        }
      ]
    },
    {
      path: '*',
      name: 'notfound',
      component: Notfound,
      meta: {
        scrollTop: 0
      }
    }
  ]
})

router.beforeEach((to, from, next) => {
  from.meta.scrollTop = window.scrollY
  next()
})

router.afterEach((to, from) => {
  window.scrollTo(0, to.meta.scrollTop)
})

export default router
