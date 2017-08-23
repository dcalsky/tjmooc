import request from 'superagent'
import { server } from '../config'

function post (url, { data, cb, token }) {
  request
    .post(url)
    .set({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${localStorage.getItem('token')}`
    })
    .send(data)
    .end(cb)
}

function get (url, { cb, token, page = 1 }) {
  request
    .get(url)
    .set({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${localStorage.getItem('token')}`
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
    get(`${server.course}${courseId}/chapter/${chapterId}/unit/${unitId}/video`, {
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
      cb
    })
  },

}

// Forum
const forum = {
  getForumList ({ page }, cb) {
    get(`${server.forum}`, { cb, page })
  },
  getPostList ({ floorId, page }, cb) {
    get(`${server.floor}/${floorId}/posts`, { cb, page })
  },
  getFloorList({forumId, page}, cb) {
    get(`${server.forum}/${forumId}/floors`, { cb, page })
  },
  getFloorDetail({floorId}, cb) {
    get(`${server.floor}/${floorId}`, { cb })
  },
  addPost({floorId, data}, cb) {
    post(`${server.floor}/${floorId}/posts/`, { cb, data })
  }
}

export {
  session,
  user,
  material,
  forum
}
