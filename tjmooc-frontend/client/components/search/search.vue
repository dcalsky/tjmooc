<template>
  <div class="search">
    <i :class="`fa fa-${icon} fa-1x`" v-if="icon"></i>
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
      },
      icon: {
          type: String,
        default: "search"
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
