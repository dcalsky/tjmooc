<template>
  <div id="notfound">
    <img src="../assets/tjmooc-404.svg" alt="404 Not Found">
  </div>
</template>

<script>
  export default {
    components: {
    }
  }
</script>

<style lang="scss" scoped>
  @import "../style/config";
  #notfound {
    display: flex;
    img {
      width: 80%;
      max-width: 920px;
      margin: auto;
      @include mobile {
        width: 90%;
      }
    }
  }
</style>
