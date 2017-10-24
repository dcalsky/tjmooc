<template>
  <div id="app">
    <navbar></navbar>
    <router-view :style="{minHeight}"></router-view>
    <footbar></footbar>
  </div>
</template>

<script>
  import Navbar from '../components/navbar/index.vue'
  import Footbar from '../components/footbar/index.vue'

  export default {
    components: {
      Navbar,
      Footbar,
    },
    data () {
      return {
        minHeight: 0

      }
    },
    mounted () {
      this.minHeight = window.innerHeight - 96 + 'px'
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "../style/app"
</style>
