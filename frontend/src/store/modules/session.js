import * as types from '../mutation-types'
import { session } from '../../api'
import router from '../../router'
import { errorHandler } from '../../utils'

// state
const state = {
  token: window.localStorage.getItem('token'),
  username: window.localStorage.getItem('username'),
  userId: window.localStorage.getItem('userId'),
  id: window.localStorage.getItem('id'),
  messages: []
}

// actions
const actions = {
  login ({ commit }, data) {
    commit(types.LOGIN_REQUEST)
    session.login(data, (err, res) => {
      // error handle
      if (err) {
        commit(types.LOGIN_FAILED, errorHandler('error'))
      }
      console.log(res.body)
      if ('token' in res.body) {
        commit(types.LOGIN_SUCCESS, { user: res.body })
        // Set localStorage for session information
        window.localStorage.setItem('token', res.body.token)
        window.localStorage.setItem('id', res.body.user.username)
        window.localStorage.setItem('username', res.body.user.nickname)
        window.localStorage.setItem('userId', res.body.user.id)
        window.localStorage.setItem('email', res.body.user.email)
        // Success: enter profile page
        router.push({ name: 'home' })
      } else {
        // Fail: return fail message
        commit(types.LOGIN_FAILED, errorHandler(res.body))
      }
    })
  },
  logout ({ commit }) {
    commit(types.LOGOUT)
    // Clear localStorage
    window.localStorage.clear()
    // Return home page
    router.push({ name: 'home' })
  }
}

const mutations = {
  [types.LOGIN_SUCCESS] (state, { user }) {
    state.token = user.token
    state.id = user.user.username
    state.username = user.user.nickname
    state.userId = user.user.id
  },
  [types.LOGIN_FAILED] (state, messages) {
    state.messages = messages
  },
  [types.LOGIN_REQUEST] (state) {
    state.messages = []
  },
  [types.LOGOUT] (state) {
    state.token = null
    state.username = null
  }
}

export default {
  state,
  actions,
  mutations
}
