#Material

课程的Material分为Homework, Test, Video

##Homework

###获取作业列表
`GET /material/homework`

####Query
同时使用`course` 和 `chapter` 或者仅使用 `course`
   - `course` : course id 返回该课程下的作业
   - `chapter` : chapter id 返回该课程下的章节下的作业

####权限
   注册用户

####返回

```json
[
    {
        "id" : "",
        "title" : "",
        "introduction" : "",
        "problem_file" : "",
        "answer_file" : "",
        "deadline" : "",
        "chapter" : ""
    },
    
    ...
]
```
`200`

###添加作业
`POST /material/homework/`

####Query
同时使用`course` 和 `chapter`
   - `course` : course id
   - `chapter` : chapter id

####权限
该章节老师
####Body
- "title" : ""
- "introduction" : ""
- "problem_file" : ""
- "answer_file" : ""
- "deadline" : ""
- "chapter" : ""

####返回

```json
    {
        "id" : "",
        "title" : "",
        "introduction" : "",
        "problem_file" : "",
        "answer_file" : "",
        "deadline" : "",
        "chapter" : ""
    }
```

`201/404/403`

####错误代码
`404` ： 章节或课程ID不存在
`403` ： 无权限

###修改作业信息
`GET/PUT/DELETE /material/homework/<id>`

####Query
同时使用`course` 和 `chapter`
   - `course` : course id
   - `chapter` : chapter id

####权限
该章节老师
####Body
- "title" : ""
- "introduction" : ""
- "problem_file" : ""
- "answer_file" : ""
- "deadline" : ""
- "chapter" : ""

####返回

- PUT

    ```json
        {
            "id" : "",
            "title" : "",
            "introduction" : "",
            "problem_file" : "",
            "answer_file" : "",
            "deadline" : "",
            "chapter" : ""
        }
    ```
    `201/404/403`
- DELETE

    `202/404/403`

####错误代码
`404` ： 章节或课程ID不存在
`403` ： 无权限



###获取某次作业的提交
`GET /material/homwork/<id>/submit`
`GET /material/homwork/submit`

####Query
可选
   - `user` ： user id

分别实现查找某个课程下的某个章节下的作业提交，
某个用户的所有作业提交、某个用户在某个课程下的某个章节下的作业提交。
####权限
注册用户

####返回

```json
[
    {
        "id" : "",
        "homework_id" : "",
        "submit_user_id" : "",
        "judge_user_id" : "",
        "comment" : "",
        "score" : "",
        "submit_time" : "",
        "judge_time" : "",
        "submit_file" : ""
    },
    
    ...
]
```
`200`

####错误
`400'
`404` course或chapter或user不存在
`403` 无权限

###提交作业

`POST /material/homework/<id>/submit/`

####Query
无

####权限
注册用户
####Body

- "submit_user_id" : ""
- "submit_time" : ""
- "submit_file" : ""

####返回
```json
    {
        "id" : "",
        "homework_id" : "",
        "submit_user_id" : "",
        "judge_user_id" : "",
        "comment" : "",
        "score" : "",
        "submit_time" : "",
        "judge_time" : "",
        "submit_file" : ""
    }
```

`201/404/403`

####错误
`404` course或chapter或user或homework不存在
`403` 无权限



###修改作业信息

`GET/PUT/DELETE /material/homework/<hid>/submit/<sid>`

####权限
注册用户

####Body

- "id" : "",
- "homework_id" : "",
- "submit_user_id" : "",
- "judge_user_id" : "",
- "comment" : "",
- "score" : "",
- "submit_time" : "",
- "judge_time" : "",
- "submit_file" : ""

####返回
```json
    {
        "id" : "",
        "homework_id" : "",
        "submit_user_id" : "",
        "judge_user_id" : "",
        "comment" : "",
        "score" : "",
        "submit_time" : "",
        "judge_time" : "",
        "submit_file" : ""
    }
```

`202/201/404/403`

####错误
`404` course或chapter或user或homework不存在
`403` 无权限


##Test

###获取测验列表
`GET /material/test`

####Query
同时使用`course` 和 `chapter` 和 `unit`
   - `course` : course id 
   - `chapter` : chapter id
   - `unit` : unit id
####权限
   注册用户
####返回

```json
[
    {
        "id" : "",
        "title" : "",
        "introduction" : "",
        "answer" : "",
        "deadline" : "",
    },
    
    ...
]
```
`200`

####错误

`404` course chapter unit id 不正确

###添加测试
`POST /material/test/`

####Query
同时使用`course` 和 `chapter` 和 `unit`
   - `course` : course id
   - `chapter` : chapter id
   - `unit` : unit id

####权限
该章节老师
####Body
- "title" : ""
- "introduction" : ""
- "answer" : ""
- "deadline" : ""
- "unit" :""

####返回

```json
    {
        "id" : "",
        "title" : "",
        "introduction" : "",
        "answer" : "",
        "deadline" : "",
    }
