import * as types from '../mutation-types'
import { manage } from '../../api'
import router from '../../router'
import { errorHandler } from '../../utils'
import {server} from '../../config'
import urlJoin from 'url-join'

// state
const state = {
  courses: [],
  course: {},
  chapters: [],
  chapter: {},
  units: [],
  unit: {},
  videos: [],
  assistants: [],

  homework: {},
}

// actions
const actions = {
  appendBlankCourse ({commit}) {
    commit('appendBlankCourse')
  },
  getAllCourses ({commit}) {
    manage.getAllCourses({}, (err, res) => {
      if (err) {
        console.error(err)
      }
      commit('getAllCourses', res.body)
    })
  },
  submitCourseForm ({commit}, {courseForm, cb}) {
    // console.log(courseForm)
    if (courseForm.id < 0) {
      manage.postCourse(courseForm, (err, res) => {
        if (err) {
          console.error(err)
        }
        // commit('submitCourseForm', res.body)
        console.log('postCourse', res.body)
        cb()
      })
    } else {
      manage.updateCourse(courseForm, (err, res) => {
        if (err) {
          console.error(err)
        }
        // commit('submitCourseForm', res.body)
        console.log('updateCourse', res.body)
        cb()
      })
    }
  },
  getCourse ({commit}, course) {
    // manage.getCourse(course, (err, res) => {
    //   if (err) {
    //     console.error(err)
    //   }
    //   commit('getCourse', res.body)
    // })
    // console.log(course)
    if (course.id >= 0) {
      actions.getAllChapters({commit}, course)
    }
    commit('getCourse', course)
  },
  removeCourse ({commit}, {course, cb}) {
    manage.removeCourse(course, (err, res) => {
      if (err) {
        console.error(err)
      }
      // commit('submitCourseForm', res.body)
      console.log('removeCourse', res.body)
      cb()
    })
  },


  appendBlankChapter ({commit}) {
    commit('appendBlankChapter')
  },
  getAllChapters ({commit}, {id}) {
    manage.getAllChapters({courseId: id}, (err, res) => {
      if (err) {
        console.error(err)
      }
      commit('getAllChapters', res.body)
    })
  },
  getChapter ({commit}, chapter) {
    if (chapter.id >= 0) {
      actions.getAllUnits({commit}, chapter)
    }
    commit('getChapter', chapter)
  },
  submitChapterForm ({commit}, {courseId, chapterForm, cb}) {
    // console.log(courseForm)
    if (chapterForm.id < 0) {
      manage.postChapter({courseId, data: chapterForm}, (err, res) => {
        if (err) {
          console.error(err)
        }
        // commit('submitCourseForm', res.body)
        console.log('postChapter', res.body)
        cb()
      })
    }
    else {
      manage.updateChapter({courseId, data: chapterForm}, (err, res) => {
        if (err) {
          console.error(err)
        }
        // commit('submitCourseForm', res.body)
        console.log('postChapter', res.body)
        cb()
      })
    }
  },
  removeChapter ({commit}, {courseId, chapterId, cb}) {
    manage.removeChapter({courseId, chapterId}, (err, res) => {
      if (err) {
        console.error(err)
      }
      // commit('submitCourseForm', res.body)
      console.log('removeChapter', res.body)
      cb()
    })
  },


  appendBlankUnit ({commit}) {
    commit('appendBlankUnit')
  },
  getAllUnits ({commit}, {id}) {
    manage.getAllUnits({courseId: state.course.id, chapterId: id}, (err, res) => {
      if (err) {
        console.error(err)
      }
      commit('getAllUnits', res.body)
    })
  },
  getUnit ({commit}, unit) {
    commit('getUnit', unit)
    if (unit.id >= 0) {
      // actions.getAllChapters({commit}, course)
      actions.getVideo({commit})
    }
  },
  submitUnitForm ({commit}, {courseId, chapterId, unitForm, cb}) {
    if (unitForm.id < 0) {
      manage.postUnit({courseId, chapterId, data: unitForm}, (err, res) => {
        if (err) {
          console.error(err)
        }
        // commit('submitCourseForm', res.body)
        console.log('postUnit', res.body)
        cb()
      })
    }
    else {
      manage.updateUnit({courseId, chapterId, data: unitForm}, (err, res) => {
        if (err) {
          console.error(err)
        }
        // commit('submitCourseForm', res.body)
        console.log('updateUnit', res.body)
        cb()
      })
    }
  },
  removeUnit ({commit}, {courseId, chapterId, unitId, cb}) {
    manage.removeUnit({courseId, chapterId, unitId}, (err, res) => {
      if (err) {
        console.error(err)
      }
      // commit('submitCourseForm', res.body)
      console.log('removeUnit', res.body)
      cb()
    })
  },


  getVideo ({commit}) {
    const courseId = state.course.id
    const chapterId = state.chapter.id
    const unitId = state.unit.id
    manage.getVideo({courseId, chapterId, unitId}, (err, res) => {
      commit('getVideo', res.body)
    })
  },
  addVideo ({commit}, {url, fileName, teacher}) {
    // const f = /(.+)\.(.+?)/i.exec(fileName)[1] // TODO: 扩展名flv, change later
    // console.log(url, f)
    const courseId = state.course.id
    const chapterId = state.chapter.id
    const unitId = state.unit.id
    const data = {
      title: fileName,
      description: fileName,
      url,
      teacher
    }
    manage.postVideo({courseId, chapterId, unitId, data}, (err, res) => {
      if (err) {
        console.error(err)
      }
      // commit('submitCourseForm', res.body)
      actions.getVideo({commit})
      console.log('addVideo', res.body)
    })
  },
  removeVideo({commit}, {fileName}) {
    const courseId = state.course.id
    const chapterId = state.chapter.id
    const unitId = state.unit.id
    console.log(state.videos)
    const videoId = state.videos.filter(x => x.name === fileName)[0].id
    manage.removeVideo({courseId, chapterId, unitId, videoId}, (err, res) => {
      if (err) {
        console.error(err)
      }
      // commit('submitCourseForm', res.body)
      actions.getVideo({commit})
      console.log('removeVideo', res.body)
    })
  }
  // updateUnitVideo ({commit}, {courseId, chapterId, unitId, fileList, cb}) {
  //   manage.updateUnitVideo({courseId, chapterId, unitId, })
  // }
}

