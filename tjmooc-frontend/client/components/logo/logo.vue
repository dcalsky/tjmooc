<template>
  <div :id="componentId" class="logo"></div>
</template>

<script>
  export default {
    name: "logo",
    props: {
      height: {
        type: Number,
        default: -1
      },
      componentId: {
        type: String,
        default: "logo"
      },
      url: {
          type: String,
        default: '/icon_title.svg'
      }
    },
    mounted: function() {
      let logo = Snap('#' + this.componentId);
      let h = this.height < 0 ? this.$el.offsetHeight : this.height;
      let t = Snap.load(this.url, function (svg) {
          this.appendChild(svg.node);
          logo.select('svg').attr({
            height: h
          });
      }, document.getElementById(this.componentId));
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "logo"
</style>
