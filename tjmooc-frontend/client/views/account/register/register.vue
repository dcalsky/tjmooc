<template>
  <div id="account-register">

    <el-slider
      v-model="step"
      :step="1"
      :max="stepList.length - 1"
      :format-tooltip="formatTooltip"
      show-stops
    >
    </el-slider>

    <div class="title">
      {{order}}{{stepList[step].info}}
    </div>
    <div class="form">
      <div class="input" v-if="!finish">
        <input ref="input" v-if="stepList[step].type == 'number'" type="number" v-model="inputText">
        <input ref="input" v-if="stepList[step].type == 'text'" type="text" v-model="inputText">
        <input ref="input" v-if="stepList[step].type == 'password'" type="password" v-model="inputText">
      </div>
    </div>

    <!--<div hidden>{{messages()}}</div>-->

    <div class="bottom">
      <div class="error" v-if="errorText">{{errorText}}</div>
      <div class="btn-box">
        <div class="to" :class="{allowed: finish}" @click="toPrev" v-if="step">上一步</div>
        <div class="to" :class="{allowed: finish}" @click="toLogin" v-else>去登录</div>
        <div class="next" @click="onNextClicked" :class="{allowed: !inputTextLegal}" v-if="!finish">下一步</div>
      </div>
    </div>
  </div>
</template>

<script>
  import { server } from '../../../config'

  export default {
    name: "register",
    beforeCreate() {
      // If has logged, return home page
      if (this.$store.state.session.token) {
        this.$router.replace({name: 'home'})
      }
    },
    data () {
      return {
        step: 0,
        stepMax: 0,
        inputText: '',
        errorText: '',
        finish: false,
        form: {
          studentId: "",
          username: "",
          password: "",
          passwordCheck: "",
        },
        stepList: [
          {
            name: '学号',
            key: 'studentId',
            type: 'number',
            info: '您的学号？',
          },
          {
            name: '用户名',
            key: 'username',
            type: 'text',
            info: '您的用户名？',
          },
          {
            name: '密码',
            key: 'password',
            type: 'password',
            info: '您设定的密码？',
          },
          {
            name: '确认密码',
            key: 'passwordCheck',
            type: 'password',
            info: '刚才输入的密码是？'
          },
          {
            name: '完成',
            type: 'finish',
            info: '正在注册...'
          }
        ],

      }
    },
    filters: {
        hidePassword: function (value, type) {
          if (type === 'password')
              return '*'.repeat(value.length);
          else
              return value;
        }
    },
    methods: {
      onStepClicked: function (i) {
        if (this.finish)
          return;
        if (i <= this.stepMax) {
          this.step = i;
          let key = this.stepList[this.step].key;
          this.inputText = this.form[key];
        }
        else {
            this.step = this.stepMax;
        }
      },
      toLogin() {
        this.$router.push({name: 'login'});
      },
      toPrev() {
          this.onStepClicked(this.step - 1);
      },
      formatTooltip: function (i) {
        return this.stepList[i] && this.stepList[i].name;
      },
      onNextClicked: function () {
        if (!this.inputTextLegal)
            return;
        if (this.step >= this.stepList.length - 1) {
            this.step = 0;
            --this.stepMax;
          this.stepList[4].info = "正在注册...";
            return;
        }


        let key = this.stepList[this.step].key;
        this.form[key] = this.inputText;
        this.step += 1;
        if (this.stepMax < this.step)
            this.stepMax = this.step;
        this.inputText = '';
        this.focusText();
        if (this.step + 1 === this.stepList.length) {
          this.onFinish();
        }
      },
      focusText: function () {
        this.$refs.input.focus();
      },
      onFinish: function () {
        this.finish = true;
        // Ajax, register
        this.$store.dispatch('register', {
          username: this.form.studentId,
          password: this.form.password,
          nickname: this.form.username
        })
      },

      messages () {
        console.log(this.$store.state.user);
        this.finish = this.$store.state.user.messages.length === 9;
        if (this.finish) {
          this.stepList[4].info = "恭喜，注册成功!";
          this.errorText = '正在进入登录界面...';
          let that = this;
          setTimeout(() => {
            that.$router.replace({ name: 'login' })
          }, 1000);
        }
        else if (this.$store.state.user.messages.length > 0) {
          this.stepList[4].info = "抱歉，注册失败!";
          this.errorText = this.$store.state.user.messages.join('\n');
        }
        return this.$store.state.user.messages.join('\n');
        // 恭喜，注册完成！
      },
    },
    computed: {
      inputType: function () {
        return this.stepList[this.step].type
      },
      order() {
        this.onStepClicked(this.step);
          return this.step + 1 + '. ';
      },
      checkLegal: function () {
          return function (index, checkFunc) {
            let d, c;
            if (this.step === index) {
              d = this.inputText;
              c = checkFunc(d);
              this.errorText = c[1];
              return c[0];
            }
            else
              return true;
          }
      },
      inputTextLegal: function () {
        if (this.step + 1 === this.stepList.length)
            return true;
        let checkFunc = [
          input => {
            let w, b;
            b = input !== '';
            if (!b)
              w = "学号不得为空";
            return [b, w];
          },
          input => {
            let w, b;
            b = input !== '';
            if (!b)
              w = "用户名不得为空";
            return [b, w];
          },
          input => {
            let w, b;
            b = input.length > 5;
            if (!b)
              w = "密码长度不小于六位";
            return [b, w];
          },
          input => {
            let w, b;
            b = input === this.form.password;
            if (!b)
              w = "两次密码输入不一致";
            return [b, w];
          }
        ];
        return this.checkLegal(this.step, checkFunc[this.step]);
      },
    }
  }
</script>


<style lang="sass" rel="stylesheet/sass" scoped>
  @import "register"
</style>
