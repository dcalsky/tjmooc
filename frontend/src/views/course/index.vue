<template>
  <div id="course">
    <display></display>
    <exercise></exercise>
  </div>
</template>

<script>
  import Display from './display.vue'
  import Exercise from './exercise.vue'
  export default {
    components: {
      Display,
      Exercise
    },
    data () {
      return {}
    }
  }
</script>

<style lang="scss">
  @import "../../style/course";
</style>
