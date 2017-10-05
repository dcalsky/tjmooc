<template>
  <div class="test">
    <div class="left">
      <div class="box">
        <div class="result" @mouseenter="onMouseenter" @mouseleave="onMouseleave" @click="onClick">
          <div class="info">
            本次测试共
            <span>{{test.length}} 题</span>
            <span v-if="testSubmitted">正确题目共</span>
            <span v-if="!testSubmitted && !resSide">您已经回答</span>
            <span v-if="!testSubmitted && resSide">您还要回答</span>
          </div>
          <div class="date" :class="{past: resSide}">
            <span class="val">
              {{infoNumber}}
            </span>
            <span class="unit">
              题
            </span>
          </div>
        </div>
        <divide :text="homeworkStatus"></divide>
        <div class="btn-box" v-if="testSubmitted">
          <span class="btn">重新提交</span>
        </div>
        <div class="btn-box" v-if="!testSubmitted">
          <span class="btn">提交答案</span>
        </div>
      </div>
    </div>
    <div class="right">
      <div class="subject" v-for="(t, i) in test">
        <div class="question">{{t.question}}</div>
        <div class="answer" v-if="t.type == 'blank'">
          <search v-model="test[i].answer" icon=""></search>
        </div>
        <div class="answer" v-if="t.type == 'select'">
          <div class="selection" v-for="(s, j) in t.options">
            <input type="radio" :id="`selection-${i}-${j}`" :value="s" v-model="test[i].answer">
            <label :for="`selection-${i}-${j}`">{{s}}</label>
          </div>
        </div>
        <div class="answer" v-if="t.type == 'check'">
          <div class="selection" v-for="(s, j) in t.options">
            <input type="checkbox" :id="`selection-${i}-${j}`" :value="s" v-model="test[i].answer">
            <label :for="`selection-${i}-${j}`">{{s}}</label>
          </div>
        </div>
      </div>
      <div class="info" v-if="info">
        {{info}}
      </div>
    </div>
  </div>
</template>

<script>
  import divide from "../../divide/divide.vue"
  import search from "../../search/search.vue"
  export default {
    name: "test",
    components: {
        divide,
      search
    },
    data() {
        return {
            test: [
              {
                type: "select",
                question: "1 + 1 = ？",
                options: ['2', '3', '不知道'],
                answer: ""
              },
              {
                type: "blank",
                question: "你已经超时几天啦？",
                answer: ""
              },
              {
                type: "check",
                question: "为什么我这么想喝酒？",
                options: ['高兴', '困', '夜深了', '不知道'],
                answer: []
              },
            ],
          testSubmitted: false,
          resSide: false,
          hoverChange: true
        }
    },
    computed: {
      info() {
        if (this.test.length == 0)
          return "暂无测试";
        else
            return "";
      },
      homeworkStatus() {
        if (this.homeworkSubmitted)
          return "答案已提交";
        else
          return "答案未提交";
      },
      answer() {
          let a = [];
          this.test.forEach(
            (e) => {
              let r;
              if (e.type == 'blank')
                r = e.answer;
              if (e.type == 'select') {
                r = e.options.findIndex(x => x === e.answer);
                r = r < 0 ? "" : `${r}`;
              }
              if (e.type == 'check') {
                r = e.answer.map(i => e.options.findIndex(x => x === i)).sort().join(',')
              }
              a.push(r);
            }
          );
          return a;
      },
      infoNumber() {
          if (this.testSubmitted) {
              return 3
          }
          else {
              let l = this.test.filter(t => t.answer && t.answer.length).length;
              if (this.resSide)
                  return this.test.length - l;
              else
                  return l;
          }
      }
    },
    methods: {
      onRemoveBtnClicked(i) {
          this.test[i].answer = "";
      },
      onMouseenter() {
        this.resSide = !this.resSide;
        this.hoverChange = true;
      },
      onMouseleave() {
        if (this.hoverChange)
            this.resSide = !this.resSide
      },
      onClick() {
        this.hoverChange = false;
      }
    },
    mounted() {
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass" scoped>
  @import "test"
</style>
