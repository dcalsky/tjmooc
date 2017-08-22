import * as types from '../mutation-types'
import { forum } from '../../api'
import { errorHandler } from '../../utils'

// state
const state = {
  forumPage: {
    current: 1,
    next: null
  },
  floorPage: {
    current: 1,
    next: null
  },
  postPage: {
    current: 1,
    next: null
  },
  currentFloor: {},
  forums: [],
  floors: [],
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
  getPostDetail ({ commit }, floorId, page = state.postPage.current) {
    forum.getPostList({ page, floorId }, (err, res) => {
      // error handle
      if (err) {
        commit(types.FETCH_FAILED, errorHandler('error'))
      }
      console.log(res.body.results)
      commit(types.POST_FETCH_SUCCESS, { posts: res.body.results, next: res.body.next, current: page })
    })
  },
  getFloorList ({ commit }, forumId, page = state.postPage.current) {
    forum.getFloorList({ page, forumId }, (err, res) => {
      // error handle
      if (err) {
        commit(types.FETCH_FAILED, errorHandler('error'))
      }
      commit(types.FLOOR_FETCH_SUCCESS, { floors: res.body.results, next: res.body.next, current: page })
    })
  },
  getFloorDetail ({ commit }, floorId) {
    forum.getFloorDetail({ floorId }, (err, res) => {
      // error handle
      if (err) {
        commit(types.FETCH_FAILED, errorHandler('error'))
      }
      commit('FLOOR_DETAIL_FETCG_SUCCESS', { floor: res.body })
    })
  },

}

const mutations = {
  [types.FORUM_FETCH_SUCCESS] (state, { forums, next, current }) {
    state.forums = forums
    state.forumPage.next = next !== null
    state.forumPage.current = current
  },
  [types.POST_FETCH_SUCCESS] (state, { posts, next, current }) {
    console.log(posts)
    state.posts = posts
    state.postPage.next = next !== null
    state.postPage.current = current
  },
  [types.FLOOR_FETCH_SUCCESS] (state, { floors, next, current }) {
    state.floors = floors
    state.floorPage.next = next !== null
    state.floorPage.current = current
  },
  [types.FETCH_FAILED] (state, messages) {
    state.messages = messages
  },
  "FLOOR_DETAIL_FETCG_SUCCESS" (state, { floor }) {
    state.currentFloor = floor
  }
}

export default {
  state,
  actions,
  mutations
}
