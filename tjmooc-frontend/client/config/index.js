const server = {
  host: 'http://localhost:8000',
  session: '/sessions/',
  post: '/bbs/posts/',
  forum: '/bbs/forums/',
  user: '/users/'
}

Object.keys(server).map((key) => {
  if (key !== 'host') {
    server[key] = server['host'] + server[key]
  }
})

export { server }
