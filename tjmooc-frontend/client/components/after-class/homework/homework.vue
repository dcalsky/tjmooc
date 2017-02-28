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
          <span class="btn">查看作业</span>
          <span class="d">|</span>
          <span class="btn">重新提交</span>
        </div>
        <div class="btn-box" v-if="!homeworkSubmitted">
          <span class="btn">提交作业</span>
        </div>
      </div>
    </div>
    <div class="right">
      <div class="header">
        <div class="title">
          <span class="first">{{homework.title[0]}}</span><span>{{homework.title.substring(1, homework.title.length)}}</span>
          <div class="section">{{homework.chapter}}</div>
        </div>
        <div class="btn-box">
          <span class="btn">作业文件</span>
          <span class="d">|</span>
          <span class="btn">参考答案</span>
        </div>
      </div>
      <div class="content">
        <p>{{homework.introduction.replace(/\n/g, '\n\n')}}</p>
      </div>
    </div>
  </div>
</template>

<script>
  import divide from "../../divide/divide.vue"
  export default {
    name: "homework",
    components: {
        divide
    },
    data() {
        return {
          homeworkSubmitted: true,
          dateInEnglish: true,
          homework: {
            id: "1",
            title: "寻找质因数",
            introduction: "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. \nNow we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. \nBut, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth. ",
            problem_file: "pf",
            answer_file: "af",
            deadline: new Date(2017, 1, 27, 11, 27),
            chapter: "第一章"
          },
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
      }
    },
    computed: {
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
        if (this.homeworkSubmitted)
          return "作业已提交";
        else
          return "作业未提交";
      }
    },
    methods: {
        refreshTime() {
            this.now = new Date();
            setTimeout(this.refreshTime, 500);
        }
    },
    mounted() {
        this.refreshTime();
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "homework"
</style>
