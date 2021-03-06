# 用户接口 /users

## 检查用户名是否已存在

`GET /users/<username>/check`

### Response

200 

{
    "message": "ok" or "existed"
}


## 用户列表

前端无法使用，请在django后台管理系统中查看。

## 获取个人信息

`GET /users/<username>`

### Header

基于JWT Token验证

请在Header中添加

key: `Authorization`
value: `Bearer <token>`
token从用户登录注册后的返回

### 成功响应

200

返回除password外的与User Model一致的用户个人信息

## 修改个人信息(除密码外)

`PATCH /users/<username>`

### Header

token

### PUT

- nickname
- mail

### 成功响应

204

### 失败响应

403 无权限
400 数据不合法

## 修改密码

`PUT /users/password`

### Header

token

### PUT

- old_password
- new_password

### 成功响应

204

### 失败响应

401 密码错误
403 无权限
400 新密码不符合要求
