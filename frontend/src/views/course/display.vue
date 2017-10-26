<template>
  <div class="course-display">
    <player></player>
    <after-class></after-class>
  </div>
</template>

<script>
  import Player from "./player/player.vue"
  import AfterClass from "./after-class/after-class.vue"
  export default {
    components: {
      Player,
      AfterClass,
    },
    data() {
      return {
      }
    },
    computed: {
      createTime() {
        let t = this.video.createTimestamp;
        let y = t.getFullYear(), m = t.getMonth(), d = t.getDate(),
          mName = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        return `${mName[m]} ${d}, ${y}`;
      },
    }
  }
</script>

<style lang="scss" scoped>
  @import "display.scss";
</style>
