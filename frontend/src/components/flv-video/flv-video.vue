<template>
  <div class='videoContainer' :style='{height: videoHeight}'>
    <video ref='videoElement' class='centeredVideo' controls autoplay :width='width' height='100%'>
      Your browser is too old which doesn't support HTML5 video.
    </video>
    <div class='noVideo' :style='hoverStyle'>
      <img :src='alt' alt=''>
    </div>
  </div>
</template>

<script>
  import * as flvjs from 'flv.js/dist/flv.min'
  export default {
    name: 'flv-video',
    props: {
      width: {
        type: String,
        default: '800px'
      },
      height: {
        type: String,
        default: ''
      },
      ratio: {
        type: Number,
        default: 9 / 16
      },
      flv: {},
      alt: {
        type: String,
      }
    },
    data () {
      return {
        videoHeight: '0'
      }
    },
    computed: {
      hoverStyle () {
        return (this.flv && this.flv.url) ? {
          opacity: 0,
          transform: 'translateY(-100%)'
        } : {}
      }
    },
    methods: {
      flv_load () {
        let element = this.$refs.videoElement;
        this.player = flvjs.createPlayer(
          this.flv,
          {
            enableWorker: false,
            lazyLoadMaxDuration: 3 * 60,
            seekType: 'range',
          }
        );
        this.player.attachMediaElement(element);
        this.player.load();
        window.p = this.player
      },
      flv_start () {
        this.player && this.player.play();
      },
      flv_pause () {
        this.player && this.player.pause();
      },
      flv_destroy () {
        if (this.player) {
          this.player.pause();
          this.player.unload();
          this.player.detachMediaElement();
          this.player.destroy();
          this.player = null;
        }
      },
    },
    watch: {
      'flv.url' (val) {
        this.flv_load()
      }
    },
    mounted () {
      this.videoHeight = this.height ? this.height : this.$el.offsetWidth * this.ratio + 'px';
    }
  }
</script>

<style lang='sass' rel='stylesheet/sass'>
  @import 'flv-video'
</style>
