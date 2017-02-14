import request from 'superagent'
import { server } from '../config'

function post (url, { data, cb }) {
  request
  .post(url)
  .set('Content-Type', 'application/json')
  .send(data)
  .end(cb)
}

// Sessions
const session = {
  login (data, cb) {
    post(`${server.session}`, {
      data: data,
      cb: cb
    })
  }
}

// Users
const user = {
  register (data, cb) {
    post(`${server.user}`, {
      data: data,
      cb: cb
    })
  },
  changePassword (data, cb) {
    // todo
  }
}


export {
  session,
  user
}
