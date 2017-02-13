<template>
  <div class="navbar">
    <logo v-bind:height="48"></logo>
    <div class="link-box">
      <div v-for="link in links" >
        <a v-bind:href="link[1]">{{link[0]}}</a>
      </div>
      <div class="account-box" v-if="!login">
        <router-link to="/account/register" class="register">注册</router-link>
        <router-link to="/account/login" class="login">登录</router-link>
      </div>
    </div>
  </div>
</template>

<script>
  import logo from 'components/logo/logo'

  export default {
    components: {
      logo
    },
    data: function() {
      let
        login = false,
        links = [
          ['全部课程', '1'],
          ['课堂论坛', '2'],
        ];
      if (login)
        links += [
            ['我的课程', '3']
        ];
      return {
        links: links,
        login: login
      }
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "navbar"
</style>
