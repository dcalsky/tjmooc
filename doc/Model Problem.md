# Model Problem

| Attribute | Type |
| --------- | ---- |
| id        | id   |
| type      | text |
| question  | JSON |
| answer    | JSON |
| teacher   | user |

`type : "multiple choice", "blank filling", "subjective"  `

`problem : html `

`answer : html`

`subjective problem answer：a URL of answer file`

## API

- `GET /problems`

**Permission** Authenticated users

**Response** 

```json
{
  {
    "id" : "1",
    "type" : "multiple choice",
  	"question" : JSON,
    "answer" : "<不知道用什么>A</不知道用什么>",
    "teacher" uuid
  },
  {
    "id" : "1",
    "type" : "multiple choice",
  	"question" : JSON,
    "answer" : "http://tjmooc/file/最帅的人.pdf",
    "teacher" uuid
  },
}
```



- `GET/problems/<id>`

**Permission** Authenticated users

**Response** 

```json

{
    "id" : "1",
    "type" : "multiple choice",
  	"question" : JSON,
    "answer" : JSON,
    "teacher" uuid
}
```



- `POST /problems`

**Permission** teacher

**Post Body**

```json
{
    "type" : "multiple choice",
  	"question" : JSON,
    "answer" : JSON,
    "teacher" uuid
}
```

**Response** 

```json
{
    "id" : "1",
    "type" : "multiple choice",
  	"question" : JSON,
    "answer" : JSON,
    "teacher" uuid
}
```



- `PUT /problems/<id> ` 

**Permission** teacher

**Body**

```json
{
    "id" : "1",
    "type" : "multiple choice",
  	"question" : JSON,
    "answer" : JSON",
    "teacher" uuid
}
```

**Response** 

```json
{
    "id" : "1",
    "type" : "multiple choice",
  	"question" : JSON,
    "answer" : JSON,
    "teacher" uuid
}
```