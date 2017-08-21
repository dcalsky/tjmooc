<template>
  <div id="forum">
    <navbar></navbar>
      <div class="wrapper">
        <router-view></router-view>
      <foot-bar></foot-bar>
    </div>
  </div>
</template>

<script>
  import footBar from "../../components/foot-bar/foot-bar.vue"
  import Navbar from "../../components/navbar/navbar.vue"

  export default {
    name: 'forum',
    components: {
      footBar,
      Navbar,
    }
  }
</script>

<style lang="scss">
  #forum .wrapper {
    padding: 25px;
    background: #fafafa;
  }
  .forum-header {
    h2 {
      font-size: 3rem;
    }
  }

</style>
