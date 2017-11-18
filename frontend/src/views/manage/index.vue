<template>
  <div id="manage">
    <div v-if="$route.name === 'manage'" class="manage">
      <div>请选择管理的内容</div>
      <div class="types">
        <div class="type" @click="routerTo('course')">
          <el-card>
            <i class="el-icon-menu"></i>
            <div>课程管理</div>
          </el-card>
        </div>

        <div class="type" @click="routerTo('afterclass')">
          <el-card>
            <i class="fa fa-sticky-note"></i>
            <div>课后管理</div>
          </el-card>
        </div>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'manage',
    methods: {
      routerTo (p) {
        this.$router.push({name: `manage-${p}`})
      }
    }
  }
</script>

<style lang="scss">
  @import "../../style/manage";
</style>
