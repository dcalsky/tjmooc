import * as types from '../mutation-types'
import { material } from '../../api'
// import router from '../../router'
import { errorHandler } from '../../utils'

// state
const state = {
  homework: {},
  test: {},
  homeworkSubmit: {},
  videos: {},
  videosLen: 0
}

// actions
const actions = {
  getHomework ({commit}, data) {
    commit(types.GET_HOMEWORK_REQUEST)
    if (data) {
      material.getHomework(data, (err, res) => {
        if (err) {
          commit(types.GET_HOMEWORK_FAILED, errorHandler('error'))
        }
        commit(types.GET_HOMEWORK_SUCCESS, res.body)
      })
    } else {
      commit(types.GET_HOMEWORK_SUCCESS, {
        file: '',
        title: '',
        desc: '',
        deadline: '',
        id: -1
      })
    }
  },
  getTest ({commit}, data) {
    commit(types.GET_TEST_REQUEST)
    console.log(data)
    if (data) {
      material.getTest(data, (err, res) => {
        if (err) {
          commit(types.GET_TEST_FAILED, errorHandler('error'))
        }
        commit(types.GET_TEST_SUCCESS, res.body)
      })
    } else {
      commit(types.GET_TEST_SUCCESS, {})
    }
  },
  getHomeworkSubmit ({commit}, data) {
    commit(types.GET_HOMEWORK_REQUEST)
    material.getHomeworkSubmit(data, (err, res) => {
      // error handle todo
      if (err) {
        console.log(err)
        commit(types.GET_HOMEWORK_SUBMIT_FAILED, errorHandler('error'))
      }
      if (res.body && res.body.length) {
        commit(types.GET_HOMEWORK_SUBMIT_SUCCESS, {homeworkSubmit: res.body[0]})
      } else {
        // Fail: return fail message
        commit(types.GET_HOMEWORK_SUBMIT_FAILED, errorHandler(res.body))
      }
    })
  },
  submitHomeworkFile ({commit}, data) {
    commit(types.POST_HOMEWORK_REQUEST)
    material.submitHomeworkFile(data, (err, res) => {
      if (err) {
        console.log(err)
        commit(types.POST_HOMEWORK_FAILED, errorHandler('error'))
      }
      if (res.body && res.body.length) {
        commit(types.POST_HOMEWORK_SUCCESS, {homeworkSubmit: res.body})
      } else {
        // Fail: return fail message
        commit(types.POST_HOMEWORK_FAILED, errorHandler(res.body))
      }
    })
  },
  getVideo ({commit}, data) {
    commit(types.GET_VIDEO_REQUEST)
    material.getVideo(data, (err, res) => {
      // error handle todo
      if (err) {
        console.log(err)
        commit(types.GET_VIDEO_FAILED, errorHandler('error'))
      }
      if (res.body) {
        commit(types.GET_VIDEO_SUCCESS, {
          video: res.body,
          courseId: data.courseId,
          chapterId: data.chapterId,
          unitId: data.unitId
        })
      } else {
        // Fail: return fail message
        commit(types.GET_VIDEO_FAILED, errorHandler(res.body))
      }
    })
  }
}

const mutations = {
  [types.GET_HOMEWORK_SUCCESS] (state, homework) {
    state.homework = homework
  },
  [types.GET_HOMEWORK_FAILED] (state, messages) {
    state.homework = {}
    state.messages = messages
  },
  [types.GET_HOMEWORK_REQUEST] (state) {
    state.messages = []
  },

  [types.GET_TEST_SUCCESS] (state, test) {
    state.test = test
  },
  [types.GET_TEST_FAILED] (state, messages) {
    state.test = {}
    state.messages = messages
  },
  [types.GET_TEST_REQUEST] (state) {
    state.messages = []
  },

  [types.GET_HOMEWORK_SUBMIT_SUCCESS] (state, {homeworkSubmit}) {
    state.homeworkSubmit = homeworkSubmit
  },
  [types.GET_HOMEWORK_SUBMIT_FAILED] (state, messages) {
    state.homeworkSubmit = {}
    state.messages = messages
  },
  [types.GET_HOMEWORK_SUBMIT_REQUEST] (state) {
    state.homeworkSubmit = {}
    state.messages = []
  },

  [types.POST_HOMEWORK_SUCCESS] (state, {homeworkSubmit}) {
    state.homeworkSubmit = homeworkSubmit
  },
  [types.POST_HOMEWORK_FAILED] (state, messages) {
    state.homeworkSubmit = {}
    state.messages = messages
  },
  [types.POST_HOMEWORK_REQUEST] (state) {
    state.homeworkSubmit = {}
    state.messages = []
  },

  [types.GET_VIDEO_SUCCESS] (state, {video, courseId, chapterId, unitId}) {
    state.video = video
    Object.assign(state.videos, {
      [`${courseId}-${chapterId}-${unitId}-${video.id}`]: video
    })
    state.videosLen = Object.keys(state.videos).length
  },
  [types.GET_VIDEO_FAILED] (state, messages) {
    state.video = {}
    state.messages = messages
  },
  [types.GET_VIDEO_REQUEST] (state) {
    state.messages = []
  }
}

export default {
  state,
  actions,
  mutations
}
