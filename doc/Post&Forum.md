
# 板块接口 /forums

## 板块列表

`GET /forums`

### 权限

所有用户

### Query String

- `page`：页码，可以省略，默认为`1`；若指定`page`，则返回`(page - 1) * 15`到`page * 15`个元素

### 成功响应

返回一个数组，数组成员与`Forum` model对应。

200

### 错误列表

- 无权限 403

## 添加课程

无法在前端添加，请通过django后台管理系统

### 权限

管理员


## 单一板块详细情况

`GET /forums/<id>`

### 权限

所有用户

### QueryString

无

### 成功响应

返回板块详细情况，与model对应。

200

### 错误列表

- ID不存在 404

## 板块修改

无法在前端添加，请通过django后台管理系统

### 权限

管理员




# 帖子接口 /posts

## 查询用户帖子

`GET /posts`

### 权限

登录的用户

### Query String

- `page`：页码，可以省略，默认为`1`；若指定`page`，则返回`(page - 1) * 15`到`page * 15`个元素
- `user_id`: 需要查询的用户id

### 成功响应

返回数组，数组成员与`Post` model对应。
200

### 错误列表

- 无此用户 404
- 没有权限 403

## 帖子列表

`GET /<forum_id>/posts`

### 权限

所有用户

### Query String

- `page`：页码，可以省略，默认为`1`；若指定`page`，则返回`(page - 1) * 15`到`page * 15`个元素

### 成功响应

返回一个数组，数组成员与`Post` model对应。

200

### 错误列表

- 无此板块 404

## 添加帖子（发帖）

`POST /posts`

### 权限

注册用户

### POST

- `title`：标题 (限制：字数6 - 50)
- `content`：内容（限制：不能为空）
- `user`：该用户uuid
- `parent`: 上一帖子id
- `forum`：对应板块id


### 成功响应

返回添加成功的数据，与`Post` model对应。

201

### 错误列表

- 无权限 403
- 数据不合法 400

## 帖子详细情况

`GET /posts/<id>`

### 权限

所有用户

### QueryString

无

### 成功响应

返回课程详细情况。其中章节返回一个数组，数组成员为单元ID。

200

### 错误列表

- ID不存在 404

## 帖子编辑

`PUT /posts/<id>`

### 权限

发帖人

### POST

- `title`：标题 (限制：字数6 - 50)
- `content`：内容（限制：不能为空）
- `forum`：对应板块id

### 成功响应

200

### 错误列表

- ID不存在 404
- 无权限 403
- 不合法 400

## 课程删除

`DELETE /posts/<id>`

### 权限

发帖人

### 成功响应

204

### 错误列表

- ID不存在 404
- 无权限 403
