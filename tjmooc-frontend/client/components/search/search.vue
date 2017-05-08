<template>
  <div class="search">
    <i class="fa fa-search fa-2x"></i>
    <input type="text" :value="value" @input="updateValue">
    <div class="remove" v-if="value" @click="onRemoveBtnClicked"></div>
  </div>
</template>

<script>
  export default {
    name: "search",
    props: {
      value: {
        type: String,
        default: ""
      }
    },
    data() {
      return {
      }
    },
    computed: {
    },
    methods: {
      updateValue(e) {
        this.$emit('input', e.target.value);
      },
      onRemoveBtnClicked: function (e) {
        this.$emit('input', '');
        this.$el.getElementsByTagName('input')[0].focus();
      },
    },
  }
</script>

<style lang="sass" rel="stylesheet/sass" scoped>
  @import "search"
</style>
