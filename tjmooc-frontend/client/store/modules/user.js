import * as types from '../mutation-types'
import { user } from '../../api'
import router from '../../router'

// state
const state = {
  profile: null
}

// getters

// actions
const actions = {
  register ({ commit, rootState }, data) {
    user.register(data, (err, res) => {
      // error handle
      commit(types.REGISTER, res.body)
      // Success: enter login page
      router.push({ name: 'login' })
      // Fail: return fail message
      // todo
    })
  },
  getProfile ({ commit, rootState }) {
    console.log(rootState)
  }

}

const mutations = {
  [types.REGISTER] (state, profile) {
    state.profile = profile
  }
}

export default {
  state,
  actions,
  mutations
}
