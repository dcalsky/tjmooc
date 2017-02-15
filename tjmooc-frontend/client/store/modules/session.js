import * as types from '../mutation-types'
import { session } from '../../api'
import router from '../../router'
import { errorHandler } from '../../utils'

// state
const state = {
  token: window.localStorage.getItem('token'),
  username: window.localStorage.getItem('username'),
  messages: []
}

// actions
const actions = {
  login({ commit }, data) {
    commit(types.LOGIN_REQUEST)
    session.login(data, (err, res) => {
      // error handle todo
      if (err) {
        console.log(err)
        commit(types.LOGIN_FAILED, errorHandler('error'))
      }
      if ('token' in res.body) {
        const token = res.body.token
        commit(types.LOGIN_SUCCESS, { token: token, username: data.username })
        // Set localStorage for session information
        window.localStorage.setItem('token', token)
        window.localStorage.setItem('username', data.username)
        // Success: enter profile page
        router.push({ name: 'profile' })
      } else {
        // Fail: return fail message
        commit(types.LOGIN_FAILED, errorHandler(res.body))
      }
    })
  },
  logout({ commit }) {
    commit(types.LOGOUT)
    // Clear localStorage
    window.localStorage.clear()
    // Return home page
    router.push({ name: 'home' })
  }
}

const mutations = {
  [types.LOGIN_SUCCESS](state, { token, username }) {
    state.token = token
    state.username = username
  },
  [types.LOGIN_FAILED](state, messages) {
    state.messages = messages
  },
  [types.LOGIN_REQUEST](state) {
    state.messages = []
  },
  [types.LOGOUT](state) {
    state.token = null
    state.username = null
  }
}

export default {
  state,
  actions,
  mutations
}
