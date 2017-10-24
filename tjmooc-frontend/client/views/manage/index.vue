<template>
  <div>
    <navbar></navbar>
    <div id="manage" :style="{minHeight}">
      <div v-if="$route.name === 'manage'">
        <div>请选择管理的内容</div>
        <div class="types">
          <div class="type" @click="routerTo('course')">
            <el-card>
              <i class="el-icon-setting"></i>
              <div>课程管理</div>
            </el-card>
          </div>

          <div class="type" @click="routerTo('afterclass')">
            <el-card>
              <i class="el-icon-document"></i>
              <div>课后管理</div>
            </el-card>
          </div>
        </div>
      </div>
      <router-view></router-view>
    </div>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import FootBar from "../../components/footbar"
  import Navbar from "../../components/navbar/index.vue"

  export default {
    name: 'manage',
    components: {
      FootBar,
      Navbar
    },
    data () {
      return {
        minHeight: 0

      }
    },
    methods: {
      routerTo (p) {
        console.log(p)
        this.$router.push({path: `/manage/${p}`});
        console.log(this.$route)
      }
    },
    mounted () {
      this.minHeight = window.innerHeight - 96 + 'px'
    }
  }
</script>

<style lang="scss">
  @import "manage";
</style>
