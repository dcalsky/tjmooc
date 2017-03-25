<template>
  <div id="account-login">
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

        <div class="error" v-if="messages.length > 0">
          <p v-for="(message, index) in messages">{{message}}</p>
        </div>
        <div class="login" @click="onLoginBtnClicked" :class="{submitting: submitting}" v-if="messages.length == 0">
          <span>登</span><span>录</span><span v-if="submitting">中</span><span v-if="submitting">…</span>
        </div>
      </div>
    </div>
    <div class="left" :style="{flexBasis: leftWidth + 'px'}">
      <div>
        <h1 class="title">
          <router-link to="/account/register">注册</router-link>登录</h1>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "login",
    beforeCreate() {
      // If has logged, return home page
      if (this.$store.state.session.token) {
        this.$router.replace({ name: 'home' })
      }
    },
    data() {
      return {
        list: [
          {
            name: "学号",
            key: "studentId",
            type: "number",
          }, {
            name: "密码",
            key: "password",
            type: "password",
          }],
        form: {
          studentId: "",
          password: "",
        },
        submitting: false,
        errorDisplayed: false
      }
    },
    methods: {
      onLoginBtnClicked: function () {
        if (this.submitting)
          return;
        console.log('logging...');
        this.submitting = true;
        this.errorDisplayed = false;
        // Ajax, login
        this.$store.dispatch('login', { username: this.form.studentId, password: this.form.password })
      }
    },
    computed: {
      leftWidth: function () {
        let h = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
        return (h - 150) * 0.4 - 10;
      },
      time: function () {
        let d = new Date(), y = d.getFullYear(), m = d.getMonth() + 1, t = "一";
        if (m >= 9)++y;
        if (2 <= m && m < 9) t = "二";
        return [y, t];
      },
      errorInfo: function () {
        if (this.form.studentId == '')
          return "请填写您的学号！";
        if (this.form.password == '')
          return "请填写您的密码！";
        return "";
      },
      messages() {
        this.submitting = false;
        let m = new Array();
        if (this.errorInfo)
          m = m.concat(this.errorInfo);
        if (!this.errorDisplayed) {
          let that = this;
          setTimeout(() => that.errorDisplayed = true, 1000);
          m = m.concat(this.$store.state.session.messages);
        }
        return m;
      }
    }
  }
</script>
