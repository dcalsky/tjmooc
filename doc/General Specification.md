# MOOC Documentation

## General Specification

- 使用HTTP、GET、PUT、DELETE与POST
- GET有QueryString参数，POST还有POST参数
- 成功返回200，失败视情况返回 403/404/5xx
- 响应是JSON Token

### 失败时错误信息字段

- `detail`：错误提示
- `status`：HTTP错误代码

### 失败时的响应示例

```json
{
  'detail': '类型为{0}，ID为{1}的数据不存在。'
}
status: 400
```

