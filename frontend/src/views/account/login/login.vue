<template>
  <div id="account-login" @keyup.enter="onLoginBtnClicked">
    <div class="title">
      <div>同济大学课程分享平台 (A版)</div>
      <div>{{time[0] - 1}}-{{time[0]}}学年 第{{time[1]}}学期</div>
    </div>
    <div class="form">
      <div v-for="(l, index) in list">
        <label>
          <span>{{l.name}}</span>
          <input v-if="l.type == 'number'" type="number" v-model="form[l.key]" :autofocus="{autofocus: !index}">
          <input v-if="l.type == 'text'" type="text" v-model="form[l.key]">
          <input v-if="l.type == 'password'" type="password" v-model="form[l.key]">
        </label>
      </div>
    </div>

    <div class="bottom">
      <div class="error" v-if="messages.length > 0" @click="errorDisplayed = true">
        <div v-for="(message, index) in messages" >{{message}}</div>
      </div>
      <div class="btn-box">
        <div class="to" @click="toRegister">去注册</div>
        <div class="login" :class="{allowed: submitting || messages.length }" @click="onLoginBtnClicked">
          <span>登</span><span>录</span><span v-if="submitting">中</span><span v-if="submitting">…</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Search from '../../../components/search/search.vue'
  export default {
    name: 'login',
    beforeCreate () {
      // If has logged, return home page
      if (this.$store.state.session.token) {
        this.$router.replace({name: 'home'})
      }
    },
    components: {
      Search
    },
    data () {
      return {
        list: [
          {
            name: '学号',
            key: 'studentId',
            type: 'number'
          }, {
            name: '密码',
            key: 'password',
            type: 'password'
          }],
        form: {
          studentId: '',
          password: ''
        },
        submitting: false,
        errorDisplayed: false
      }
    },
    methods: {
      toRegister () {
        this.$router.push({name: 'register'})
      },
      onLoginBtnClicked: function () {
        if (this.submitting || this.messages.length) {
          return
        }
        console.log('logging...')
        this.submitting = true
        this.errorDisplayed = false
        // Ajax, login
        this.$store.dispatch('login', {username: this.form.studentId, password: this.form.password})
      }
    },
    computed: {
      time: function () {
        const d = new Date()
        let y = d.getFullYear()
        const m = d.getMonth() + 1
        let t = '一'
        if (m >= 9) { ++y }
        if (m >= 2 && m < 9) { t = '二' }
        return [y, t]
      },
      errorInfo: function () {
        if (this.form.studentId === '') {
          return '请填写您的学号！'
        }
        if (this.form.password === '') {
          return '请填写您的密码！'
        }
        return ''
      },
      messages () {
        this.submitting = false
        let m = []
        if (this.errorInfo) {
          m = m.concat(this.errorInfo)
        }
        if (!this.errorDisplayed) {
          setTimeout(() => { this.errorDisplayed = true }, 1000)
          m = m.concat(this.$store.state.session.messages)
        }
        return m
      }
    }
  }
</script>
