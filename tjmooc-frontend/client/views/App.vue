<template>
  <div id="app">
    <navbar v-if="showNav"></navbar>
    <div :style="{minHeight}">
      <router-view></router-view>
    </div>
    <footbar v-if="showFoot"></footbar>
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
      this.minHeight = window.innerHeight - 96 + 'px'
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "../style/app"
</style>
