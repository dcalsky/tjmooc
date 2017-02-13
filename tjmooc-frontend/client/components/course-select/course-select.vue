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
          <a class="btn" :href="c.url">参与这门课</a>
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
                url: "/shu"
              },
              {
                name: "丑",
                url: "/niu"
              },
            ]
          },
          {
            name: "地方向",
            courses: [
              {
                name: "辰",
                url: "/long"
              },
              {
                name: "巳",
                url: "/she"
              },
              {
                name: "辰",
                url: "/long"
              },
              {
                name: "巳",
                url: "/she"
              },
              {
                name: "辰",
                url: "/long"
              },
              {
                name: "巳",
                url: "/she"
              },
              {
                name: "辰",
                url: "/long"
              },
              {
                name: "巳",
                url: "/she"
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
                url: "/hou"
              },
              {
                name: "酉",
                url: "/ji"
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
