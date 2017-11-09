<template>
  <div id="course-test">
    <div class="left" :class="{center: !testStart}">

      <div class="box">
        <div class="count" v-if="testStart">
          <div class="info">
            剩余时间
            <span>90 分钟</span>
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
            <span>90 分钟</span>
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
          <span class="d">测试不能重复提交</span>
        </div>
        <div class="btn-box" v-if="testStart && !testSubmitted">
          <span class="btn" @click="submitAnswer">提交答案</span>
        </div>

        <div class="btn-box" v-if="!testStart && testSubmitted">
          <span class="d">测试不能重复提交</span>
        </div>
        <div class="btn-box" v-if="!testStart && !testSubmitted">
          <span class="btn" @click="startTest">开始测试</span>
        </div>
      </div>

    </div>
    <div class="right">
      <transition name="fade">
      <div v-if="testStart">
          <div class="content question" v-for="q, i in questions">
            <div v-if="q.type === `select`">
              <div class="desc">{{q.desc}}</div>
              <el-radio-group v-model="answer[i]" :disabled="testSubmitted">
                <el-radio v-for="o, j in q.options" :label="j">{{o}}</el-radio>
              </el-radio-group>
            </div>
            <div v-if="q.type === `check`">
              <div class="desc">{{q.desc}}</div>
              <el-checkbox-group v-model="answer[i]" :disabled="testSubmitted">
                <el-checkbox v-for="o, j in q.options" :label="j">{{o}}</el-checkbox>
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
        testSubmitted: false,
        testStart: false,
        answer: []
      }
    },
    computed: {
      infoNumber () {
        if (!this.testStart) {
          return this.questions && this.questions.length
        } else {
          return this.answer && this.answer.filter(x => x === null || x === '' || x.length === 0).length
        }
      },
      test () {
        return this.$store.state.material.test
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
      }
    },
    methods: {
      startTest () {
        // this.testStart = true
        const f = {
          'select': null,
          'check': [],
          'blank': ''
        }
        this.answer = this.questions.map(({type}) => f[type])
        this.testStart = !this.testStart
      },
      submitAnswer () {
        this.testSubmitted = true
      }
    },
    mounted () {
    }
  }
</script>

<!--<style lang="sass" rel="stylesheet/sass" scoped>-->
  <!--@import "test"-->
<!--</style>-->
