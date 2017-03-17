<template>
  <div class="homework">
    <div class="left">
      <div class="box">
        <div class="count">
          <div class="ddl" @mouseenter="dateInEnglish = !dateInEnglish" @mouseleave="dateInEnglish = !dateInEnglish">
            <span v-if="!timeRemain.past">距</span>
            <span v-if="timeRemain.past">逾</span>
            截止日
            <span>{{homework.deadline | convertTime(dateInEnglish)}}</span>
            <span>{{homework.deadline | showTime(dateInEnglish)}}</span>
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
          <a class="btn" :href="homeworkSubmit.submit_file" target="_self">查看作业</a>
          <span class="d" v-if="!timeRemain.past">|</span>
          <label class="btn" v-if="!timeRemain.past" for="homework-submit">重新提交</label>
        </div>
        <div class="btn-box" v-if="!homeworkSubmitted">
          <label class="btn" v-if="!timeRemain.past" for="homework-submit">提交作业</label>
          <span class="d" v-if="timeRemain.past">作业逾期不能提交</span>
        </div>
      </div>

      <input hidden type="file" @change="submitFile" id="homework-submit">
    </div>
    <div class="right">
      <div class="header">
        <div class="title">
          <span class="first">{{homework.title[0]}}</span><span>{{homework.title.substring(1, homework.title.length)}}</span>
          <div class="section">{{homework.chapter}}</div>
        </div>
        <div class="btn-box">
          <a class="btn" :href="homework.problem_file" target="_self">作业文件</a>
          <span class="d">|</span>
          <a class="btn" :href="homework.answer_file" target="_self">参考答案</a>
        </div>
      </div>
      <div class="content mathjax" id="homework-content">
        <div v-html="compiledMarkdown"></div>
      </div>
    </div>
  </div>
</template>

<script>
  import * as marked from 'marked'
  import divide from "../../divide/divide.vue"
  export default {
    name: "homework",
    components: {
      divide
    },
    data() {
      return {
        dateInEnglish: true,
        now: new Date()
      }
    },
    filters: {
      convertTime(t, e) {
        let
          monthName = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        let [y, m, d] = [t.getFullYear(), t.getMonth(), t.getDate()];
        if (e)
          return `${monthName[m]} ${d}, ${y}`;
        else
          return `${y}年${m}月${d}日`;
      },
      showTime(t, e) {
        if (e) {
          let [h, m, s] = [t.getHours(), t.getMinutes(), t.getSeconds()].map(i => {
            if (i < 10)
              return "0" + i;
            else
              return i;
          });
          return `${h}:${m}:${s}`;
        }
        else {
          let
            [h, m, s] = [t.getHours(), t.getMinutes(), t.getSeconds()],
            r = `${h}时`;
          if (m)
            r += `${h}分`;
          if (s)
            r += `${s}秒`;
          return r;
        }
      },
    },
    computed: {
      compiledMarkdown() {
        let text = this.homework.introduction;
        return marked(text, {sanitize: true});
      },
      token() {
        return this.$store.state.session.token;
      },
      homework() {
        let
          course = this.$store.state.course,
          chapterId = course.chapterNow,
          chapter = course.chapters.filter(x => x.id && x.id === chapterId)[0];

        let
          homework = Object.assign({}, this.$store.state.material.homework);
//          homework.chapter = chapter.title;
        // TODO: 增加章节号
        homework.deadline = new Date(homework.deadline);
        return homework;
      },
      homeworkSubmit() {
        return this.$store.state.material.homeworkSubmit;
      },
      homeworkSubmitted() {
        return Boolean(this.homeworkSubmit.id);
      },
      timeRemain() {
        let
          now = this.now.getTime(),
          ddl = this.homework.deadline.getTime(),
          remain = parseInt(Math.abs(ddl - now) / 1000),
          past = ddl < now;
        let unit = [
          ['秒', 60],
          ['分', 60],
          ['时', 24],
          ['天', 7],
          ['周', 1],
        ], u = 0;
        while (remain >= unit[u][1] && u < unit.length - 1) {
          remain = parseInt(remain / unit[u][1]);
          ++u;
        }

        return {
          val: remain,
          unit: unit[u][0],
          past: past
        }
      },
      homeworkStatus() {

        console.log(this.$store.state.session);
        if (this.homeworkSubmitted)
          return "作业已提交";
        else
          return "作业未提交";
      },
      course() {
        return this.$route.params.courseId;
      },
      chapter() {
        let c = this.$store.state.course.chapterNow;
        console.log('homework-chapter', c);
        return c;
      },
    },
    methods: {
      refreshTime() {
        this.now = new Date();
        setTimeout(this.refreshTime, 500);
      },
      submitFile(e) {
        let f = e.target.files[0];
        console.log(f, this.token);
        let data = {
          submit_user_id: this.$store.state.session.userId,
          submit_time: new Date(),
          submit_file: f
        }

        this.$store.dispatch('submitHomeworkFile', {file: data, homeworkId: this.homework.id, token: this.token});
      }
    },
    mounted() {
      this.refreshTime();

      let mathId = document.getElementsByClassName("mathjax");

      if (MathJax) {
        MathJax.Hub.Config({
          tex2jax: {
            inlineMath: [['$', '$'], ["\\(", "\\)"]],
            displayMath: [['$$', '$$'], ["\\[", "\\]"]]
          }
        });
        MathJax.Hub.Queue(["Typeset", MathJax.Hub, mathId]);
      }
    },
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "homework"
</style>
