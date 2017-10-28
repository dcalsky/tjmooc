<template>
  <div id="course">
    <player></player>
  </div>
</template>

<script>
  import Player from './player/player.vue'
//  import AfterClass from './after-class/after-class.vue'
  export default {
    components: {
      Player
      //      AfterClass
    },
    data () {
      return {
      }
    }
  }
</script>

<style lang="scss">
  @import "../../style/course";
</style>
