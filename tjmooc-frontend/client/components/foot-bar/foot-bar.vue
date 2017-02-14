<template>
  <div class="foot-bar">
    <div class="link-box">
      <router-link :to="l[1]" v-for="l in links">{{l[0]}}</router-link>
    </div>
    <div class="brand" @click="eggshell">
      <logo :height="35" componentId="foot-logo"></logo>
      <a :href="school[0].url">{{school[0].name}}</a>
    </div>
  </div>
</template>

<script>
  import logo from "../../components/logo/logo.vue"
  export default {
    name: "foot-bar",
    components: {
        logo
    },
    data: function () {
      return {
        school: [
          {
            name: "同济大学数学科学学院",
            url: "http://math.tongji.edu.cn/"
          },
          {
            name: "同济大学软件学院",
            url: "http://sse.tongji.edu.cn/en"
          },
        ],
        links: [
          ['主页', '/'],
          ['关于我们', '/about'],
          ['课堂论坛', '/forum'],
          ['版权声明', '/copyright'],
          ['沪ICP备160000xx号', '/beian'],
        ]
      }
    },
    methods: {
        eggshell: function () {
          this.school.reverse();
        }
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "foot-bar"
</style>
