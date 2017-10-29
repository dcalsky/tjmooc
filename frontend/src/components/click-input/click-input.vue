<template>
  <span class="click-input">
    <el-input
      :size="size"
      :type="textarea === 'textarea' ? 'textarea' : ''"
      :autosize="{ minRows: 1 }"
      resize="none"
      v-model="val"
      class="w"
      :class="{t: val}"
    >
      <i slot="suffix" class="el-input__icon el-icon-close" @click="click"></i>
    </el-input>
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
        this.$emit('input', '')
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
    input, textarea {
      border-color: transparent;
    }
  }
</style>
