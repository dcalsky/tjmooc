<template>
  <div class="divide">
    <div class="text">{{text}}</div>
  </div>
</template>

<script>
  export default {
    name: 'divide',
    props: {
      text: {
        type: String,
        default: 'NEXT'
      }
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "divide"
</style>
