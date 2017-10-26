import { translation } from '../config'

function find (list, f) {
  return list.filter(f)[0]
}

function eng2zh (value) {
  if (value in translation) {
    return translation[value]
  } else {
    return value
  }
}

// Format error object:
// {
//   "field1": [
//     "error1",
//     "error2"
//   ],
//   "field2": [
//     "error1",
//     "error2"
//   ]
// }
// to:
// ["field1(zh): error1(zh).", "field1(zh): error2(zh)" ...]
export function errorHandler (obj) {
  const messages = []
  if (obj instanceof Object) {
    Object.keys(obj).map((key) => {
      let field = eng2zh(key)
      const value = eng2zh(obj[key])
      if (field.length > 0) field += ':'
      messages.push(`${field} ${value}`)
    })
  } else if (typeof (obj) === 'string') {
    messages.push(eng2zh(obj))
  }
  return messages
}

export function deepCopy (obj, cache = []) {
  // just return if obj is immutable value
  if (obj === null || typeof obj !== 'object') {
    return obj
  }

  // if obj is hit, it is in circular structure
  const hit = find(cache, c => c.original === obj)
  if (hit) {
    return hit.copy
  }

  const copy = Array.isArray(obj) ? [] : {}
  // put the copy into cache at first
  // because we want to refer it in recursive deepCopy
  cache.push({
    original: obj,
    copy
  })

  Object.keys(obj).forEach(key => {
    copy[key] = deepCopy(obj[key], cache)
  })

  return copy
}
