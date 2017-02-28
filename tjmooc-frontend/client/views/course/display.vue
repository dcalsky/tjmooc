<template>
  <div id="course-display">
    <player :flv="flv"></player>
    <after-class></after-class>
  </div>
</template>

<script>
  import Player from "../../components/player/player.vue"
  import AfterClass from "../../components/after-class/after-class.vue"
  export default {
    components: {
      Player,
      AfterClass,
    },
    data() {
      return {
        video: {
          flv: {
            type: 'mp4',
            url: 'http://ohp6g3bar.bkt.clouddn1.com/job_IMG_1603.MOV',
          },
          title: "同济大学摇滚高等数学",
          desc: "flv.js works by transmuxing FLV file stream into ISO BMFF (Fragmented MP4) segments, followed by feeding mp4 segments into an HTML5 \<video\> element through Media Source Extensions API.",
          teacher: "朱彦樵",
          createTimestamp: new Date(),
        }
      }
    },
    computed: {
      createTime() {
        let t = this.video.createTimestamp;
        let y = t.getFullYear(), m = t.getMonth(), d = t.getDate(),
          mName = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        return `${mName[m]} ${d}, ${y}`;
      },
      flv() {
        return this.video.flv;
      }
    }
  }
</script>

<style lang="scss">
  @import "display.scss";
</style>