const mutations = {
  appendBlankCourse(state) {
    state.courses.push({
      id: -1,
      title: '',
      subtitle: '',
      introduction: '',
      cover_image: ''
    })
  },
  appendBlankChapter(state) {
    state.chapters.push({
      id: -1,
      title: '',
      description: '',
    })
  },
  appendBlankUnit(state) {
    state.units.push({
      id: -1,
      title: '',
      description: '',
    })
  },

  getAllCourses(state, courses) {
    // TODO: 约束后端！只要这几个字段: id, title, subtitle, cover_image, introduction
    state.courses = courses.map(x => {
        let {id, title, subtitle, introduction, cover_image} = x
        cover_image = cover_image.startsWith('http') ? cover_image : urlJoin(server.host, 'media', cover_image)
        return {id, title, subtitle, introduction, cover_image}
      }
    )
  },
  getAllChapters(state, c) {
    state.chapters = c
  },
  getAllUnits(state, c) {
    state.units = c
  },

  getCourse(state, c) {
    state.course = Object.assign({}, state.course, c)
  },
  getChapter(state, c) {
    state.chapter = Object.assign({}, state.chapter, c)
  },
  getUnit(state, c) {
    state.unit = Object.assign({}, state.unit, c)
  },
  getVideo(state, c) {
    state.videos = c.map(x => ({
      name: x.title,
      id: x.id
    }))
  },

  clearCourse(state) {
    mutations.clearChapter(state)
    state.course = Object()
    state.chapters = []
  },
  clearChapter(state) {
    mutations.clearUnit(state)
    state.chapter = Object()
    state.units = []
  },
  clearUnit (state) {
    state.unit = Object()
    state.videos = []
  }
}

export default {
  state,
  actions,
  mutations
}
