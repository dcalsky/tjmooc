import * as types from '../mutation-types'
import { course } from '../../api'
import router from '../../router'
import { errorHandler } from '../../utils'

// state
const state = {
  course: {
    'id': 0,
    'title': '加载中',
    'subtitle': 'Loading...',
    'introduction': '加载中...',
    'cover_image': '',
    'update_time': '',
    'participants_count': 0,
    'obligator': ''
  },
  chapters: [],
  messages: []
}

// actions
const actions = {
  getCourses ({ commit }, data) {
    commit(types.GET_COURSE_REQUEST)
    course.getCourses(data, (err, res) => {
      // error handle todo
      if (err) {
        console.log(err)
        commit(types.GET_COURSE_FAILED, errorHandler('error'))
      }
      // console.log(res.body)
      if (res.body && 'results' in res.body) {
        const token = res.body.token
        commit(types.LOGIN_SUCCESS, { token: token, username: data.username })
        // Set localStorage for session information
        window.localStorage.setItem('token', token)
        window.localStorage.setItem('username', data.username)
        // Success: enter profile page
        router.push({ name: 'profile' })
      } else {
        // Fail: return fail message
        commit(types.GET_COURSE_FAILED, errorHandler(res.body))
      }
    })
  },
  getCourseById ({ commit }, data) {
    commit(types.GET_COURSE_REQUEST)
    course.getCourseById(data, (err, res) => {
      // error handle todo
      if (err) {
        console.log(err)
        commit(types.GET_COURSE_FAILED, errorHandler('error'))
      }
      if (res.body && 'id' in res.body) {
        commit(types.GET_COURSE_SUCCESS, { course: res.body })
      } else {
        // Fail: return fail message
        commit(types.GET_COURSE_FAILED, errorHandler(res.body))
      }
    })
  },
  getChapters ({ commit }, data) {
    commit(types.GET_CHAPTER_REQUEST)
    course.getChapters(data, (err, res) => {
      // error handle todo
      if (err) {
        console.log(err)
        commit(types.GET_CHAPTERS_FAILED, errorHandler('error'))
      }
      if (res.body) {
        commit(types.GET_CHAPTERS_SUCCESS, { chapters: res.body })
      } else {
        // Fail: return fail message
        commit(types.GET_CHAPTERS_FAILED, errorHandler(res.body))
      }
    })
  },
  getUnits ({ commit }, data) {
    commit(types.GET_UNITS_REQUEST)
    course.getUnits(data, (err, res) => {
      // error handle todo
      if (err) {
        console.log(err)
        commit(types.GET_UNITS_FAILED, errorHandler('error'))
      }
      if (res.body) {
        commit(types.GET_UNITS_SUCCESS, { units: res.body, chapter: data.chapterId })
      } else {
        // Fail: return fail message
        commit(types.GET_UNITS_FAILED, errorHandler(res.body))
      }
    })
  },
  getVideos ({ commit }, data) {
    commit(types.GET_VIDEOS_REQUEST)
    course.getVideos(data, (err, res) => {
      // error handle todo
      // console.log(data, res.body)
      if (err) {
        console.log(err)
        commit(types.GET_VIDEOS_FAILED, errorHandler('error'))
      }
      if (res.body) {
        commit(types.GET_VIDEOS_SUCCESS, { commit, videos: res.body, courseId: data.courseId, chapterId: data.chapterId, unitId: data.unitId })
      } else {
        // Fail: return fail message
        commit(types.GET_VIDEOS_FAILED, errorHandler(res.body))
      }
    })
  }
  // getChapterById({ commit }, data) {
  //   commit(types.GET_COURSE_REQUEST)
  //   course.getChapterById(data, (err, res) => {
  //     // error handle todo
  //     if (err) {
  //       console.log(err)
  //       commit(types.GET_COURSE_FAILED, errorHandler('error'))
  //     }
  //     if (res.body && 'id' in res.body) {
  //       commit(types.GET_COURSE_SUCCESS, { course: res.body })
  //     } else {
  //       // Fail: return fail message
  //       commit(types.GET_COURSE_FAILED, errorHandler(res.body))
  //     }
  //   })
  // },
}

const mutations = {
  [types.GET_COURSE_SUCCESS] (state, { course }) {
    state.course = course
  },
  [types.GET_COURSE_FAILED] (state, messages) {
    // state.course = {};
    state.messages = messages
  },
  [types.GET_COURSE_REQUEST] (state) {
    // state.course = {};
    state.messages = []
  },

  [types.GET_CHAPTERS_SUCCESS] (state, { chapters }) {
    state.chapters = chapters
  },
  [types.GET_CHAPTERS_FAILED] (state, messages) {
    state.course = {}
    state.messages = messages
  },
  [types.GET_CHAPTERS_REQUEST] (state) {
    state.course = {}
    state.messages = []
  },

  [types.GET_VIDEOS_SUCCESS](state, {commit, videos, courseId, chapterId, unitId }) {
    // state.video = video;
    // Object.assign(state.videos, {
    //   [`${courseId}-${chapterId}-${unitId}-${video.id}`]: video
    // })
    videos.forEach(video => {
      // console.log(video)
      commit(types.GET_VIDEO_SUCCESS, { commit, video, courseId, chapterId, unitId})
    })
  },
  [types.GET_VIDEOS_FAILED](state, messages) {
    // state.video = {};
    state.messages = messages;
  },
  [types.GET_VIDEOS_REQUEST](state) {
    state.messages = [];
  },

  [types.GET_UNITS_SUCCESS] (state, { units, chapter }) {
    state.chapters.find(x => x.id == chapter).units = units;
  },
  [types.GET_UNITS_FAILED] (state, messages) {
    state.messages = messages
  },
  [types.GET_UNITS_REQUEST] (state) {
    state.messages = []
  },

}

export default {
  state,
  actions,
  mutations
}
