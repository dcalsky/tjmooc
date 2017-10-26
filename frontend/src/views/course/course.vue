<template>
  <div class="course-main">
    <navbar></navbar>
    <router-view></router-view>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import Navbar from "../../components/navbar"
  import FootBar from "../../components/footbar"

export default {
    components: {
      Navbar,
      FootBar
    },
  }
</script>

<!--<style lang="scss">-->
  <!--@import "../../components/config";-->
  <!--.course-main {-->
    <!--@include respond-to('xs') {-->
      <!--min-width: 900px;-->
    <!--}-->
  <!--}-->
<!--</style>-->
