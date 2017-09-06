import Vue from 'Vue'

const vm = new Vue({
  data () {
    return {
      courses: [...[
        '高等数学',
        '微积分',
        '大学物理',
        '编译原理',
        '数字控制',
        '视听说',
        '数据库',
        '操作系统',
        '面向对象程序设计',
        '金工实习'
      ].map(x => ({
        title: x,
        subtitle: `一门非常有意思的${x}课`
      }))],
      course: {
        title: '',
        subtitle: '',
        introduction: 'qwertyuiop',
        coverImage: ''
      },
      index: -1
    }
  },
  watch: {
    index (i) {
      this.course = Object.assign({}, this.course, this.courses[i])
    },
    'course.title' (val) {
      this.courses[this.index].title = val
    },
    'course.subtitle' (val) {
      this.courses[this.index].subtitle = val
    }
  },
  methods: {
    getCourse (i) {
      this.index = i
    },
    update (index, {title, subtitle}) {
      title && (this.course.title = title)
      subtitle && (this.course.subtitle = subtitle)
    }
  }
})

export default vm
