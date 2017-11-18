// import * as types from '../mutation-types'
import { manage } from '../../api'
// import router from '../../router'
// import { errorHandler } from '../../utils'
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
  assistants: [],

  homework: {}
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
      commit('getAllCourses', res.body.results)
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
    // console.log(course)
    if (course.id >= 0) {
      manage.getCourse(course, (err, res) => {
        if (err) {
          console.error(err)
        }
        commit('getCourse', res.body)
      })
    } else {
      commit('getCourse', course)
    }
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
  // getAllChapters ({commit}, {id}) {
  //   manage.getAllChapters({courseId: id}, (err, res) => {
  //     if (err) {
  //       console.error(err)
  //     }
  //     commit('getAllChapters', res.body)
  //   })
  // },
  getChapter ({commit}, chapter) {
    // console.log(course)
    if (chapter.id >= 0) {
      manage.getChapter(chapter, (err, res) => {
        if (err) {
          console.error(err)
        }
        commit('getChapter', res.body)
      })
    } else {
      commit('getChapter', chapter)
    }
  },
  submitChapterForm ({commit}, {course, chapterForm, cb}) {
    const {title, description, id} = chapterForm
    if (chapterForm.id < 0) {
      manage.postChapter({course, title, description}, (err, res) => {
        if (err) {
          console.error(err)
        }
        // commit('submitCourseForm', res.body)
        console.log('postChapter', res.body)
        cb()
      })
    } else {
      manage.updateChapter({course, title, description, id}, (err, res) => {
        if (err) {
          console.error(err)
        }
        // commit('submitCourseForm', res.body)
        console.log('updateChapter', res.body)
        cb()
      })
    }
  },
  removeChapter ({commit}, {id, cb}) {
    manage.removeChapter({id}, (err, res) => {
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
  // getAllUnits ({commit}, {id}) {
  //   manage.getAllUnits({courseId: state.course.id, chapterId: id}, (err, res) => {
  //     if (err) {
  //       console.error(err)
  //     }
  //     commit('getAllUnits', res.body)
  //   })
  // },
  getUnit ({commit}, unit) {
    if (unit.id >= 0) {
      manage.getUnit(unit, (err, res) => {
        if (err) {
          console.error(err)
        }
        commit('getUnit', res.body)
      })
    } else {
      commit('getUnit', unit)
    }
    //
    //
    // commit('getUnit', unit)
    // if (unit.id >= 0) {
    //   // actions.getAllChapters({commit}, course)
    //   actions.getVideo({commit})
    // }
  },
  submitUnitForm ({commit}, {chapter, unitForm, cb}) {
    const {title, description, id} = unitForm
    if (unitForm.id < 0) {
      manage.postUnit({title, description, chapter}, (err, res) => {
        if (err) {
          console.error(err)
        }
        // commit('submitCourseForm', res.body)
        console.log('postUnit', res.body)
        cb()
      })
    } else {
      manage.updateUnit({title, description, chapter, id}, (err, res) => {
        if (err) {
          console.error(err)
        }
        // commit('submitCourseForm', res.body)
        console.log('updateUnit', res.body)
        cb()
      })
    }
  },
  removeUnit ({commit}, {id, cb}) {
    manage.removeUnit({id}, (err, res) => {
      if (err) {
        console.error(err)
      }
      // commit('submitCourseForm', res.body)
      console.log('removeUnit', res.body)
      cb()
    })
  },

  // getVideo ({commit}) {
  //   const courseId = state.course.id
  //   const chapterId = state.chapter.id
  //   const unitId = state.unit.id
  //   manage.getVideo({courseId, chapterId, unitId}, (err, res) => {
  //     if (err) {
  //       console.error(err)
  //     }
  //     commit('getVideo', res.body)
  //   })
  // },
  addVideo ({commit}, {url, fileName, teacher}) {
    // const f = /(.+)\.(.+?)/i.exec(fileName)[1] // TODO: 扩展名flv, change later
    // console.log(url, f)
    manage.postVideo({
      title: fileName,
      description: fileName,
      unit: state.unit.id,
      url,
      teacher
    }, (err, res) => {
      if (err) {
        console.error(err)
      }
      // commit('submitCourseForm', res.body)
      actions.getUnit({commit}, state.unit)
    })
  },
  removeVideo ({commit}, {id}) {
    manage.removeVideo({id}, (err, res) => {
      if (err) {
        console.error(err)
      }
      // commit('submitCourseForm', res.body)
      actions.getUnit({commit}, state.unit)
      console.log('removeVideo', res.body)
    })
  },

  submitHomeworkForm ({commit}, {homeworkForm, cb}) {
    // console.log(courseForm)
    if (homeworkForm.id >= 0) {
      manage.updateHomework(homeworkForm, (err, res) => {
        if (err) {
          console.error(err)
        }
        console.log('updateHomework', res.body)
        cb()
      })
    } else {
      manage.postHomework(homeworkForm, (err, res) => {
        if (err) {
          console.error(err)
        }
        // commit('submitCourseForm', res.body)
        console.log('postHomework', res.body)
        cb()
      })
    }
  },
  submitQuestionForm ({commit}, {questionForm, test, cb}) {
    console.log(questionForm, test)
    const questions = questionForm.map(
      ({right_answer, options, desc, score, type}) => {
        right_answer.sort && right_answer.sort()
        return {
          type,
          score,
          desc,
          options: options && JSON.stringify(options),
          // eslint-disable-next-line
          right_answer: right_answer && JSON.stringify(right_answer),
          test
        }
      })
    console.log(questions)
    manage.postQuestionList({questions}, (err, res) => {
      if (err) {
        console.error(err)
      }
      console.log('postQuestionList', res.body)
      cb()
    })
  },
  submitTestForm ({commit}, {deadline, chapter, testTime, id, cb}) {
    if (id) {
      manage.updateTest({deadline, test_time: testTime, chapter, id}, (err, res) => {
        if (err) {
          console.error(err)

          const info = res.body
          let t = ''
          for (let i in info) {
            t = t + i + ': ' + info[i].join('; ') + '\n'
          }

          window.$app.$message.error(t)
          return
        }
        console.log('submitTestForm', res.body)
        cb(res.body)
      })
    } else {
      manage.postTest({deadline, test_time: testTime, chapter}, (err, res) => {
        if (err) {
          console.error(err)

          const info = res.body
          let t = ''
          for (let i in info) {
            t = t + i + ': ' + info[i].join('; ') + '\n'
          }

          window.$app.$message.error(t)
          return
        }
        console.log('submitTestForm', res.body)
        cb(res.body)
      })
    }
  },
  clearQuestions ({commit}, {id, cb}) {
    manage.clearQuestions({id}, (err, res) => {
      if (err) {
        console.error(err)
      }
      console.log('clearQuestions', res.body)
      cb()
    })
  },
  removeTest ({commit}, {id, cb}) {
    manage.removeTest({id}, (err, res) => {
      if (err) {
        console.error(err)
      }
      console.log('removeTest', res.body)
      cb()
    })
  },
  removeHomework ({commit}, {id, cb}) {
    manage.removeHomework({id}, (err, res) => {
      if (err) {
        console.error(err)
      }
      // commit('submitCourseForm', res.body)
      console.log('removeHomework', res.body)
      cb()
    })
  },
  appendAssistant ({commit}, data) {
    manage.appendAssistant(data, (err, res) => {
      if (err) {
        console.error(err)
      }
      console.log('appendAssistant', res.body)
      actions.getCourse({commit}, data.course)
    })
  },
  removeAssistant ({commit}, course) {
    manage.removeAssistant(course, (err, res) => {
      if (err) {
        console.error(err)
      }
      console.log('removeAssistant', res.body)
      actions.getCourse({commit}, course)
    })
  }
}

const mutations = {
  appendBlankCourse (state) {
    state.courses.push({
      id: -1,
      title: '',
      subtitle: '',
      introduction: '',
      cover_image: '',
      top: false
    })
  },
  appendBlankChapter (state) {
    state.chapters.push({
      id: -1,
      title: '',
      description: ''
    })
  },
  appendBlankUnit (state) {
    state.units.push({
      id: -1,
      title: '',
      description: ''
    })
  },

  getAllCourses (state, courses) {
    // TODO: 约束后端！只要这几个字段: id, title, subtitle, cover_image, introduction
    state.courses = courses.map && courses.map(x => {
      let {id, title, subtitle, introduction, cover_image: coverImage, top} = x
      coverImage = coverImage.startsWith('http') ? coverImage : urlJoin(server.host, 'media', coverImage)
      return {id, title, subtitle, introduction, cover_image: coverImage, top}
    })
  },
  getAllChapters (state, c) {
    state.chapters = c
  },
  getAllUnits (state, c) {
    state.units = c
  },

  getCourse (state, c) {
    state.course = Object.assign({}, state.course, c)
    state.chapters = c.chapters
  },
  getChapter (state, c) {
    state.chapter = Object.assign({}, state.chapter, c)
    state.units = c.units
  },
  getUnit (state, c) {
    state.unit = Object.assign({}, state.unit, c)
    // state.videos = c.lists
    // TODO: videos
  },
  // getVideo (state, c) {
  //   state.videos = c.map(x => ({
  //     name: x.title,
  //     id: x.id
  //   }))
  // },
  // getHomework (state, c) {
  //   state.homework = {}
  // },

  clearCourse (state) {
    mutations.clearChapter(state)
    state.course = Object()
    state.chapters = []
  },
  clearChapter (state) {
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
