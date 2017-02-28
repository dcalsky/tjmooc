import request from 'superagent'
import { server } from '../config'

function post(url, { data, cb }) {
  request
    .post(url)
    .set('Content-Type', 'application/json')
    .send(data)
    .end(cb)
}

function get(url, { query, cb }) {
  request
    .get(url)
    .query(query)
    .end(cb)
}

// Sessions
const session = {
  login(data, cb) {
    post(`${server.session}`, {
      data: data,
      cb: cb
    })
  }
}

// Users
const user = {
  register(data, cb) {
    post(`${server.user}`, {
      data: data,
      cb: cb
    })
  },
  changePassword(data, cb) {
    // todo
  }
}

// BBS
const forum = {
  ForumUrl: `${server.forum}`,
  PostUrl: `${server.post}`,
  getForumList(query, cb) {
    get(`${this.ForumUrl}`, {
      query: query,
      cb: cb
    })
  },
  getForumDetail(forumId, query, cb) {
    get(`${this.ForumUrl}/${forumId}`, {
      query: query,
      cb: cb
    })
  },
  getPostDetail(postId, cb) {
    get(`${this.PostUrl}/${postId}`, {
      query: query,
      cb: cb
    })
  }
}

export {
  session,
  user
}
