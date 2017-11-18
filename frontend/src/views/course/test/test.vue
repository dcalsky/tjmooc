<template>
  <div id="course-test">
    <div class="left" :class="{center: !testStart && !testSubmitted}">

      <div class="box">
        <div class="count" v-if="testStart">
          <div class="info">
            剩余时间
            <span>{{formattedTimeRemain}}</span>
            <span>您还要回答</span>
          </div>
          <div class="date">
            <span class="val">
              {{infoNumber}}
            </span>
            <span class="unit">
              题
            </span>
          </div>
        </div>
        <div class="count" v-else>
          <div class="info">
            测试时间
            <span>{{formattedTimeRemain}}</span>
            <span>本次测试共</span>
          </div>
          <div class="date">
            <span class="val">
              {{infoNumber}}
            </span>
            <span class="unit">
              题
            </span>
          </div>
        </div>

        <divide :text="testSubmitted ? '测试已提交' : '测试未提交'"></divide>


        <div class="btn-box" v-if="testStart && testSubmitted">
          <span class="d">得分 {{testSubmit.score}}分</span>
        </div>
        <div class="btn-box" v-if="testStart && !testSubmitted">
          <span class="btn" @click="submitAnswer">提交答案</span>
        </div>

        <div class="btn-box" v-if="!testStart && testSubmitted">
          <span class="d">得分 {{testSubmit.score}}分</span>
        </div>
        <div class="btn-box" v-if="!testStart && !testSubmitted">
          <span class="btn" @click="startTest">开始测试</span>
        </div>
      </div>

    </div>
    <div class="right">
      <transition name="fade">
      <div v-if="testStart || testSubmitted">
          <div class="content question" v-for="q, i in questions">
            <div v-if="q.type === `select`">
              <div class="desc">{{q.desc}}</div>
              <el-radio-group v-model="answer[i]" :disabled="testSubmitted">
                <el-radio v-for="o, j in q.options" :label="j" :key="j">{{o}}</el-radio>
              </el-radio-group>
            </div>
            <div v-if="q.type === `check`">
              <div class="desc">{{q.desc}}</div>
              <el-checkbox-group v-model="answer[i]" :disabled="testSubmitted">
                <el-checkbox v-for="o, j in q.options" :label="j" :key="j">{{o}}</el-checkbox>
              </el-checkbox-group>
            </div>
            <div v-if="q.type === `blank`">
              <div class="desc">{{q.desc}}</div>
              <el-input size="mini" v-model="answer[i]" placeholder="请输入问题答案" :disabled="testSubmitted"></el-input>
            </div>
        </div>
      </div>
      </transition>
    </div>
  </div>
</template>

<script>
  import divide from '../../../components/divide/divide.vue'
  import search from '../../../components/search/search.vue'
  export default {
    name: 'course-test',
    components: {
      divide,
      search
    },
    data () {
      return {
        testStart: false,
        startTime: 0,
        timeRemain: 0,
        testTime: 0,
        countInterval: null,
        answer: []
      }
    },
    computed: {
      infoNumber () {
        if (!this.testStart) {
          return this.questions && this.questions.length
        } else {
          return this.answer && this.answer.filter(x => x === -1 || x === '' || x.length === 0).length
        }
      },
      test () {
        const test = this.$store.state.material.test
        const t = new Date(test['test_time'])
        this.timeRemain = this.testTime = t.getSeconds() + t.getMinutes() * 60 + t.getHours() * 3600
        return test
      },
      chapter () {
        return this.$store.state.course.chapter
      },
      questions () {
        return this.test.questions && this.test.questions.map(({right_answer, options, desc, score, type}) => ({
          type,
          score,
          desc,
          options: JSON.parse(options),
          // eslint-disable-next-line
          right_answer: JSON.parse(right_answer)
        }))
      },
      formattedTimeRemain () {
        let remain = this.timeRemain
        let res = ''
        const unit = [
          ['秒', 60],
          ['分', 60],
          ['时', 24],
          ['天', 7],
          ['周', 1]
        ]
        unit.forEach(x => {
          const t = remain % x[1]
          t && (res = t + x[0] + res)
          remain = parseInt(remain / x[1])
        })
        return res || '已用完'
      },
      testSubmit () {
        return this.$store.state.material.testSubmit
      },
      testSubmitted () {
        const b = Boolean(this.testSubmit && this.testSubmit.id)
        if (b) {
          const a = this.$store.state.material.testSubmit.answer
          // eslint-disable-next-line
          this.answer = eval(a.join('')).map(x => eval(x)) // FUCK U B-E
        }
        return b
      }
    },
    methods: {
      startTest () {
        this.$confirm(`即将开始测试。考试时间 ${this.formattedTimeRemain}`, '测试即将开始', {
          confirmButtonText: '确定',
          type: 'warning'
        }).then(() => {
          this.testStart = true
          this.startTime = new Date()
          const f = {
            'select': -1,
            'check': [],
            'blank': ''
          }
          this.answer = this.questions.map(({type}) => f[type])
          this.countInterval = setInterval(this.count, 1000)
        })
      },
      count () {
        const now = new Date()
        this.timeRemain = this.testTime - parseInt((now - this.startTime) / 1000)
        if (this.timeRemain <= 0) {
          this.submitAnswer()
        }
      },
      submitAnswer () {
        this.$alert('本次测试结束。', '测试结束', {
          confirmButtonText: '好的'
        })
        this.testStart = false
        this.timeRemain = this.testTime
        clearInterval(this.countInterval)
        const answer = this.answer.map(x => JSON.stringify(x.sort ? x.sort() : x))
        this.$store.dispatch('submitTest', {
          answer,
          test: this.test.id,
          user: this.$store.state.session.userId,
          chapterId: this.chapter.id
        })
      }
    },
    mounted () {
      this.$store.dispatch('getSubmits', this.chapter)
    }
  }
</script>

<!--<style lang="sass" rel="stylesheet/sass" scoped>-->
  <!--@import "test"-->
<!--</style>-->
