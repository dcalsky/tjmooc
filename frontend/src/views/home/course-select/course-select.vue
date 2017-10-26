<template>
  <div class='course-select-box'>
    <div class='course-select'>
      <div class='top'>
        <!--<div class='search'>-->
          <!--<i class='fa fa-search fa-2x'></i>-->
          <!--<input type='text' v-model='searchText'>-->
          <!--<div class='remove' v-if='searchText' @click='onRemoveBtnClicked'></div>-->
        <!--</div>-->
        <search v-model='searchText'></search>

      </div>

      <div class='select'>
        <!--:class='{subSelected: subjectNow != -1}'-->
        <div class='left'>
          <div class='back'>
            <img src="../../../assets/tongji.svg" alt="">
          </div>
          <el-pagination
            class='subject'
            small
            layout='total, prev, pager, next'
            @current-change='handlePageChange'
            :total='count'>
          </el-pagination>
          <!--<div class='subject' v-if='false' v-for='(s, index) in subject' @click='onSubjectClicked(index)' :class='{selected: index == subjectNow}'>-->
            <!--{{s.name}}-->
          <!--</div>-->
        </div>
        <div class='right'>
          <!--<div class='info' v-if='subjectNow == -1'>选择感兴趣的方向</div>-->
          <!--<div class='info' v-if='subjectNow != -1 && course.length == 0'>暂无课程</div>-->
          <div
            class='course'
            v-for='c in course'
            @click='$router.push({path: `/course/display/${c.id}`})'
          >
            <div class='title'>{{c.title}}</div><div class='teacher'>{{c.subtitle}}</div>
            <p class='desc'>{{c.introduction}}</p>
            <!--<router-link class='btn' :to=''/course/display/' + c.courseId'>参与这门课</router-link>-->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Search from '../../../components/search/search.vue'
  export default {
    name: 'course-select',
    components: {
      Search
    },
    data: function () {
      return {
        searchText: ''
      }
    },
    computed: {
      course () {
        const course = this.$store.state.course.courses
        if (course && this.searchText) {
          return course.filter(c => c.name === this.searchText)
        }
        return course
      },
      count () {
        return this.$store.state.course.count
      }
    },
    methods: {
      handlePageChange (i) {
        this.$store.dispatch('getCourses', i)
      }
    },
    created () {
      this.$store.dispatch('getCourses', 1)
    }
  }
</script>
