<template>
  <div id="home" ref="home">
    <!--slide-->
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

    <!--<course-select></course-select>-->
  </div>
</template>

<script>
  import CourseSelect from './course-select/course-select'

  export default {
    name: 'home',
    components: {
      CourseSelect,
    },
    data: function () {
      return {
        sections: [
          {
            title: '高等数学',
            desc: '由微积分学，较深入的代数学、几何学以及它们之间的交叉内容所形成的一门基础学科。',
            imgUrl: '/slide/gdsx.jpg',
            id: 1,
          },
          {
            title: '线性代数',
            desc: '数学的一个分支，它的研究对象是向量，向量空间（或称线性空间），线性变换和有限维的线性方程组。',
            imgUrl: '/slide/fbhs.jpg',
            id: 1,
          },

        ],
        slideHeight: '0px',
        type: '',
        index: 0
      }
    },
    methods: {
      onEnterClicked(id) {
        this.$router.push({path: `/course/display/${id}`})
      },
    },
    mounted: function () {
      const w = this.$refs.home.getBoundingClientRect().width
      this.type = ((document.getElementsByClassName('navbar-more')[0].getBoundingClientRect().x === 0) &&
        (window.innerWidth < 1840)) ? '' : 'card'
      this.slideHeight = w * 9 / 16 * (this.type ? .81 : 1) + 'px'
    }
  }
</script>

<style lang="scss">
  @import "../../style/home";
</style>
