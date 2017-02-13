<template>
  <div class="page">
    <navbar></navbar>
    <slide></slide>
    <course-select></course-select>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import navbar from 'components/navbar/navbar'
  import slide from 'components/slide/slide'
  import courseSelect from 'components/course-select/course-select'
  import footBar from 'components/foot-bar/foot-bar'

  export default {
    components: {
        navbar,
        slide,
        courseSelect,
        footBar,
    },
  }
</script>

<style lang="scss">
</style>
