# 接口文档

## 说明

前后端接口文档编写按照系统的角度编写。

除登录外的接口都在header中附加Token。

文档格式：

- `路径` 接口路径与method
- `参数` 说明提交的参数
- `返回` 说明返回值
- `错误列表` 可能出现的错误与错误HTTP状态码

返回范例：

```
{
    "info": "相关信息",
    "data": 数据json
}
Status code: 200
```

Status Code依据HTTP的规则设置。参考文档中的具体说明。



## 作业布置

路径：

`POST /<unit>/homework/`

参数：

- `title` 作业标题
- `introduction` 作业介绍
- `problem_file` 题目文件
- `answer_file` 答案文件
- `deadline` 

返回：

- 成功：

  ```javascript
  {
      homework added
  }
  Status code: 201
  ```

  ​

- 失败：

  ```javascript
  {
      "detail":error message
  }
  Status code: 403
  ```

  ​

错误列表：

- 无权限 403

## 作业信息

路径：

`GET/PUT /<unit>/homework/<homework_id> `

参数(`PUT`)：

- `title` 作业标题
- `introduction` 作业介绍
- `problem_file` 题目文件
- `answer_file` 答案文件
- `deadline` 

返回：

- 成功：

  - `GET`

    ```javascript
    {
       ···
    }
    Status code: 200
    ```


  - `PUT`

    ```javascript
    {
        homework updated
    }
    Status code: 201
    ```

    ​

- 失败：

  ```javascript
  {
      "detail":error message
  }
  Status code: 401/403
  ```

错误列表:

- 未登录 `401`
- 无权限 `403`



## 作业提交

路径：

`POST /<unit>/homework/<homeword_id>/`

参数：

- `submit_user_id`
- `submit_time`
- `submit_file`

返回:

- 成功：

  ```javascript
  {
      submit succeed
  }
  Status code: 201
  ```

- 失败：

  ```javascript
  {
      "datail":error messsage
  }
  Status code: 401
  ```

错误列表:

- 未登录 `401`
- 无权限 `403`



## 作业批改

路径：

`PUT /<unit>/homework/<homework_id>/<submit_id>`

参数：

- `judge_user_id` 批改人
- `score` 作业得分
- `judge_time`批改时间
- `comment` 评语

返回：

- 成功：

  ```javascript
  {
      judge succeed
  }
  Status code: 201
  ```

- 失败

  ```javascript
  {
      "detail":error message
  }
  Status code 401
  ```

错误列表：

- 未登录`401`





## 测试布置

路径：

`POST /<class>/test/`

参数：

- `title` 测试标题
- `introduction` 测试介绍
- `problem_file` 题目文件
- `answer_file` 答案文件
- `deadline` 

返回：

- 成功：

  ```javascript
  {
      test added
  }
  Status code: 201
  ```

  ​

- 失败：

  ```javascript
  {
      "detail":error message
  }
  Status code: 401/403
  ```

错误列表：

- 无权限 403
- 未登录 `401`

## 测试信息

路径：

`GET/PUT /<unit>/test/<test_id> `

参数(`PUT`)：

- `title` 测试标题
- `introduction` 测试介绍
- `problem_file` 题目文件
- `answer_file` 答案文件
- `deadline` 

返回：

- 成功：

  - `GET`

    ```javascript
    {
       ···
    }
    Status code: 200
    ```


  - `PUT`

    ```javascript
    {
        homework updated
    }
    Status code: 201
    ```

    ​

- 失败：

  ```javascript
  {
      "detail":error message
  }
  Status code: 401/403
  ```

错误列表:

- 未登录 `401`
- 无权限 `403`



## 测试提交

路径：

`POST /<unit>/test/<test_id>/`

参数：

- `submit_user_id`
- `submit_time`
- `submit_file`

返回:

- 成功：

  ```javascript
  {
      submit succeed
  }
  Status code: 201
  ```

- 失败：

  ```javascript
  {
      "datail":error messsage
  }
  Status code: 401
  ```

