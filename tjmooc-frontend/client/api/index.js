import request from 'superagent'
import { server } from '../config'

function post(url, { data, cb, token}) {

  console.log(token)
  request
    .post(url)
    .set({
      'Content-Type': 'application/json',
      'Token': token ? `Bearer ${token}` : null
    })
    .send(data)
    .end(cb)
}

function get(url, {data, cb, token}) {
  request
    .get(url)
    .set({
      'Content-Type': 'application/json'
    })
    .send(data)
    .end(cb)
}

// Sessions
const session = {
  login(data, cb, token) {
    post(`${server.session}`, {
      data: data,
      cb: cb
    })
  }
}

// Users
const user = {
  register(data, cb, token) {
    post(`${server.user}`, {
      data: data,
      cb: cb
    })
  },
  changePassword(data, cb, token) {
    // todo
  }
}

// Course
const course = {
  getCourses(data, cb, token) {
    get(`${server.course}`, {
      data: data,
      cb: cb
    })
  },
  getCourseById(data, cb, token) {
    let courseId = data.courseId;
    get(`${server.course}${courseId}`, {
      cb: cb
    })
  },
  getChapters(data, cb, token) {
    let courseId = data.courseId;
    get(`${server.course}${courseId}/chapter?title=true&description=true&id=true`, {
      cb: cb
    })
  },
  getChapterById(data, cb, token) {
    let courseId = data.courseId, chapterId = data.chapterId;
    get(`${server.course}${courseId}/chapter/${chapterId}`, {
      cb: cb
    })
  },
  getUnits(data, cb, token) {
    let courseId = data.courseId, chapterId = data.chapterId;
    get(`${server.course}${courseId}/chapter/${chapterId}/unit`, {
      cb: cb
    })
  },
  getUnitById(data, cb, token) {
    let courseId = data.courseId, chapterId = data.chapterId, unitId = data.unitId;
    get(`${server.course}${courseId}/chapter/${chapterId}/unit/${unitId}`, {
      cb: cb
    })
  }
}

// material
const material = {
  getHomework(data, cb, token) {
    console.log(data)
    get(`${server.material}homework?course=${data.course}&chapter=${data.chapter}`, {
      cb: cb
    })
  },
  getHomeworkSubmit(data, cb, token) {
    console.log(data)
    get(`${server.material}homework/${data.chapter}/submit?user=${data.user}`, {
      cb: cb
    })
  },
  submitHomeworkFile(data, cb, token) {
    console.log(data, token);
    post(`${server.material}homework/${data.homeworkId}/submit`, {
      data: data.file,
      cb: cb,
      token: token
    })
  }
}

export {
  session,
  user,
  course,
  material
}
