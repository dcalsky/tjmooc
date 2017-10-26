<template>
  <div id="forum">
    <navbar></navbar>
    <router-view :style="{minHeight}"></router-view>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import footBar from "components/footbar/footbar"
  import Navbar from "components/navbar/navbar"

  export default {
    name: 'forum',
    data () {
      return {
        minHeight: 0
      }
    },
    components: {
      footBar,
      Navbar,
    },
    mounted () {
      this.minHeight = window.innerHeight - 96 + 'px'
    }
  }
</script>
