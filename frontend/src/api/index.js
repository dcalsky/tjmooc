import request from 'superagent'
import { server } from '../config'

function post (url, { data, cb, token }) {
  request
    .post(url)
    .set({
      'Content-Type': 'application/json',
      'Authorization': localStorage.getItem('token') && `Bearer ${localStorage.getItem('token')}`
    })
    .send(data)
    .end(cb)
}

function put (url, { data, cb, token }) {
  request('put', url)
    .set({
      'Content-Type': 'application/json',
      'Authorization': localStorage.getItem('token') && `Bearer ${localStorage.getItem('token')}`
    })
    .send(data)
    .end(cb)
}

function delet (url, { data, cb, token }) {
  request('delete', url)
    .set({
      'Content-Type': 'application/json',
      'Authorization': localStorage.getItem('token') && `Bearer ${localStorage.getItem('token')}`
    })
    .query(data)
    .end(cb)
}

function get (url, { cb, token, page = 1 }) {
  console.log('page', page)
  request
    .get(url)
    .set({
      'Content-Type': 'application/json',
      'Authorization': localStorage.getItem('token') && `Bearer ${localStorage.getItem('token')}`
    })
    .query(page >= 0 ? { page } : {})
    .end(cb)
}

// Sessions
const session = {
  login (data, cb, token) {
    post(`${server.session}`, {
      data, cb
    })
  }
}

// Users
const user = {
  register (data, cb, token) {
    post(`${server.user}`, {
      data, cb
    })
  },
  changePassword (data, cb, token) {
    // todo
  }
}

// Course
const course = {
  getTops (cb) {
    get(`${server.course}course/top/`, {
      cb
    })
  },
  getCourses (page, cb, token) {
    get(`${server.course}course`, {
      page, cb
    })
  },
  getCourseById ({id}, cb) {
    get(`${server.course}course/${id}`, {cb})
  },
  getChapters (data, cb, token) {
    const courseId = data.courseId
    get(`${server.course}${courseId}/chapter?title=true&description=true&id=true&units=true`, {
      cb
    })
  },
  getChapterById ({id}, cb) {
    get(`${server.course}chapter/${id}`, {cb})
  },
  getUnits (data, cb, token) {
    const courseId = data.courseId
    const chapterId = data.chapterId
    get(`${server.course}${courseId}/chapter/${chapterId}/unit`, {
      cb
    })
  },
  getVideos (data, cb, token) {
    console.log(data)
    const {courseId, chapterId, unitId} = data
    // get(`${server.course}${courseId}/chapter/${chapterId}/unit/${unitId}/video`, {
    get(`${server.material}video?course=${courseId}&chapter=${chapterId}&unit=${unitId}`, {
      page: -1,
      cb
    })
  },
  getUnitById ({id}, cb, token) {
    get(`${server.course}unit/${id}`, {cb})
  }
}

// material
const material = {
  getHomework ({id}, cb, token) {
    get(`${server.material}homework/${id}`, {
      cb
    })
  },
  getTest ({id}, cb, token) {
    get(`${server.material}test/${id}`, {
      cb
    })
  },
  getHomeworkSubmit (data, cb, token) {
    console.log(data)
    get(`${server.material}homework/${data.chapter}/submit?user=${data.user}`, {
      cb
    })
  },
  submitHomeworkFile ({file, homework}, cb) {
    console.log(file)
    post(`${server.material}homework/${homework}/submit`, {
      data: {file},
      cb
    })
  },
  getVideo (data, cb, token) {
    console.log(data)
    get(`${server.material}video/${data.videoId}`, {
      cb
    })
  }
}

// Forum
const forum = {
  getForumList ({page}, cb) {
    get(`${server.forum}`, {cb, page})
  },
  getPostList ({floorId, page}, cb) {
    get(`${server.floor}/${floorId}/posts/`, {cb, page})
  },
  getFloorList ({forumId, page}, cb) {
    get(`${server.forum}/${forumId}/floors/`, {cb, page})
  },
  getFloorDetail ({floorId}, cb) {
    get(`${server.floor}/${floorId}`, {cb})
  },
  addPost ({floorId, data}, cb) {
    post(`${server.floor}/${floorId}/posts/`, {cb, data})
  },
  addFloor ({forumId, data}, cb) {
    post(`${server.forum}/${forumId}/floors/`, {cb, data})
  }
}

// manage
const manage = {
  getAllCourses (data, cb) {
    get(`${server.course}course`, {cb})
  },
  getCourse (data, cb) {
    get(`${server.course}course/${data.id}`, {cb})
  },
  postCourse (data, cb) {
    post(`${server.course}course/`, {data, cb})
  },
  updateCourse (data, cb) {
    put(`${server.course}course/${data.id}/`, {data, cb})
  },
  removeCourse ({id}, cb) {
    delet(`${server.course}course/${id}`, {cb})
  },

  // getAllChapters ({courseId}, cb) {
  //   get(`${server.course}${courseId}/chapter?id&title&description`, {cb})
  // },
  getChapter (data, cb) {
    get(`${server.course}chapter/${data.id}`, {cb})
  },
  postChapter (data, cb) {
    post(`${server.course}chapter/`, {data, cb})
  },
  updateChapter (data, cb) {
    put(`${server.course}chapter/${data.id}/`, {data, cb})
  },
  removeChapter ({id}, cb) {
    delet(`${server.course}chapter/${id}/`, {cb})
  },

  // getAllUnits ({courseId, chapterId}, cb) {
  //   get(`${server.course}${courseId}/chapter/${chapterId}/unit?id&title&description`, {cb})
  // },
  getUnit (data, cb) {
    get(`${server.course}unit/${data.id}`, {cb})
  },
  postUnit (data, cb) {
    post(`${server.course}unit/`, {data, cb})
  },
  updateUnit (data, cb) {
    put(`${server.course}unit/${data.id}/`, {data, cb})
  },
  removeUnit ({id}, cb) {
    delet(`${server.course}unit/${id}/`, {cb})
  },

  getVideo ({courseId, chapterId, unitId}, cb) {
    get(`${server.material}video?course=${courseId}&chapter=${chapterId}&unit=${unitId}`, {cb})
  },
  postVideo ({courseId, chapterId, unitId, data}, cb) {
    post(`${server.material}video?course=${courseId}&chapter=${chapterId}&unit=${unitId}`, {data, cb})
  },
  removeVideo ({courseId, chapterId, unitId, videoId}, cb) {
    delet(`${server.material}video/${videoId}?course=${courseId}&chapter=${chapterId}&unit=${unitId}`, {cb})
  },

  postHomework (data, cb) {
    post(`${server.material}homework/`, {data, cb})
  },
  updateHomework (data, cb) {
    put(`${server.material}homework/${data.id}/`, {data, cb})
  },
  removeHomework ({id}, cb) {
    delet(`${server.material}homework/${id}/`, {cb})
  },

  postTest (data, cb) {
    post(`${server.material}test/`, {data, cb})
  },
  removeTest ({id}, cb) {
    delet(`${server.material}test/${id}`, {cb})
  },
  postQuestionList (data, cb) {
    post(`${server.material}question/list/`, {
      data,
      cb
    })
  }
}

export {
  session,
  user,
  material,
  course,
  manage,
  forum
}
