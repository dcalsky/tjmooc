<template>
  <div class="course-select">
    <div class="top">
      <!--<div class="search">-->
        <!--<i class="fa fa-search fa-2x"></i>-->
        <!--<input type="text" v-model="searchText">-->
        <!--<div class="remove" v-if="searchText" @click="onRemoveBtnClicked"></div>-->
      <!--</div>-->
      <search v-model="searchText"></search>

    </div>

    <div class="select" :class="{subSelected: subjectNow != -1}">
      <div class="left">
        <div class="back"></div>
        <div class="subject" v-for="(s, index) in subject" @click="onSubjectClicked(index)" :class="{selected: index == subjectNow}">
          {{s.name}}
          <div class="percentage" :style="{width: scrollPercentage + '%'}"></div>
        </div>
      </div>
      <div class="right">
        <div class="info" v-if="subjectNow == -1">选择感兴趣的方向</div>
        <div class="info" v-if="subjectNow != -1 && course.length == 0">暂无课程</div>
        <div class="course" v-for="(c, index) in course">
          <div class="title">{{c.name}}</div><div class="teacher">妮可</div>
          <p class="desc">Vue.js 是一套构建用户界面的 渐进式框架。与其他重量级框架不同的是，Vue 采用自底向上增量开发的设计。Vue 的核心库只关注视图层，并且非常容易学习，非常容易与其它库或已有项目整合。</p>
          <router-link class="btn" :to="'/course/display/' + c.courseId">参与这门课</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Search from '../../../components/search/search.vue'
  export default {
    name: "course-select",
    components: {
      Search
    },
    data: function () {
      return {
        searchText: '',
        subject: [
          {
            name: "软件方向",
            courses: [
              {
                name: "子",
                courseId: "shu"
              },
              {
                name: "丑",
                courseId: "niu"
              },
            ]
          },
          {
            name: "车辆方向",
            courses: [
              {
                name: "辰",
                courseId: "long"
              },
              {
                name: "巳",
                courseId: "she"
              },
              {
                name: "辰",
                courseId: "long"
              },
              {
                name: "巳",
                courseId: "she"
              },
              {
                name: "辰",
                courseId: "long"
              },
              {
                name: "巳",
                courseId: "she"
              },
              {
                name: "辰",
                courseId: "long"
              },
              {
                name: "巳",
                courseId: "she"
              },
            ]
          },
          {
            name: "智能方向",
            courses: [
            ]
          },
          {
            name: "数字方向",
            courses: [
              {
                name: "申",
                courseId: "hou"
              },
              {
                name: "酉",
                courseId: "ji"
              },
            ]
          },
        ],
        subjectNow: -1
      }
    },
    computed:  {
      course: function () {
        let course;
        if (this.subjectNow >= 0)
          course = this.subject[this.subjectNow].courses;
        else
          course = [];
        if (course && this.searchText) {
          course = course.filter(c => c.name == this.searchText)
        }
        return course;
      },
      scrollPercentage: function () {
//        let bar = document.getElementsByName('course-scroll-bar');
        console.log(this.$refs.scrollBar);
//        let p = (bar.scrollTop + 1) / (bar.scrollHeight - bar.offsetHeight + 1);
//        console.log(bar.scrollTop, bar.scrollHeight, bar.offsetHeight);
//        return p;
        return 0;
      }
    },
    methods: {
      onSubjectClicked: function(index) {
        console.log(this.$refs.scrollBar);
          this.subjectNow = index;
      }
    },
  }
</script>

<style lang="sass" rel="stylesheet/sass" scoped>
  @import "../../../style/home"
</style>
