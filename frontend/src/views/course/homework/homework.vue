<template>
  <div id="course-homework" v-if="homework.id">
    <div class="left">
      <div class="box">
        <div class="count">
          <div class="info" @mouseenter="dateInEnglish = !dateInEnglish" @mouseleave="dateInEnglish = !dateInEnglish">
            <span v-if="!timeRemain.past">距</span>
            <span v-if="timeRemain.past">逾</span>
            截止日
            <span>{{deadline | convertTime(dateInEnglish)}}</span>
            <span>{{deadline | showTime(dateInEnglish)}}</span>
          </div>
          <div class="date" :class="{past: timeRemain.past}">
            <span class="val">
              {{timeRemain.val}}
            </span>
            <span class="unit">
              {{timeRemain.unit}}
            </span>
          </div>
        </div>
        <divide :text="homeworkStatus"></divide>
        <div class="btn-box" v-if="homeworkSubmitted">
          <a class="btn" :href="homeworkSubmit.file" target="_self" download style="color: currentColor;">查看作业</a>
          <span class="d" v-if="!timeRemain.past">|</span>
          <a class="btn" v-if="!timeRemain.past" @click="cancelUpload" style="color: currentColor;">取消提交</a>
        </div>
        <div class="btn-box" v-if="!homeworkSubmitted">
          <label class="btn" v-if="!timeRemain.past" for="homework-submit">提交作业</label>
          <span class="d" v-if="timeRemain.past">作业逾期不能提交</span>
        </div>
      </div>

      <el-upload
        :action="uploadTo"
        hidden
        :on-success="onUploadSuccess">
        <el-button size="small" type="primary" id="homework-submit">点击上传</el-button>
      </el-upload>

      <!--<input hidden type="file" @change="submitFile" id="homework-submit">-->
    </div>
    <div class="right">
      <div class="header">
        <div class="title">
          <span class="first">{{homework.title && homework.title[0]}}</span><span>{{homework.title && homework.title.substring(1, homework.title.length)}}</span>
          <span class="section" hidden>{{chapterTitle}}</span>
        </div>
        <div class="btn-box">
          <a class="btn" :href="homework.file" target="_self" download>作业文件</a>
        </div>
      </div>
      <div class="content" id="homework-content">
        <div v-html="compiledMarkdown" ref="katex"></div>
      </div>
    </div>
  </div>
</template>

<script>
  //  import * as marked from 'marked'
  import divide from '../../../components/divide/divide.vue'
  import {server} from '../../../config/index'
  import urlJoin from 'url-join'

  export default {
    name: 'course-homework',
    components: {
      divide
    },
    data () {
      return {
        dateInEnglish: true,
        now: new Date(),
        katexRendered: false,
        uploadTo: server.upload
      }
    },
    //    directives: {
    //        katex(el, binding) {
    //          console.log(el, binding)
    //
    //        }
    //    },
    filters: {
      convertTime (t, e) {
        let
          monthName = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        let [y, m, d] = [t.getFullYear(), t.getMonth(), t.getDate()]
        if (e) {
          return `${monthName[m]} ${d}, ${y}`
        } else {
          return `${y}年${m}月${d}日`
        }
      },
      showTime (t, e) {
        if (e) {
          let [h, m, s] = [t.getHours(), t.getMinutes(), t.getSeconds()].map(i => {
            if (i < 10) {
              return '0' + i
            } else {
              return i
            }
          })
          return `${h}:${m}:${s}`
        } else {
          const [h, m, s] = [t.getHours(), t.getMinutes(), t.getSeconds()]
          let r = `${h}时`
          if (m) {
            r += `${h}分`
          }
          if (s) {
            r += `${s}秒`
          }
          return r
        }
      }
    },
    computed: {

      compiledMarkdown () {
        //        let
        //          text = this.homework.desc,
        //          html = marked(text, {sanitize: true})
        //        console.log('a')
        //        this.katexRendered = false
        //        return html
        return this.homework.desc
      },
      homework () {
        return this.$store.state.material.homework
      },
      deadline () {
        console.log(this.homework)
        return new Date(this.homework.deadline)
      },
      chapter () {
        return this.$store.state.course.chapter
      },
      homeworkSubmit () {
        return this.$store.state.material.homeworkSubmit
      },
      homeworkSubmitted () {
        return Boolean(this.homeworkSubmit && this.homeworkSubmit.id)
      },
      timeRemain () {
        const now = this.now.getTime()
        const ddl = this.deadline.getTime()
        let remain = parseInt(Math.abs(ddl - now) / 1000)
        const past = ddl < now
        const unit = [
          ['秒', 60],
          ['分', 60],
          ['时', 24],
          ['天', 7],
          ['周', 1]
        ]
        let u = 0
        while (remain >= unit[u][1] && u < unit.length - 1) {
          remain = parseInt(remain / unit[u][1])
          ++u
        }

        return {
          val: remain,
          unit: unit[u][0],
          past
        }
      },
      homeworkStatus () {
        console.log(this.$store.state.session)
        if (this.homeworkSubmitted) {
          return '作业已提交'
        } else {
          return '作业未提交'
        }
      },
      chapterTitle () {
        return this.chapter.title
      }
    },
    methods: {
      onUploadSuccess (res, file, fileList) {
        const t = res.startsWith('http') ? res : urlJoin(server.host, res)
        this.$store.dispatch('submitHomeworkFile', {
          file: t,
          homework: this.homework.id,
          user: this.$store.state.session.userId,
          chapterId: this.chapter.id
        })
      },
      cancelUpload () {
        console.log(this.homeworkSubmit)
        if (this.homeworkSubmit && this.homeworkSubmit.id) {
          this.$store.dispatch('removeHomeworkSubmit', {
            id: this.homeworkSubmit.id,
            chapterId: this.chapter.id
          })
        }
      },
      refreshTime () {
        this.now = new Date()
        setTimeout(this.refreshTime, 500)
      }
      //      submitFile(e) {
      //        let f = e.target.files[0]
      //        console.log(f)
      //        let data = {
      //          submit_user_id: this.$store.state.session.userId,
      //          submit_time: new Date(),
      //          file: f
      //        }
      //
      //        this.$store.dispatch('submitHomeworkFile', {file: f, homeworkId: this.homework.id})
      //      }
    },
    mounted () {
      this.refreshTime()
      this.$store.dispatch('getSubmits', this.chapter)
    }
  }
</script>