```

`201/404/403`

####错误代码
`404` ： 章节或课程ID不存在
`403` ： 无权限
`400`

###修改测试信息
`GET/PUT/DELETE /material/test/<id>`

####Query
同时使用`course` 和 `chapter` 和 `unit`
   - `course` : course id
   - `chapter` : chapter id
   - `unit` : unit id


####权限
该章节老师
####Body
- "title" : ""
- "introduction" : ""
- "answer" : ""
- "deadline" : ""

####返回

- PUT

    ```json
        {
            "id" : "",
            "title" : "",
            "introduction" : "",
            "problem_file" : "",
            "answer_file" : "",
            "deadline" : "",
        }
    ```
    `201/404/403`
- DELETE

    `202/404/403`

####错误代码
`404` ： 章节或课程ID不存在
`403` ： 无权限



###获取某次测试的提交
`GET /material/test/<id>/submit`
`GET /material/test/submit`
####Query
同时使用`course` 和 `chapter` 和 `unit`
   - `course` : course id
   - `chapter` : chapter id
   - `unit` : unit id

可选
   - `user` ： user id

分别实现查找某个课程下的某个章节下的某个单元的测试提交，
某个用户的所有测试提交、某个用户在某个课程下的某个章节下的测试提交。
####权限
注册用户

####返回

```json
[
    {
        "id" : "",
        "test_id" : "",
        "submit_user_id" : "",
        "submit_time" : "",
        "submit" : "",
        "score" : "",
        
    },
    
    ...
]
```
`200`

####错误
`404` course或chapter unit 或user不存在
`403` 无权限

###提交测试

`POST /material/test/<id>/submit/`

####Query
无

####权限
注册用户
####Body

- “test_id" : ""
- "submit_user_id" : ""
- "submit_time" : ""
- "submit" : ""
- "score" : ""

####返回
```json
    {
        "id" : "",
        "test_id" : "",
        "submit_user_id" : "",
        "submit_time" : "",
        "submit" : "",
        "score" : "",
        
    }
```

`201/404/403`

####错误
`404` test不存在
`403` 无权限



###修改作业信息

`PUT/DELETE /material/test/<tid>/submit/<sid>`

####权限
注册用户

####Body

- “test_id" : ""
- "submit_user_id" : ""
- "submit_time" : ""
- "submit" : ""
- "score" : ""

####返回
```json
   {     "id" : "",
        "test_id" : "",
        "submit_user_id" : "",
        "submit_time" : "",
        "submit" : "",
        "score" : "",
    }
```

`201/404/403`

####错误
`404` test或submit不存在
`403` 无权限



##Video

###获取Video列表

`GET /material/video`

####Query

   - `user` user id

某个用户的所有Video。
####权限
   注册用户
####返回

```json
[
    {
        "id" : "",
        "title" : "",
        "description" : "",
        "upload_time" : "",
        "url" : "",
        "teacher" : "",
    },
    
    ...
]
```
`200`

####错误

`404` user id 不正确

###添加Video
`POST /material/video/`

####Query
同时使用`course` 和 `chapter` 和 `unit`
   - `course` : course id
   - `chapter` : chapter id
   - `unit` : unit id

####权限
该章节老师
####Body
- "title" : ""
- "description" : ""
- "url" : ""
- "teacher" : ""


####返回

```json
    {
        "id" : "",
        "title" : "",
        "description" : "",
        "upload_time" : "",
        "url" : "",
        "teacher" : "",
    }
```

`201/404/403`

####错误代码
`404` ： 章节或课程或单元不存在
`403` ： 无权限

###修改视频信息
`PUT/DELETE /material/video/<id>`

####Query
同时使用`course` 和 `chapter` 和 `unit`
   - `course` : course id
   - `chapter` : chapter id
   - `unit` : unit id


####权限
该章节老师
####Body
- "title" : ""
- "description" : ""
- "url" : ""
- "teacher" : ""


####返回

- PUT

    ```json
        {
        "id" : "",
        "title" : "",
        "description" : "",
        "upload_time" : "",
        "url" : "",
        "teacher" : "",
        }
    ```
    `201/404/403`
- DELETE

    `202/404/403`

####错误代码
`404` ： 章节或课程或单元或视频不存在
`403` ： 无权限



## 上传文件

  

`POST /material/upload`

文件key使用`file`

- 返回值：文件url