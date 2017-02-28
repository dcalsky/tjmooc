<template>
  <div class="after-class">
    <div class="select-box">
      <div class="select homework" :class="{selected: selectHomework}" @click="selectHomework = true">作 业</div>
      <div class="select test" :class="{selected: !selectHomework}" @click="selectHomework = false">测 试</div>
    </div>
    <homework v-if="selectHomework"></homework>
    <test v-if="!selectHomework"></test>
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
    },
    methods: {
    },
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "after-class"
</style>
