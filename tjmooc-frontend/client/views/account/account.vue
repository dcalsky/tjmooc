<template>
  <div>
    <div id="account">
      <div class="account" :style="{minHeight}">
        <div class="home" @click="backHome" :class="left ? 'home-right' : 'home-left'">
          <div class="toggle">返回主页</div>
          <logo></logo>
        </div>
        <div class="front">
          <div class="back" :class="left ? 'back-left' : 'back-right'">
            <div class="title">{{title}}</div>
          </div>
          <router-view :style="{minHeight: routerHeight}"></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import logo from 'components/logo/logo'
  export default {
    name: "account",
    components: {
      logo
    },
    data: function () {
      return {
        minHeight: 0,
        routerHeight: 0
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
      },
    },
    mounted () {
      this.minHeight = window.innerHeight - 64 + 'px'
      if (window.innerWidth <= 480) {
        this.routerHeight = window.innerHeight - 64 - 98 + 'px'
      }
      else {
        this.routerHeight = 0
      }
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "account"
</style>
