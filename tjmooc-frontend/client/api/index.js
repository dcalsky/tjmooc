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
  getCourses (data, cb, token) {
    get(`${server.course}`, {
      data, cb
    })
  },
  getCourseById (data, cb, token) {
    const courseId = data.courseId
    get(`${server.course}${courseId}`, {
      cb
    })
  },
  getChapters (data, cb, token) {
    const courseId = data.courseId
    get(`${server.course}${courseId}/chapter?title=true&description=true&id=true&units=true`, {
      cb
    })
  },
  getChapterById (data, cb, token) {
    const courseId = data.courseId
    const chapterId = data.chapterId
    get(`${server.course}${courseId}/chapter/${chapterId}`, {
      cb
    })
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
  getUnitById (data, cb, token) {
    const courseId = data.courseId
    const chapterId = data.chapterId
    const unitId = data.unitId
    get(`${server.course}${courseId}/chapter/${chapterId}/unit/${unitId}`, {
      cb
    })
  }
}

// material
const material = {
  getHomework (data, cb, token) {
    console.log(data)
    get(`${server.material}homework?course=${data.courseId}&chapter=${data.chapterId}`, {
      cb
    })
  },
  getHomeworkSubmit (data, cb, token) {
    console.log(data)
    get(`${server.material}homework/${data.chapter}/submit?user=${data.user}`, {
      cb
    })
  },
  submitHomeworkFile (data, cb, token) {
    post(`${server.material}homework/${data.homeworkId}/submit`, {
      data: data.file,
      cb,
      token
    })
  },
  getVideo (data, cb, token) {
    console.log(data)
    get(`${server.material}video/${data.videoId}`, {
      cb,
    })
  },

}

// Forum
const forum = {
  getForumList ({ page }, cb) {
    get(`${server.forum}`, { cb, page })
  },
  getPostList ({ floorId, page }, cb) {
    get(`${server.floor}/${floorId}/posts/`, { cb, page })
  },
  getFloorList({forumId, page}, cb) {
    get(`${server.forum}/${forumId}/floors/`, { cb, page })
  },
  getFloorDetail({floorId}, cb) {
    get(`${server.floor}/${floorId}`, { cb })
  },
  addPost({floorId, data}, cb) {
    post(`${server.floor}/${floorId}/posts/`, { cb, data })
  },
  addFloor({forumId, data}, cb) {
    post(`${server.forum}/${forumId}/floors/`, { cb, data })
  }
}

// manage
const manage = {
  getAllCourses ({}, cb) {
    get(`${server.course}?manage`, {cb})
  },
  getCourse (data, cb) {
    get(`${server.course}${data.id}`, {cb})
  },
  postCourse (data, cb) {
    post(`${server.course}`, {data, cb})
  },
  updateCourse (data, cb) {
    put(`${server.course}${data.id}`, {data, cb})
  },
  removeCourse (data, cb) {
    delet(`${server.course}${data.id}`, {cb})
  },

  getAllChapters ({courseId}, cb) {
    get(`${server.course}${courseId}/chapter?id&title&description`, {cb})
  },
  postChapter ({courseId, data}, cb) {
    post(`${server.course}${courseId}/chapter`, {data, cb})
  },
  updateChapter ({courseId, data}, cb) {
    put(`${server.course}${courseId}/chapter/${data.id}`, {data, cb})
  },
  removeChapter ({courseId, chapterId}, cb) {
    delet(`${server.course}${courseId}/chapter/${chapterId}`, {cb})
  },


  getAllUnits ({courseId, chapterId}, cb) {
    get(`${server.course}${courseId}/chapter/${chapterId}/unit?id&title&description`, {cb})
  },
  postUnit ({courseId, chapterId, data}, cb) {
    post(`${server.course}${courseId}/chapter/${chapterId}/unit`, {data, cb})
  },
  updateUnit ({courseId, chapterId, data}, cb) {
    put(`${server.course}${courseId}/chapter/${chapterId}/unit/${data.id}`, {data, cb})
  },
  removeUnit ({courseId, chapterId, unitId}, cb) {
    delet(`${server.course}${courseId}/chapter/${chapterId}/unit/${unitId}`, {cb})
  },


  getVideo ({courseId, chapterId, unitId}, cb) {
    get(`${server.material}video?course=${courseId}&chapter=${chapterId}&unit=${unitId}`, {cb})
  },
  postVideo ({courseId, chapterId, unitId, data}, cb) {
    post(`${server.material}video?course=${courseId}&chapter=${chapterId}&unit=${unitId}`, {data, cb})
  },
  removeVideo ({courseId, chapterId, unitId, videoId}, cb) {
    delet(`${server.material}video/${videoId}?course=${courseId}&chapter=${chapterId}&unit=${unitId}`, {cb})
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
