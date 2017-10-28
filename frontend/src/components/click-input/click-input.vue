<template>
  <span class="click-input">
    {{textarea}}
    <el-input
      :size="size"
      :type="textarea === undefined ? '' : 'textarea'"
      :autosize="{ minRows: 1 }"
      resize="none"
      v-model="val"
      class="w"
      icon="close"
      :on-icon-click="click"
      :class="{t: val}"
    ></el-input>
  </span>
</template>

<script>
  export default {
    name: 'click-input',
    props: ['value', 'size', 'textarea'],
    watch: {
      value (v) {
        this.val = v
      },
      val (v) {
        if (v !== this.value) {
          this.$emit('input', v)
        }
      }
    },
    methods: {
      click () {
        this.$emit('remove')
      }
    },
    data () {
      return {
        val: this.value
      }
    }
  }
</script>

<style lang="scss" rel="stylesheet/scss">
  .click-input {
    display: inline-flex;
  }
  .w {
    width: 100%;
  }
  .t {
    textarea {
      border-color: transparent;
    }
  }
</style>
