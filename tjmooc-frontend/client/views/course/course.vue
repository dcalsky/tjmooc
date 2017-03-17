<template>
<<<<<<< HEAD
  <div id="course">
=======
  <div class="course-main">
>>>>>>> 多个页面
    <navbar></navbar>
    <router-view></router-view>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import Navbar from "../../components/navbar/navbar.vue"
  import FootBar from "../../components/foot-bar/foot-bar.vue"

export default {
    components: {
      Navbar,
      FootBar
    },
  }
</script>

<style lang="scss">
<<<<<<< HEAD
  #course {
=======
  .course-main {
>>>>>>> 多个页面
    min-width: 900px;
  }
</style>
