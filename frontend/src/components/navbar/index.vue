<template>
  <div id="navbar">
    <div class="navbar">
      <router-link to="/">
        <logo></logo>
      </router-link>
      <span class="navbar-more" @click="toggleLink" :class="{'navbar-more-active': linkDisplay}">
        <span class="navbar-more-ch" :class="navbarClass(i)" v-for="i in [1, 2 ,3]"></span>
      </span>
      <div class="link-box" :class="{'side-box': linkDisplay}" @click="toggleLink">
        <div v-for="link in links" >
          <router-link :to="link[1]">{{link[0]}}</router-link>
        </div>
        <div class="account-box" v-if="!login" >
          <router-link to="/account/register" class="register">注册</router-link>
          <router-link to="/account/login" class="login">登录</router-link>
        </div>
        <div class="account-box" v-if="login">
          <router-link class="register" to="/profile">{{ username }}</router-link>
          <a class="login" @click="logout">退出</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import logo from '../logo/logo.vue'

  export default {
    components: {
      logo
    },
    computed: {
      navbarClass () {
        return i => [
          'navbar-more-ch' + i
        ]
      },
      login () {
        return this.$store.state.session.token !== null
      },
      username () {
        return this.$store.state.session.username
      },
      links () {
        const links = [
          ['首页', '/'],
          ['课堂论坛', '/bbs'],
          ['课程管理', '/manage']
        ]
        return links
      }
    },
    methods: {
      toggleLink () {
        this.linkDisplay = !this.linkDisplay
      },
      logout () {
        this.$store.dispatch('logout')
      }
    },
    data () {
      return {
        linkDisplay: false
      }
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "../../style/navbar"
</style>
