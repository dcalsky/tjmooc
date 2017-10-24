const server = {
  // host: 'http://115.159.218.143:8000',
  // host: 'http://lisirrx.tpddns.cn',
  host: 'http://127.0.0.1:8000',
  session: '/sessions/',
  post: '/bbs/posts',
  floor: '/bbs/floors',
  forum: '/bbs/forums',
  user: '/users/',
  course: '/course/',
  material: '/material/',
  upload: '/material/upload/'
}

const translation = {
  'non_field_errors': '',
  'Unable to login with provided credentials.': '账户密码错误',
  username: '学号',
  password: '密码',
  nickname: '姓名',
  error: '与服务器通信错误'
}

Object.keys(server).map((key) => {
  if (key !== 'host') {
    server[key] = server['host'] + server[key]
  }
})

export { server, translation }
