import * as types from '../mutation-types'
import { user } from '../../api'
import router from '../../router'
import { errorHandler } from '../../utils'

// state
const state = {
  profile: null,
  messages: []
}

// actions
const actions = {
  register ({ commit, rootState }, data) {
    user.register(data, (err, res) => {
      // error handle todo
      if (err) {
        console.log(err)
        commit(types.LOGIN_FAILED, errorHandler('error'))
      }
      if ('id' in res.body) {
        commit(types.REGISTER_SUCCESS, res.body)
        // Success: enter login page
        router.push({ name: 'login' })
      } else {
        // Fail: return fail message
        commit(types.REGISTER_FAILED, errorHandler(res.body))
      }
    })
  },
  getProfile ({ commit, rootState }) {
    console.log('getProfile', rootState)
  }

}

const mutations = {
  [types.REGISTER_REQUEST] (state) {
    state.messages = []
  },
  [types.REGISTER_SUCCESS] (state, profile) {
    state.profile = profile
  },
  [types.REGISTER_FAILED] (state, messages) {
    state.messages = messages
  }
}

export default {
  state,
  actions,
  mutations
}
