import * as types from '../mutation-types'
import { course } from '../../api'
// import router from '../../router'
import { errorHandler } from '../../utils'

// state
const state = {
  course: {
    id: 0,
    title: '',
    subtitle: '',
    introduction: '',
    cover_image: '',
    chapters: []
  },
  chapter: {
    id: 0,
    title: '',
    description: '',
    units: []
  },
  unit: {
    id: 0,
    title: '',
    description: '',
    videos: []
  },
  messages: [],

  tops: [],
  courses: [],
  count: 0
}

// actions
const actions = {
  getTops ({commit}, data) {
    course.getTops((err, res) => {
      if (err) {
        console.log(err)
      }
      console.log(res.body)
      commit('getTops', res.body)
    })
  },
  getCourses ({ commit }, page) {
    commit(types.GET_COURSES_REQUEST)
    course.getCourses(page, (err, res) => {
      // error handle todo
      if (err) {
        console.log(err)
        commit(types.GET_COURSES_FAILED, errorHandler('error'))
      }
      // console.log(res.body)
      if (res.body && 'results' in res.body) {
        console.log(res.body)
        commit(types.GET_COURSES_SUCCESS, res.body)
      } else {
        // Fail: return fail message
        commit(types.GET_COURSES_FAILED, errorHandler(res.body))
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
        commit(types.GET_COURSE_SUCCESS, res.body)
      } else {
        // Fail: return fail message
        commit(types.GET_COURSE_FAILED, errorHandler(res.body))
      }
    })
  },
  getChapterById ({ commit }, data) {
    commit(types.GET_CHAPTER_REQUEST)
    course.getChapterById(data, (err, res) => {
      // error handle todo
      if (err) {
        console.log(err)
        commit(types.GET_CHAPTER_FAILED, errorHandler('error'))
      }
      if (res.body && 'id' in res.body) {
        commit(types.GET_CHAPTER_SUCCESS, res.body)
      } else {
        // Fail: return fail message
        commit(types.GET_CHAPTER_FAILED, errorHandler(res.body))
      }
    })
  },
  getUnitById ({ commit }, data) {
    commit(types.GET_UNIT_REQUEST)
    course.getUnitById(data, (err, res) => {
      if (err) {
        console.log(err)
        commit(types.GET_UNIT_FAILED, errorHandler('error'))
      }
      if (res.body && 'id' in res.body) {
        commit(types.GET_UNIT_SUCCESS, res.body)
      } else {
        // Fail: return fail message
        commit(types.GET_UNIT_FAILED, errorHandler(res.body))
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
}

const mutations = {
  [types.GET_COURSE_SUCCESS] (state, course) {
    state.course = Object.assign({}, course)
  },
  [types.GET_COURSE_FAILED] (state, messages) {
    // state.course = {}
    state.messages = messages
  },
  [types.GET_COURSE_REQUEST] (state) {
    // state.course = {}
    state.messages = []
  },

  [types.GET_COURSES_SUCCESS] (state, {count, results}) {
    state.count = count
    state.courses = results
  },
  [types.GET_COURSES_FAILED] (state, messages) {
    // state.course = {}
    state.messages = messages
  },
  [types.GET_COURSES_REQUEST] (state) {
    // state.course = {}
    state.messages = []
  },

  [types.GET_CHAPTER_SUCCESS] (state, chapter) {
    state.chapter = Object.assign({}, chapter)
  },
  [types.GET_CHAPTER_FAILED] (state, messages) {
    state.chapter = {}
    state.messages = messages
  },
  [types.GET_CHAPTER_REQUEST] (state) {
    // state.course = {}
    state.messages = []
  },

  [types.GET_UNIT_SUCCESS] (state, unit) {
    state.unit = Object.assign({}, unit)
  },
  [types.GET_UNIT_FAILED] (state, messages) {
    state.unit = {}
    state.messages = messages
  },
  [types.GET_UNIT_REQUEST] (state) {
    // state.course = {}
    state.messages = []
  },

  [types.GET_VIDEOS_SUCCESS] (state, {commit, videos, courseId, chapterId, unitId}) {
    // state.video = video
    // Object.assign(state.videos, {
    //   [`${courseId}-${chapterId}-${unitId}-${video.id}`]: video
    // })
    videos.forEach(video => {
      // console.log(video)
      commit(types.GET_VIDEO_SUCCESS, {commit, video, courseId, chapterId, unitId})
    })
  },
  [types.GET_VIDEOS_FAILED] (state, messages) {
    // state.video = {}
    state.messages = messages
  },
  [types.GET_VIDEOS_REQUEST] (state) {
    state.messages = []
  },

  [types.GET_UNITS_SUCCESS] (state, {units, chapter}) {
    state.chapters.find(x => parseInt(x.id) === chapter).units = units
  },
  [types.GET_UNITS_FAILED] (state, messages) {
    state.messages = messages
  },
  [types.GET_UNITS_REQUEST] (state) {
    state.messages = []
  },

  getTops (state, tops) {
    state.tops = tops
  }

}

export default {
  state,
  actions,
  mutations
}
