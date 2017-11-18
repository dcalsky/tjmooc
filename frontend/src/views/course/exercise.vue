<template>
  <div id="course-exercise" v-if="homeworkId || testId">
    <div class="select-box" v-if="homeworkId && testId">
      <div class="select homework" :class="{selected: selectHomework}" @click="selectHomework = true">作 业</div>
      <div class="select test" :class="{selected: !selectHomework}" @click="selectHomework = false">测 试</div>
    </div>
    <div class="select-box" v-else>
      <div class="select single selected">{{ homeworkId ? `作 业` : `测 试` }}</div>
    </div>
    <divide class="mid"></divide>

    <homework class="content" v-if="selectHomework && homeworkId"></homework>
    <test class="content" v-else></test>
  </div>
</template>

<script>
  import homework from './homework/homework.vue'
  import divide from '../../components/divide/divide.vue'
  import test from './test/test.vue'
  export default {
    name: 'course-exercise',
    components: {
      homework,
      divide,
      test
    },
    data: function () {
      return {
        selectHomework: 1
      }
    },
    watch: {
      selectHomework (val) {
        if (val) {
          this.$store.dispatch('getHomework', {id: this.homeworkId})
        } else {
          this.$store.dispatch('getTest', {id: this.testId})
        }
      }
    },
    computed: {
      testId () {
        const t = this.$store.state.course.chapter.tests
        const id = t && t[0] && t[0].id
        if (id) {
          this.selectHomework = false
        }
        return id
      },
      homeworkId () {
        const h = this.$store.state.course.chapter.homeworks
        const id = h && h[0] && h[0].id
        if (id) {
          this.selectHomework = true
        }
        return id
      }
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  /*@import "after-class"*/
</style>
