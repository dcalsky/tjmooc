import * as types from '../mutation-types'
import { forum } from '../../api'
import router from '../../router'
import { errorHandler } from '../../utils'

// state
const state = {
  forum_page: 1,
  post_page: 1,
  forums: [],
  posts: [],
  messages: null
}

// actions
const actions = {
  getForumList({ commit }, page = state.forum_page) {
    forum.getForumList({page}, (err, res) => {
      // error handle
      if (err) {
        commit(types.FETCH_FAILED, errorHandler('error'))
      }
      commit(types.FORUM_FETCH_SUCCESS, { forums: res.body.results })
    })
  },
  getForumDetail({ commit }, page = state.post_page ) {
    forum.getForumDetail({page}, (err, res) => {
      // error handle
      if (err) {
        commit(types.FETCH_FAILED, errorHandler('error'))
      }
      commit(types.POSTS_FETCH_SUCCESS, { posts: res.body })
    })
  },
  // todo: getPostDetail
}

const mutations = {
  [types.FORUM_FETCH_SUCCESS](state, { forums }) {
    state.forums = forums
    state.forum_page ++
  },
  [types.POSTS_FETCH_SUCCESS](state, { posts }) {
    state.posts = posts
    state.post_page ++
  },
  [types.FETCH_FAILED](state, messages) {
    state.messages = messages
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
