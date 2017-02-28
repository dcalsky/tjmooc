<template>
  <div id="forum">
    <navbar></navbar>
    <div class="wrapper">
      <div class="forum-header">
        <h2>板块一览</h2>
        <hr >
      </div>
      <ul class="content">
        <li v-for="item in items">
          {{ item }}
        </li>
      </ul>
    </div>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import footBar from "../../components/foot-bar/foot-bar.vue"
  import Navbar from "../../components/navbar/navbar.vue"
  import divide from '../../components/divide/divide.vue'
  export default {
    name: 'forum',
    components: {
      footBar,
      Navbar,
      divide
    },
    beforeCreate() {
      // Ajax to get data
      this.items = ['1', '2']
    }
  }
</script>

<style lang="scss">
@import "forum.scss"
</style>
