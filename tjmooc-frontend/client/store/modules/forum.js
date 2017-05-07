import * as types from '../mutation-types'
import { forum } from '../../api'
import { errorHandler } from '../../utils'

// state
const state = {
  forumPage: {
    current: 1,
    next: null
  },
  postPage: {
    current: 1,
    next: null
  },
  forums: [],
  posts: [],
  messages: null
}

// actions
const actions = {
  getForumList ({ commit }, page = state.forumPage.current) {
    forum.getForumList({ page }, (err, res) => {
      // error handle
      if (err) {
        commit(types.FETCH_FAILED, errorHandler('error'))
      }
      commit(types.FORUM_FETCH_SUCCESS, { forums: res.body.results, next: res.body.next, current: page })
    })
  },
  getPostList ({ commit }, forumId, page = state.postPage.current) {
    forum.getPostList({ page, forumId }, (err, res) => {
      // error handle
      if (err) {
        commit(types.FETCH_FAILED, errorHandler('error'))
      }
      commit(types.POSTS_FETCH_SUCCESS, { posts: res.body.results, next: res.body.next, current: page })
    })
  }
  // todo: getPostDetail
}

const mutations = {
  [types.FORUM_FETCH_SUCCESS] (state, { forums, next, current }) {
    state.forums = forums
    state.forumPage.next = next !== null
    state.forumPage.current = current
  },
  [types.POSTS_FETCH_SUCCESS] (state, { posts, next, current }) {
    state.posts = posts
    state.postPage.next = next !== null
    state.postPage.current = current
  },
  [types.FETCH_FAILED] (state, messages) {
    state.messages = messages
  }
}

export default {
  state,
  actions,
  mutations
}
