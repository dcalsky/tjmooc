<template>
  <div>
    <div id="account">
      <!--<div class="paper">-->
        <!--<div class="back-home" @click="backHome">-->
          <!--<i class="fa fa-home fa-lg"></i>-->
          <!--<span>返回主页</span>-->
        <!--</div>-->
        <!--&lt;!&ndash;<router-view></router-view>&ndash;&gt;-->
        <!--<div id="account-logo-tie"></div>-->
      <!--</div>-->
      <div class="front">

        <div class="back" :class="left ? 'back-left' : 'back-right'">
          <div class="title">{{title}}</div>
        </div>
        <router-view></router-view>
      </div>
      <div class="home" @click="backHome" :class="left ? 'home-right' : 'home-left'">
        <div class="toggle">返回主页</div>
        <logo url="/icon.svg"></logo>
      </div>
    </div>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import logo from 'components/logo/logo'
  import footBar from "../../components/foot-bar/foot-bar.vue"
  export default {
    name: "account",
    components: {
      logo,
      footBar
    },
    data: function () {
      return {
        width: 600,
        height: 200
      }
    },
    methods: {
      backHome() {
        this.$router.push({name: 'home'});
      }
    },
    computed: {
      title() {
        return {
          register: '注 册',
          login: '登 录'
        }[this.$route.name];
      },
      left() {
          return this.$route.name === 'login'
      }
    },
    mounted: function () {
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass" scoped>
  @import "account"
</style>
