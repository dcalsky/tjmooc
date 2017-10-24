<template>
  <div>
    <div id="account">
      <div class="front">
        <div class="back" :class="left ? 'back-left' : 'back-right'">
          <div class="title">{{title}}</div>
        </div>
        <router-view></router-view>
      </div>
      <div class="home" @click="backHome" :class="left ? 'home-right' : 'home-left'">
        <div class="toggle">返回主页</div>
        <logo></logo>
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
        width: 600,
        height: 200,
        minHeight: 0
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
  }
</script>

<style lang="sass" rel="stylesheet/sass" scoped>
  @import "account"
</style>
