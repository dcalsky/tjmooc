<template>
  <div class="after-class">
    <div class="select-box" v-if="haveHomework || haveTest">
      <div class="select homework" :class="{selected: selectHomework}" @click="selectHomework = true">作 业</div>
      <div class="select test" :class="{selected: !selectHomework}" @click="selectHomework = false">测 试</div>
    </div>


    <homework class="content" v-if="selectHomework && haveHomework"></homework>
    <test class="content" v-else-if="!selectHomework && haveTest"></test>
    <!--<div class="error" v-else>-->
      <!--本章暂无{{selectHomework ? '作业' : '测试'}}-->
    <!--</div>-->
  </div>
</template>

<script>
  import homework from "./homework/homework.vue"
  import test from "./test/test.vue"
  export default {
    name: "after-class",
    components: {
      homework,
      test
    },
    data: function () {
        return {
          selectHomework: true
        }
    },
    computed:  {
        haveHomework() {
            console.log(this.$store.state.material.homework);
            return this.$store.state.material.homework && this.$store.state.material.homework.id;
        },
      haveTest() {
            return this.haveHomework;
      }
    },
    methods: {
    },
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "after-class"
</style>
