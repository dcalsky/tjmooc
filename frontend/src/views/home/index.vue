<template>
  <div id="home" ref="home">
    <!--slide-->
    <el-carousel :interval="-1" :type="type" arrow="hover" :height="slideHeight" :class="type">
      <el-carousel-item v-for="t in tops" :autoplay="false" :key="t.id" class="page" :style="{height: slideHeight}">
        <div @click="onEnterClicked(t.id)" >
          <img :src="t.cover_image" alt="" class="img">

          <div class="text">
            <div class="detail">
              {{t.introduction}}
            </div>
            <h1>{{t.title}}</h1>
            <div class="subtitle">{{t.subtitle}}</div>
          </div>
        </div>
      </el-carousel-item>
    </el-carousel>

    <course-select></course-select>
  </div>
</template>

<script>
  import CourseSelect from './course-select/course-select'

  export default {
    name: 'home',
    components: {
      CourseSelect
    },
    data: function () {
      return {
        slideHeight: '0px',
        type: '',
        index: 0
      }
    },
    computed: {
      tops () {
        return this.$store.state.course.tops
      }
    },
    methods: {
      onEnterClicked (id) {
        this.$router.push({path: `/course/${id}`})
      }
    },
    mounted: function () {
      this.$store.dispatch('getTops')
      const w = this.$refs.home.getBoundingClientRect().width
      this.type = ((document.getElementsByClassName('navbar-more')[0].getBoundingClientRect().x === 0) &&
        (window.innerWidth < 1840)) ? '' : 'card'
      this.slideHeight = w * 9 / 16 * (this.type ? 0.81 : 1) + 'px'
    }
  }
</script>

<style lang="scss">
  @import "../../style/home";
</style>
