import request from 'superagent'
import { server } from '../config'

function post (url, { data, cb, token }) {
  request
    .post(url)
    .set({
      'Content-Type': 'application/json',
      'Token': token ? `Bearer ${token}` : null
    })
    .send(data)
    .end(cb)
}

function get (url, { cb, token, page = 1 }) {
  request
    .get(url)
    .set({
      'Content-Type': 'application/json'
    })
    .query({ page })
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
    get(`${server.course}${courseId}/chapter?title=true&description=true&id=true`, {
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
    get(`${server.material}homework?course=${data.course}&chapter=${data.chapter}`, {
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
  }
}

// Forum
const forum = {
  getForumList ({ page }, cb) {
    get(`${server.forum}`, { cb, page })
  },
  getPostList ({ forumId, page }, cb) {
    get(`${server.forum}/${forumId}/posts`, { cb, page })
  }
}

export {
  session,
  user,
  course,
  material,
  forum
}
