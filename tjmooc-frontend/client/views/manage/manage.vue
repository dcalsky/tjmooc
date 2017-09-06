<template>
  <div>
    <navbar></navbar>
    <div id="manage" :class="{selectCourse: !showList}">

      <div class="title" @click="clearSelect" :class="{btn: !showList}">
        <span v-if="!showList"><i class="el-icon-arrow-left"></i>全部课程</span>
        <span v-else>课程管理</span>
      </div>

      <transition name="fade">
        <div v-if="showList" :style="{ minHeight }">
          <div class="subtitle">
            <span>我管理的课程</span>
          </div>
          <div class="courses">
            <div
              class="course"
              :class="{selected: selected === index}"
              ref="course"
              @click="selectCourse(index)"
              v-for="course, index in courses">
              <img src="/slide/gll.jpg" alt="">
              <div>{{course.title}}</div>
            </div>
          </div>
        </div>
      </transition>
      <div v-if="!showList">
        <div class="detail">
          <div class="title">{{course.title}}</div>
          <div class="subtitle">{{course.subtitle}}</div>
        </div>

        <el-form
          ref="form"
          :model="form"
          label-width="80px"
          labelPosition="left"
          v-if="!showList">
          <el-form-item label="课程名称">
            <el-input v-model="form.title"></el-input>
          </el-form-item>
          <el-form-item label="课程简介">
            <el-input v-model="form.subtitle"></el-input>
          </el-form-item>
          <el-form-item label="课程描述">
            <el-input v-model="form.introduction"></el-input>
          </el-form-item>
          <el-form-item label="课程封面">
            <el-upload
              class="avatar-uploader"
              action="http://localhost:3000"
              :show-file-list="false"
              :on-success="handleAvatarSuccess">
              <img v-if="form.coverImage" :src="form.coverImage" class="avatar">
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
          </el-form-item>

          <!--<el-form-item label="活动区域">-->
            <!--<el-select v-model="form.region" placeholder="请选择活动区域">-->
              <!--<el-option label="区域一" value="shanghai"></el-option>-->
              <!--<el-option label="区域二" value="beijing"></el-option>-->
            <!--</el-select>-->
          <!--</el-form-item>-->
          <!--<el-form-item label="活动时间">-->
            <!--<el-col :span="11">-->
              <!--<el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>-->
            <!--</el-col>-->
            <!--<el-col class="line" :span="2">-</el-col>-->
            <!--<el-col :span="11">-->
              <!--<el-time-picker type="fixed-time" placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>-->
            <!--</el-col>-->
          <!--</el-form-item>-->
          <!--<el-form-item label="即时配送">-->
            <!--<el-switch on-text="" off-text="" v-model="form.delivery"></el-switch>-->
          <!--</el-form-item>-->
          <!--<el-form-item label="活动性质">-->
            <!--<el-checkbox-group v-model="form.type">-->
              <!--<el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>-->
              <!--<el-checkbox label="地推活动" name="type"></el-checkbox>-->
              <!--<el-checkbox label="线下主题活动" name="type"></el-checkbox>-->
              <!--<el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>-->
            <!--</el-checkbox-group>-->
          <!--</el-form-item>-->
          <!--<el-form-item label="特殊资源">-->
            <!--<el-radio-group v-model="form.resource">-->
              <!--<el-radio label="线上品牌商赞助"></el-radio>-->
              <!--<el-radio label="线下场地免费"></el-radio>-->
            <!--</el-radio-group>-->
          <!--</el-form-item>-->
          <!--<el-form-item label="活动形式">-->
            <!--<el-input type="textarea" v-model="form.desc"></el-input>-->
          <!--</el-form-item>-->
          <el-form-item>
            <el-button type="primary" @click="submit">保存更改</el-button>
          </el-form-item>
        </el-form>
      </div>

      <div class="course float" ref="float">
        <img src="/slide/gll.jpg" alt="">
        <!--<div>{{courses[selected]}}</div>-->
      </div>

    </div>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import footBar from "../../components/foot-bar/foot-bar.vue"
  import Navbar from "../../components/navbar/navbar.vue"
  import store from "./store"

  export default {
    name: 'manage',
    components: {
      footBar,
      Navbar,
    },
    computed: {
      courses () {
        return store.courses
      },
      course () {
          console.log(this.form, store.course)
        Object.assign(this.form, store.course)
        return store.course
      }
    },
    data () {
      return {
        selected: -1,
        showList: true,
        top: 0,
        left: 0,
        minHeight: 'auto',
        form: {
          title: '',
          subtitle: '',
          introduction: '',
          coverImage: ''
        }
      }
    },
    methods: {
      selectCourse (i) {
        this.selected = i
        this.toggle(true)
        setTimeout(this.toggleCourses, 0)
        store.getCourse(i)
      },
      clearSelect () {
        if (this.selected >= 0) {
          this.toggleCourses()
          this.toggle(false)
          setTimeout(() => {
            this.selected = -1
          }, 300)
        }
      },
      toggleCourses () {
        this.showList = !this.showList
      },
      toggle (show) {
        let f = this.$refs.float
        if (show) {
          const i = this.selected
          let r = this.$refs.course[i]
          let p = r.parentElement.parentElement.parentElement
          const style = window.getComputedStyle(r)
          const marginLeft = parseInt(style.getPropertyValue('margin-left'))
          const marginTop = parseInt(style.getPropertyValue('margin-top'))
          let top = r.getBoundingClientRect().top - p.getBoundingClientRect().top - marginTop + 'px'
          let left = r.getBoundingClientRect().left - p.getBoundingClientRect().left - marginLeft + 'px'

          this.top = top
          this.left = left
          console.log(top, left)

          f.setAttribute('style', `top: ${top}; left: ${left};`)
          setTimeout(() => {
            f.setAttribute('style', `top: 50px; left: 20px; opacity: 1; transition-duration: .3s`)
          }, 0)
        } else {
          f.setAttribute('style', `top: ${this.top}; left: ${this.left}; opacity: 1; transition-duration: .3s`)
          setTimeout(() => {
            f.removeAttribute('style')
          }, 300)
        }
      },
      submit () {
        store.update(this.selected, {
          title: this.form.title,
          subtitle: this.form.subtitle
        })
        this.$message.success(`课程 ${this.course.title} 修改成功`);
      },
      handleAvatarSuccess(res, file) {
        this.imageUrl = URL.createObjectURL(file.raw);
      }
    },
    mounted () {
      this.minHeight = window.innerHeight - 364 + 'px'
    }
  }
</script>

<style lang="scss">
  @import "manage";
</style>
