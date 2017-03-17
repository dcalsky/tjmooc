<template>
  <div class="slide">
    <div class="img">
      <div class="background" :style="{backgroundColor: dataNow('color')}"></div>
      <div class="descImg">
        <img :src="dataNow('imgUrl')" :alt="dataNow('title')">
      </div>

      <div class="text">
        <div class="detail">
          <div class="teacher">{{dataNow('teacher')}} 主讲</div>
          <div class="time">{{dataNow('time')}} 课时</div>
        </div>
        <h1>{{dataNow('title')}}</h1>
        <div class="btn" :style="{color: dataNow('color')}" @click="onEnterClicked">
          <div>进入课程</div>
        </div>
      </div>
    </div>
    <div class="tip-box">
      <div class="scroll">
        <div class="tip" v-for="(section, index) in sections" @click="onTipClicked(index)" :style="{opacity: index == displayNow ? 1 : 0.75}">
          <div class="color-bar" :style="{backgroundColor: section.color}" v-if="index == displayNow"></div>
          <h1>{{section.title}}</h1>
          <p>{{section.teacher}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  // import drop from 'lodash/fp/drop'
  // let _ = require('lodash');
  export default {
    name: "slide",
    data: function () {
      return {
        sections: [
          {
            title: '高等数学',
            desc: '由微积分学，较深入的代数学、几何学以及它们之间的交叉内容所形成的一门基础学科。',
            teacher: '南小鸟',
            time: 159,
            color: '#EEEEEE',
            imgUrl: '/slide/gdsx.jpg',
            courseId: '1',
          },
          {
            title: '线性代数',
            desc: '数学的一个分支，它的研究对象是向量，向量空间（或称线性空间），线性变换和有限维的线性方程组。',
            teacher: '东条希',
            time: 159,
            color: '#800080',
            imgUrl: '/slide/fbhs.jpg',
            courseId: 'xianxingdaishu',
          },
          {
            title: '概率论',
            desc: '概率论是研究随机现象数量规律的数学分支。',
            teacher: '星空凛',
            time: 155,
            color: '#FFFF00',
            imgUrl: '/slide/gll.jpg',
            courseId: 'gailvlun',
          },
          {
            title: '复变函数',
            desc: '以复数作为自变量和因变量的函数就叫做复变函数，而与之相关的理论就是复变函数论。',
            teacher: '矢泽妮可',
            time: 154,
            color: '#FFC0CB',
            imgUrl: '/slide/fbhs.jpg',
            courseId: 'fubianhanshu',
          },

        ],
        title: "同济慕课",
        timeoutFunc: null,
        displayNow: 3,
      }
    },
    computed: {
      dataNow: function () {
        let s = this.sections[this.displayNow];
        return function (key) {
          return s[key];
        }
      },
      desc: function () {
        let desc = this.sections[this.displayNow].desc;
        return desc;
      }
    },
    methods: {
      scrollTo: function (left, ms) {
          let box = document.getElementsByClassName('tip-box')[0], now;
          if (box) {
              now = box.scrollLeft;
            let frame = ms / 40, step = (left - now) / frame;
            for (let i = 0; i < frame; ++i) {
                setTimeout( function() {
                  box.scrollLeft += step;
                }, 40 * i);
            }
          }
      },
      startSlide: function () {
        if (this.timeoutFunc)
            clearTimeout(this.timeoutFunc);


        //let first = this.sections[0];
        //this.sections = _.drop(this.sections).concat(this.sections[0]);
        this.displayNow = (this.displayNow + 1) % this.sections.length;
        this.scrollTo(240 * this.displayNow, 600);

        let s = this.startSlide;
        this.timeoutFunc = setTimeout(function () {
            s();
          },
          5000
        )
      },
      onTipClicked: function (i) {
        if (this.timeoutFunc)
          clearTimeout(this.timeoutFunc);
        this.displayNow = i;
      },
      onEnterClicked: function (e) {
        if (this.timeoutFunc)
          clearTimeout(this.timeoutFunc);
        console.log(this.displayNow);
        window.r = this.$router;
        this.$router.push({ path: '/course/display/' + this.sections[this.displayNow].courseId })
      }
    },
    mounted: function () {
      this.startSlide();
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "slide.scss"
</style>
