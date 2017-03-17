import * as types from '../mutation-types'
import { material } from '../../api'
import router from '../../router'
import { errorHandler } from '../../utils'

// state
const state = {
  homework: {
    "id": 0,
    "title": "",
    "introduction": "",
    "problem_file": "",
    "answer_file": "",
    "deadline": "",
    "chapter": 0
  },
  homeworkSubmit: {}
}

// actions
const actions = {
  getHomework({ commit }, data) {
    commit(types.GET_HOMEWORK_REQUEST)
    material.getHomework(data, (err, res) => {
      // error handle todo
      if (err) {
        console.log(err)
        commit(types.GET_HOMEWORK_FAILED, errorHandler('error'))
      }
      if (res.body && res.body.length) {
        commit(types.GET_HOMEWORK_SUCCESS, { homework: res.body[0] })
      } else {
        // Fail: return fail message
        commit(types.GET_HOMEWORK_FAILED, errorHandler(res.body))
      }
    })
  },
  getHomeworkSubmit({ commit }, data) {
    commit(types.GET_HOMEWORK_REQUEST)
    material.getHomeworkSubmit(data, (err, res) => {
      // error handle todo
      if (err) {
        console.log(err)
        commit(types.GET_HOMEWORK_SUBMIT_FAILED, errorHandler('error'))
      }
      if (res.body && res.body.length) {
        commit(types.GET_HOMEWORK_SUBMIT_SUCCESS, { homeworkSubmit: res.body[0] })
      } else {
        // Fail: return fail message
        commit(types.GET_HOMEWORK_SUBMIT_FAILED, errorHandler(res.body))
      }
    })
  },
  submitHomeworkFile({commit}, data, token) {
    commit(types.POST_HOMEWORK_REQUEST);
    console.log('shf', token);
    material.submitHomeworkFile(data, (err, res) => {
      if (err) {
        console.log(err)
        commit(types.POST_HOMEWORK_FAILED, errorHandler('error'))
      }
      if (res.body && res.body.length) {
        commit(types.POST_HOMEWORK_SUCCESS, { homeworkSubmit: res.body[0] })
      } else {
        // Fail: return fail message
        commit(types.POST_HOMEWORK_FAILED, errorHandler(res.body))
      }
    }, token)
  }
};

const mutations = {
  [types.GET_HOMEWORK_SUCCESS](state, { homework }) {
    state.homework = homework;
  },
  [types.GET_HOMEWORK_FAILED](state, messages) {
    state.homework = {};
    state.messages = messages;
  },
  [types.GET_HOMEWORK_REQUEST](state) {
    state.homework = {};
    state.messages = [];
  },

  [types.GET_HOMEWORK_SUBMIT_SUCCESS](state, { homeworkSubmit }) {
    state.homeworkSubmit = homeworkSubmit;
  },
  [types.GET_HOMEWORK_SUBMIT_FAILED](state, messages) {
    state.homeworkSubmit = {};
    state.messages = messages;
  },
  [types.GET_HOMEWORK_SUBMIT_REQUEST](state) {
    state.homeworkSubmit = {};
    state.messages = [];
  },

  [types.POST_HOMEWORK_SUCCESS](state, { homeworkSubmit }) {
    state.homeworkSubmit = homeworkSubmit;
  },
  [types.POST_HOMEWORK_FAILED](state, messages) {
    state.homeworkSubmit = {};
    state.messages = messages;
  },
  [types.POST_HOMEWORK_REQUEST](state) {
    state.homeworkSubmit = {};
    state.messages = [];
  },
}

export default {
  state,
  actions,
  mutations
}
