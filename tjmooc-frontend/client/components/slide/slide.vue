<template>
  <div class="slide" ref="slide">
    <!--<div class="img">-->
      <!--<div class="background"></div>-->
      <!--<div class="descImg">-->
        <!--<img :src="dataNow('imgUrl')" :alt="dataNow('title')">-->
      <!--</div>-->

      <!--<div class="text">-->
        <!--<div class="detail">-->
          <!--<div class="teacher">{{dataNow('teacher')}} 主讲</div>-->
          <!--<div class="time">{{dataNow('time')}} 课时</div>-->
        <!--</div>-->
        <!--<h1>{{dataNow('title')}}</h1>-->
        <!--<div class="btn" @click="onEnterClicked">-->
          <!--<div>进入课程</div>-->
        <!--</div>-->
      <!--</div>-->
    <!--</div>-->
    <!--<div class="tip-box">-->
      <!--<div class="scroll">-->
        <!--<div class="tip" v-for="(section, index) in sections" @click="onTipClicked(index)" :style="{opacity: index == displayNow ? 1 : 0.75}">-->
          <!--<div class="color-bar" v-if="index == displayNow"></div>-->
          <!--<h1>{{section.title}}</h1>-->
          <!--<p>{{section.teacher}}</p>-->
        <!--</div>-->
      <!--</div>-->
    <!--</div>-->

    <el-carousel :interval="-1" :type="type" arrow="hover" :height="slideHeight" :class="type">
      <el-carousel-item v-for="s in sections" :autoplay="false" :key="s.id" class="page" :style="{height: slideHeight}">
        <div @click="onEnterClicked(s.id)" >
          <img :src="s.imgUrl" alt="" class="img">

          <div class="text">
            <div class="detail">
              {{s.desc}}
            </div>
            <h1>{{s.title}}</h1>
          </div>
        </div>
      </el-carousel-item>
    </el-carousel>

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
            id: 1,
          },
          {
            title: '线性代数',
            desc: '数学的一个分支，它的研究对象是向量，向量空间（或称线性空间），线性变换和有限维的线性方程组。',
            teacher: '东条希',
            time: 159,
            color: '#800080',
            imgUrl: '/slide/fbhs.jpg',
            id: 1,
          },
          {
            title: '概率论',
            desc: '概率论是研究随机现象数量规律的数学分支。',
            teacher: '星空凛',
            time: 155,
            color: '#FFFF00',
            imgUrl: '/slide/gll.jpg',
            id: 'gailvlun',
          },
          {
            title: '复变函数',
            desc: '以复数作为自变量和因变量的函数就叫做复变函数，而与之相关的理论就是复变函数论。',
            teacher: '矢泽妮可',
            time: 154,
            color: '#FFC0CB',
            imgUrl: '/slide/fbhs.jpg',
            id: 'fubianhanshu',
          },

        ],
        slideHeight: '0px',
        type: '',
        index: 0
      }
    },
    computed: {
    },
    methods: {
      onEnterClicked (id) {
        this.$router.push({ path: `/course/display/${id}`})
      },
      onChange (index) {
        this.index = index
      }
    },
    mounted: function () {
      let slideWidth = this.$refs.slide.getBoundingClientRect().width
      this.type = ((document.getElementsByClassName('navbar-more')[0].getBoundingClientRect().x === 0) &&
        (window.innerWidth < 1840)) ? '' : 'card'
      this.slideHeight = slideWidth * 9 / 16 * (this.type ? .81 : 1) + 'px'
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "slide.scss"
</style>
