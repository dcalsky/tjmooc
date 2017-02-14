const server = {
  host: 'http://localhost:8000',
  session: '/sessions/',
  post: '/bbs/posts/',
  forum: '/bbs/forums/',
  user: '/users/'
}

const translation = {
  'non_field_errors': '',
  'Unable to login with provided credentials.': '账户密码错误',
  username: '学号',
  password: '密码',
  nickname: '姓名'
}

Object.keys(server).map((key) => {
  if (key !== 'host') {
    server[key] = server['host'] + server[key]
  }
})

export { server, translation }
