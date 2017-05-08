<template>
  <div class="videoContainer" :style="{height: videoHeight}">
    <video name="videoElement" class="centeredVideo" controls autoplay :width="width" height="100%">
      Your browser is too old which doesn't support HTML5 video.
    </video>
  </div>
</template>

<script>
  import * as flvjs from "flv.js/dist/flv.min"
  export default {
    name: "flv-video",
    props: {
      width: {
        type: String,
        default: "800px"
      },
      height: {
        type: String,
        default: ""
      },
      ratio: {
          type: Number,
        default: 9 / 16
      },
      flv: {}
    },
    data() {
        return {
            videoHeight: '0'
        }
    },
    methods: {
      flv_load() {
        let
          element = document.getElementsByName('videoElement')[0],
          player = flvjs.createPlayer(
              this.flv,
            {
            enableWorker: false,
            lazyLoadMaxDuration: 3 * 60,
            seekType: 'range',
            }
          );
        player.attachMediaElement(element);
        player.load();
      },
      flv_start() {
        player.play();
      },
      flv_pause() {
        player.pause();
      },
      flv_destroy() {
        player.pause();
        player.unload();
        player.detachMediaElement();
        player.destroy();
        player = null;
      },
    },
    mounted: function() {

      this.videoHeight = this.height ? this.height : this.$el.offsetWidth * this.ratio + 'px';
        this.flv_load();
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "flv-video"
</style>
