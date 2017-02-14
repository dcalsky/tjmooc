<template>
  <div class="course-select">
    <div class="top">
      <div class="search">
        <i class="fa fa-search fa-2x"></i>
        <input type="text" v-model="searchText">
        <div class="remove" v-if="searchText" @click="onRemoveBtnClicked"></div>
      </div>

    </div>

    <div class="select" :class="{subSelected: subjectNow != -1}">
      <div class="back"></div>
      <div class="left">
        <div class="subject" v-for="(s, index) in subject" @click="onSubjectClicked(index)" :class="{selected: index == subjectNow}">
          {{s.name}}
        </div>
      </div>
      <div class="right">
        <div class="info" v-if="subjectNow == -1">选择感兴趣的方向</div>
        <div class="info" v-if="subjectNow != -1 && course.length == 0">暂无课程</div>
        <div class="course" v-for="(c, index) in course">
          <div class="title">{{c.name}}</div><div class="teacher">妮可</div>
          <p class="desc">啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高啦啦赛高</p>
          <router-link class="btn" :to="'/course/display/' + c.courseId">参与这门课</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "course-select",
    data: function () {
      return {
        searchText: '',
        subject: [
          {
            name: "天方向",
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
            name: "地方向",
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
            name: "玄方向",
            courses: [
            ]
          },
          {
            name: "黄方向",
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
      }
    },
    methods: {
      onRemoveBtnClicked: function () {
          this.searchText = "";
      },
      onSubjectClicked: function(index) {
          this.subjectNow = index;
      }
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "course-select"
</style>
