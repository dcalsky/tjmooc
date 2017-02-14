<template>
  <div>
    <div class="account" :style="scrStyle">
      <div class="paper">
        <router-view></router-view>

      </div>
    </div>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import footBar from "../../components/foot-bar/foot-bar.vue"
  export default {
    name: "account",
    components: {
      footBar
    },
    data: function () {
      return {
          width: 600,
          height: 200
      }
    },
    methods: {
    },
    computed: {
      scrWidth: function () {
        let w = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
        return w;
      },
      scrHeight: function () {
        let h = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
        return h;
      },
      scrStyle: function () {
        return {
          height: this.scrHeight - 120 + 'px',
          width: this.scrWidth - 100 + 'px',
        }
      }
    },
    mounted: function() {
      let logo = Snap('#account-logo-tie');
      let
        h = (this.scrHeight - 150) * 0.4,
        w = (this.scrWidth - 90);
      let t = Snap.load("/icon_tie.svg", function (svg) {
        this.appendChild(svg.node);
        let wNow = logo.select('svg').attr('width') - logo.select('rect').attr('width');
        logo.select('rect').attr({
          width: w - wNow
        });
        logo.select('svg').attr({
          height: h,
          width: w
        });
      }, document.getElementById('account-logo-tie'));
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "account"
</style>
