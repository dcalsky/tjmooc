<template>
  <div class="account-login">
    <div class="right">
      <div class="slice">
        <h1 class="title">
          <div>同济大学课程分享平台 (A版)</div>
          <div>{{time[0] - 1}}-{{time[0]}}学年第{{time[1]}}学期</div>
        </h1>
        <div class="form">
          <div v-for="(l, index) in list">
            <label>{{l.name}}
            <input v-if="l.type == 'number'" type="number" v-model="form[l.key]" :autofocus="{autofocus: !index}">
            <input v-if="l.type == 'text'" type="text" v-model="form[l.key]">
            <input v-if="l.type == 'password'" type="password" v-model="form[l.key]">
            </label>
          </div>
        </div>

        <div class="error" v-if="errorInfo">{{errorInfo}}</div>
        <div class="login" v-if="!errorInfo" @click="onLoginBtnClicked" :class="{submitting: submitting}">
          <span>登</span><span>录</span><span v-if="submitting">中</span><span v-if="submitting">…</span>
        </div>
      </div>
    </div>
    <div class="left" :style="{flexBasis: leftWidth + 'px'}">
      <h1 class="title"><router-link to="/account/register">注册</router-link>登录</h1>
    </div>
  </div>
</template>

<script>
  import request from 'superagent';
  import { server } from '../../../config'
  export default {
    name: "login",
    data: function () {
      return {
        list: [
          {
            name: "学号",
            key: "studentId",
            type: "number",
          },
          {
            name: "密码",
            key: "password",
            type: "password",
          },
        ],
        form: {
          studentId: "",
          password: "",
        },
        submitting: false
      }
    },
    methods: {
      onLoginBtnClicked: function () {
        if (this.submitting)
            return;
        console.log('logging...');
        console.log(this.form)
        this.submitting = true;
        // Ajax
        request
          .post(`${server.session}`)
          .set('Content-Type', 'application/json')
          .send({ username: this.form.studentId, password: this.form.password })
          .end(function(err, res){
            console.log(res)
            // Calling the end function will send the request
        });
      }
    },
    computed: {
      leftWidth: function () {
        let h = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
        return (h - 150) * 0.4 - 10;
      },
      time: function () {
        let d = new Date(), y = d.getFullYear(), m = d.getMonth() + 1, t = "一";
        if (m >= 9) ++y;
        if (2 <= m && m < 9) t = "二";
        return [y, t];
      },
      errorInfo: function () {
        if (this.form.studentId == '')
          return "请填写您的学号！";
        if (this.form.password == '')
          return "请填写您的密码！";
      }
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "../account"
</style>
