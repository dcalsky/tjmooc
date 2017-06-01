<template>
  <div class="after-class">
    <div class="select-box">
      <div class="select homework" :class="{selected: selectHomework}" @click="selectHomework = true">作 业</div>
      <div class="select test" :class="{selected: !selectHomework}" @click="selectHomework = false">测 试</div>
    </div>
    <div v-if="selectHomework">
      <homework v-if="haveHomework"></homework>
      <div class="error" v-if="!haveHomework">
        本章暂无作业
      </div>
    </div>
    <test v-else></test>
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
            return this.$store.state.material.homework.id;
        },
      haveTest() {
            return true;
      }
    },
    methods: {
    },
  }
</script>

<style lang="sass" rel="stylesheet/sass" scoped>
  @import "after-class"
</style>
