import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from '../utils/logger'
import session from './modules/session'
import user from './modules/user'
import course from './modules/course'
import material from './modules/material'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

const store = new Vuex.Store({
  modules: {
    session,
    user,
    course,
    material
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})

export default store
