<template>
  <div id="forum">
    <navbar></navbar>
    <router-view></router-view>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import footBar from "components/foot-bar/foot-bar"
  import Navbar from "components/navbar/navbar"

  export default {
    name: 'forum',
    components: {
      footBar,
      Navbar,
    }
  }
</script>
