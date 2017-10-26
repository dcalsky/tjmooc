<template>
  <div id="app">
    <navbar v-if="showNav"></navbar>
      <router-view :style="{minHeight}"></router-view>
    <footbar v-if="showFoot"></footbar>
  </div>
</template>

<script>
  import Navbar from '../components/navbar/index.vue'
  import Footbar from '../components/footbar/index.vue'

  export default {
    components: {
      Navbar,
      Footbar
    },
    watch: {
      $route: {
        deep: true,
        handler ({name}) {
          console.log(name)
          this.showNav = !this.navRule[name] && true
          this.showFoot = !this.footRule[name] && true
        }
      }
    },
    data () {
      return {
        minHeight: 0,
        showNav: true,
        showFoot: true,
        navRule: {
          register: 1,
          login: 1
        },
        footRule: {
        }
      }
    },
    mounted () {
      this.minHeight = window.innerHeight - 64 + 'px'
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "../style/app"
</style>
