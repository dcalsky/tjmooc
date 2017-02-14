import * as types from '../mutation-types'
import { session } from '../../api'
import router from 'vue-router'

// state
const state = {
  token: null
}

// getters
const getters = {
  checkoutStatus: state => state.checkoutStatus
}

// actions
const actions = {
  login ({ commit }, data) {
    session.login(data, (err, res) => {
      // error handle
      commit(types.LOGIN, res.token)
    })
  },
  logout ({ commit }) {
    commit(types.LOGOUT)
  }
}

const mutations = {
  [types.LOGIN] (state, token) {
    state.token = token
    // Return profile page
    router.push({ name: 'profile' })
  },
  [types.LOGOUT] (state) {
    state.token = null
    // Return home page
    router.push({ name: 'home' })
  }
}


export default {
  state,
  getters,
  actions,
  mutations
}
