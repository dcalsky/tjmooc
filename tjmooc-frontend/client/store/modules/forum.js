import * as types from '../mutation-types'
import { forum } from '../../api'
import router from '../../router'
import { errorHandler } from '../../utils'

// state
const state = {
  forum_page: {
    current: 0,
    next: null,
  },
  post_page: {
    current: 0,
    next: null,
  },
  forums: [],
  posts: [],
  messages: null
}

// actions
const actions = {
  getForumList({ commit }, page = 1) {
    forum.getForumList({page}, (err, res) => {
      // error handle
      if (err) {
        commit(types.FETCH_FAILED, errorHandler('error'))
      }
      commit(types.FORUM_FETCH_SUCCESS, { forums: res.body.results, next: res.body.next, current: page })
    })
  },
  getForumDetail({ commit }, page = state.post_page ) {
    forum.getForumDetail({page}, (err, res) => {
      // error handle
      if (err) {
        commit(types.FETCH_FAILED, errorHandler('error'))
      }
      commit(types.POSTS_FETCH_SUCCESS, { posts: res.body.results, next: res.body.next, current: page  })
    })
  },
  // todo: getPostDetail
}

const mutations = {
  [types.FORUM_FETCH_SUCCESS](state, { forums, next, current }) {
    state.forums = forums
    state.forum_page.next = next !== null
    state.forum_page.current = current
  },
  [types.POSTS_FETCH_SUCCESS](state, { posts, next, current }) {
    state.posts = posts
    state.post_page.next = next !== null
    state.post_page.current = current
  },
  [types.FETCH_FAILED](state, messages) {
    state.messages = messages
  }
}

export default {
  state,
  actions,
  mutations
}
