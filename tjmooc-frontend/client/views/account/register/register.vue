<template>
  <div class="account-register">
    <div class="right">
      <div class="info">{{stepList[step].info}}</div>

      <div class="input" v-if="!finish">
        <input v-if="stepList[step].type == 'number'" type="number" v-model="inputText">
        <input v-if="stepList[step].type == 'text'" type="text" v-model="inputText">
        <input v-if="stepList[step].type == 'password'" type="password" v-model="inputText">

        <div class="remove" v-if="inputTextLegal" @click="onRemoveBtnClicked"></div>
      </div>

      <div class="next" @click="onNextClicked" v-if="inputTextLegal && !finish">下一步</div>
      <div class="error" v-if="errorText && !finish">{{errorText}}</div>
    </div>
    <div class="left" :style="{flexBasis: leftWidth + 'px'}">
      <div>
        <h1 class="title"><router-link to="/account/login">登录</router-link>注册</h1>
        <div @click="onStepClicked(index)" v-for="(s, index) in stepList" :class="{now: index == step, been: index <= stepMax }">
          <span>{{s.name}}</span>
          <span v-if="form[s.key]">{{form[s.key] | hidePassword(stepList[index].type)}}</span>
          <span class="bar"></span>
        </div>
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
            info: '恭喜，注册完成！正在进入登录界面...'
          }
        ],

      }
    },
    filters: {
        hidePassword: function (value, type) {
          if (type == 'password')
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
      },
      onRemoveBtnClicked: function () {
        this.inputText = "";
        this.focusText();
      },
      onNextClicked: function () {
        let key = this.stepList[this.step].key;
        this.form[key] = this.inputText;
        this.step += 1;
        if (this.stepMax < this.step)
            this.stepMax = this.step;
        this.inputText = '';
        this.focusText();
        if (this.stepMax + 1 == this.stepList.length) {
          this.onFinish();
        }
      },
      focusText: function () {
        let inputs = document.getElementsByTagName('input');
        inputs && inputs[0].focus();
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
        this.finish = false
        return this.$store.state.session.messages
      }
    },
    computed: {
      leftWidth: function () {
        let h = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
        return (h - 150) * 0.4 - 10;
      },
      inputType: function () {
        return this.stepList[this.step].type
      },
      checkLegal: function () {
          return function (index, checkFunc) {
            let d, c;
            if (this.step == index) {
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
        if (this.step + 1 == this.stepList.length)
            return true;
        let checkFunc = [
          input => {
            let w, b;
            b = input != '';
            if (!b)
              w = "学号不得为空";
            return [b, w];
          },
          input => {
            let w, b;
            b = input != '';
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
            b = input == this.form.password;
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

<style lang="sass" rel="stylesheet/sass">
  @import "../account"
</style>
