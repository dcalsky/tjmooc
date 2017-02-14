import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from '../utils/logger'
import session from './modules/session'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

const store = new Vuex.Store({
  modules: {
    session
  },
  strict: debug,
  plugins: debug ? [createLogger()] : []
})

export default store
