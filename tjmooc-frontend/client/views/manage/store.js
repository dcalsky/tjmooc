import Vue from 'Vue'
let i = 0
let j = 100
let k = 10000
let l = 1000000
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
        id: i++,
        title: x,
        subtitle: `一门非常有意思的${x}课`,
        img: 'http://element.eleme.io/static/hamburger.50e4091.png'
      }))],
      course: {},
      chapters: [],
      chapter: {

      },
      units: [],
      unit: {

      },
      videos: [],
      assistants: [],

      homework: {},

    }
  },
  watch: {
  },
  methods: {
    getHomework () {
      this.homework = Object.assign({}, this.homework, {
        introduction: '作业正文在这里',
        title: '作业标题是什么',
        deadline: new Date('2017-10-1 12:15'),

        submitted: new Array(10).fill(1).map((x, i) => ({
          id: 1552000 + i,
          name: '同学' + i,
          url: 'urlhere',
          time: new Date(i * 10000000000).toTimeString()
        })),
        unsubmit: new Array(11).fill(1).map((x, i) => ({
          id: 1253000 + i,
          name: '同学' + i
        })),
      })
    },


    getCourse (i) {
      let c = this.courses.filter(x => x.id === i)[0]

      console.log(i, c, this.courses)
      if (c) {
        this.course = Object.assign({}, c, {
            introduction: 'qwertyuiop',
            coverImage: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'
          }
        )
      }

      this.chapters = [
        ...[
          '等可能概型',
          '随机事件与概率',
          '矩阵',
          '行列式',
          '一元函数微分学',
          '极限和导数'
        ].map(x => ({
          id: j++,
          title: x,
          subtitle: `一章非常有意思的${x}章节`
        }))]
    },
    getChapter (i) {
      let c = this.chapters.filter(x => x.id === i)[0]

      if (c) {
        this.chapter = Object.assign({}, c, {
            introduction: 'poiuytrewq',
          }
        )
      }

      this.units = [
        ...[
          '古典概型的应用',
          '古典概型',
          '概率',
          '随机事件',
          '矩阵的计算',
          '矩阵的定义'
        ].map(x => ({
          id: l++,
          title: x,
          subtitle: `一节非常有意思的${x}节`
        }))]
    },
    getUnit (i) {
      let u = this.units.filter(x => x.id === i)[0]

      if (u) {
        this.unit = Object.assign({}, u, {
            introduction: 'sdfghjk',
          }
        )
      }

      this.videos = [
        ...[
          '一个视频',
          '两个视频',
          '又一个小视频',
          '不能说的视频',
          '刺激小视频'
        ].map(x => ({
          id: l++,
          name: x,
          subtitle: `一个非常有意思的${x}视频`
        }))]
    },

    clearChapter () {
    },
    appendChapter() {
      this.chapters.push({
        id: j++,
        title: '新一章' + j,
        subtitle: `一章非常有意思的新章`
      })
    },
    appendUnit() {
      this.units.push({
        id: k++,
        title: '新一节' + k,
        subtitle: `一节非常有意思的新节`
      })
    },

    appendAssistant (id) {
      this.assistants.push({
        id,
        name: id[0] + '个学生'
      })
    },
    removeAssistant(id) {
      let i = this.assistants.find(x => x.id === id)
      this.assistants.splice(i, 1)
    }

  }
})

export default vm
