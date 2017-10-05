<template>
  <div id="manage-course" :style="{minHeight}">
    <div class="left">
      <h1 class="el-icon-arrow-left" @click="$router.push({ name: 'manage'})" data-text="课程管理" data-text-hover="返 回"></h1>
      <a v-for="item in left" @click="item.click">
        {{item.tag}}
      </a>
    </div>
    <div class="right">
      <transition name="fade">
        <div id="courses" v-if="select.length === 1">
        <el-input
          :placeholder="`输入${step}名称以筛选，或点击右侧按钮增加新${step}`"
          class="filter"
          v-model="search"
          size="small">
          <el-button slot="append" icon="plus" @click="appendCourse"></el-button>
        </el-input>
          <div class="cards">
            <div v-for="c in searchFilter(courses)" @click="courseCardClick(c)" class="cardBox">
              <el-card :body-style="{ padding: '0px' }">
                <div class="img">
                  <img :src="c.img" class="image">
                </div>
                <div class="detail">
                  <div class="title">{{c.title}}</div>
                  <div class="subtitle">{{c.subtitle}}</div>
                </div>
              </el-card>
            </div>
          </div>
        </div>
      </transition>

      <transition name="fade">
        <div id="course" v-if="select.length === 2">

          <el-form
            :model="courseForm"
            label-width="80px"
            label-position="top"
          >
            <el-form-item label="课程图片">
              <el-upload
                action="https://jsonplaceholder.typicode.com/posts/"
                :show-file-list="false">
                <img v-if="courseForm.coverImage" :src="courseForm.coverImage" class="avatar">
                <i v-else class="el-icon-plus"></i>
                <div slot="tip" class="el-upload__tip">点击以上传或修改图片</div>
              </el-upload>
            </el-form-item>

            <el-form-item label="课程标题">
              <el-input v-model="courseForm.title"></el-input>
            </el-form-item>
            <el-form-item label="课程描述">
              <el-input v-model="courseForm.subtitle"  type="textarea"
                        :autosize="{ minRows: 1, maxRows: 4}" resize="none"></el-input>
            </el-form-item>
            <el-form-item class="save">
              <el-button type="primary">保存修改</el-button>
            </el-form-item>

            <div class="divide"></div>

            <el-form-item label="修改章" class="changeChapter">
              <el-input
                :placeholder="`输入${step}名称以筛选，或点击右侧按钮增加新一${step}`"
                class="filter"
                v-model="search"
                size="small">
                <el-button slot="append" icon="plus" @click="appendChapter"></el-button>
              </el-input>

              <div class="cards">
                <div class="cardBox" v-for="c in searchFilter(chapters)" @click="chapterCardClick(c)">
                  <el-card>
                    <span>{{c.title}}</span>
                    <i class="el-icon-edit"></i>
                  </el-card>
                </div>
              </div>
            </el-form-item>
          </el-form>
        </div>
      </transition>


      <transition name="fade">
        <div id="chapter" v-if="select.length === 3">
          <el-form
            :model="chapterForm"
            label-width="80px"
            label-position="top"
          >

            <!--<el-radio-group v-model="afterclass" style="margin: 27px 0 50px 0">-->
              <!--<el-radio-button label="0">修改信息</el-radio-button>-->
              <!--<el-radio-button label="1">课后练习</el-radio-button>-->
            <!--</el-radio-group>-->

            <el-form-item label="本章标题">
              <el-input v-model="chapterForm.title"></el-input>
            </el-form-item>
            <el-form-item label="本章描述">
              <el-input v-model="chapterForm.subtitle"  type="textarea"
                        :autosize="{ minRows: 1, maxRows: 4}" resize="none"></el-input>
            </el-form-item>
            <el-form-item class="save">
              <el-button type="primary">保存修改</el-button>
            </el-form-item>

            <!--<transition name="fader">-->
            <!--<div class="divide" v-if="afterclass"></div>-->
            <!--</transition>-->

            <!--<el-form-item label="课后练习" style="margin: 40px 0">-->
              <!--<el-button :plain="afterclass !== 1" type="primary" @click="afterclass = (afterclass === 1 ? 0 : 1)">布置作业</el-button>-->
              <!--<el-button :plain="afterclass !== 2" type="primary" @click="afterclass = (afterclass === 2 ? 0 : 2)">布置测试</el-button>-->
            <!--</el-form-item>-->

            <!--<transition name="fader">-->
              <!--<div v-if="afterclass === 1">-->
                <!--<el-form-item label="作业标题">-->
                  <!--<el-input v-model="homeworkForm.title"></el-input>-->
                <!--</el-form-item>-->
                <!--<el-form-item label="截止时间">-->
                  <!--<el-date-picker-->
                    <!--v-model="homeworkForm.deadline"-->
                    <!--type="datetime"-->
                    <!--placeholder="选择作业截止时间">-->
                  <!--</el-date-picker>-->
                <!--</el-form-item>-->
                <!--<el-form-item label="作业描述"></el-form-item>-->
                  <!--<vue-editor v-model="homeworkForm.introduction" style="transform: translateY(-20px)"></vue-editor>-->


                <!--&lt;!&ndash;:editorToolbar="[&ndash;&gt;-->
                <!--&lt;!&ndash;['bold', 'italic', 'underline'],&ndash;&gt;-->
                <!--&lt;!&ndash;[{ 'list': 'ordered'}, { 'list': 'bullet' }],&ndash;&gt;-->
                <!--&lt;!&ndash;['image', 'code-block', 'formula', 'code-block']&ndash;&gt;-->
                <!--&lt;!&ndash;]"&ndash;&gt;-->



                <!--<el-form-item class="save">-->
                  <!--<el-button type="primary">保存修改</el-button>-->
                <!--</el-form-item>-->
              <!--</div>-->
            <!--</transition>-->


            <div class="divide"></div>

            <el-form-item label="修改节">
              <el-input
                :placeholder="`输入${step}名称以筛选，或点击右侧按钮增加新一${step}`"
                class="filter"
                v-model="search"
                size="small">
                <el-button slot="append" icon="plus" @click="appendUnit"></el-button>
              </el-input>

              <div class="cards">
                <div class="cardBox" v-for="c in searchFilter(units)" @click="unitCardClick(c)">
                  <el-card>
                    <span>{{c.title}}</span>
                    <i class="el-icon-edit"></i>
                  </el-card>
                </div>
              </div>
            </el-form-item>
          </el-form>
        </div>
      </transition>


      <transition name="fade">
        <div id="unit" v-if="select.length === 4">

          <el-form
            :model="unitForm"
            label-width="80px"
            label-position="top"
          >
            <el-form-item label="本节标题">
              <el-input v-model="unitForm.title"></el-input>
            </el-form-item>
            <el-form-item label="本节描述">
              <el-input v-model="unitForm.subtitle"  type="textarea"
                        :autosize="{ minRows: 1, maxRows: 4}" resize="none"></el-input>
            </el-form-item>
            <el-form-item class="save">
              <el-button type="primary" style="margin-top: 10px">保存修改</el-button>
            </el-form-item>

            <div class="divide"></div>

            <el-form-item label="修改视频">
              <el-upload
                class="upload-demo"
                action="https://jsonplaceholder.typicode.com/posts/"
                :on-change="function() {}"
                :file-list="videos">
                <el-button size="small" type="primary">点击上传</el-button>
                <div slot="tip" class="el-upload__tip">只能上传flv格式视频，且文件名将作为这段视频的名称</div>
              </el-upload>


            </el-form-item>
          </el-form>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
  import FootBar from "../../components/foot-bar/foot-bar.vue"
  import Navbar from "../../components/navbar/navbar.vue"
  import store from "./store"
  import {debounce} from "lodash"
  import { VueEditor } from 'vue2-editor'

  export default {
    name: 'manage',
    components: {
      FootBar,
      Navbar,
      VueEditor
    },
    watch: {
      course: {
        deep: true,
        handler (val) {
          this.courseForm = Object.assign({}, this.courseForm, val)
        }
      },
      chapter: {
        deep: true,
        handler (val) {
          this.chapterForm = Object.assign({}, this.chapterForm, val)
        }
      },
      unit: {
        deep: true,
        handler (val) {
          this.unitForm = Object.assign({}, this.unitForm, val)
        }
      },
      homework: {
        deep: true,
        handler (val) {
          this.homeworkForm = Object.assign({}, this.homeworkForm, val)
        }
      }
    },
    computed: {
      courses () {
        return store.courses
      },
      chapters () {
        return store.chapters
      },
      units () {
        return store.units
      },
      videos () {
        return store.videos
      },
      course () {
        return store.course
      },
      chapter () {
        return store.chapter
      },
      unit () {
        return store.unit
      },
      homework () {
        return store.homework
      },
      filterCourses () {
        return this.courses.filter(x => x.title.search(this.search) > -1)
      },
      courseSelect () {
        let f = this.courses.filter(x => x.id === this.select[0])
        return f.length > 0 ? f[0] : null
      },
      step () {
        const u = ['课程', '章', '节', '视频']
        return u[this.select.length - 1]
      }
    },
    data () {
      return {
        select: [-1],
        search: '',
        left: [
          {
            tag: '全部课程',
            click: () => {
              while (this.select.length) this.select.pop()
              this.select.push(-1)
              this.search = ''
              store.clearChapter()
              this.left = this.left.slice(0, 1)
            }
          }
        ],
        afterclass: 0,
        courseForm: {},
        chapterForm: {},
        unitForm: {},

        homeworkForm: {},


        minHeight: 0

      }
    },
    methods: {
      courseCardClick(c) {
        this.select[0] = c.id
        store.getCourse(c.id)
        this.select.push(-1)
        this.search = ''
        this.left.push(
          {
            tag: '课程信息',
            click: () => {
              while (this.select.length > 1) this.select.pop()
              this.select.push(-1)
              this.search = ''
              store.clearChapter()
              this.left = this.left.slice(0, 2)
            }
          },
        )
      },
      chapterCardClick(c) {
        this.select[1] = c.id
        store.getChapter(c.id)
        this.select.push(-1)
        this.search = ''
        this.left.push({
          tag: '章信息',
          click: () => {
            while (this.select.length > 2) this.select.pop()
            this.select.push(-1)
            this.search = ''
            store.clearChapter()
            this.left = this.left.slice(0, 3)
          }
        })

        store.getHomework()
      },
      unitCardClick(c) {
        this.select[2] = c.id
        store.getUnit(c.id)
        this.select.push(-1)
        this.search = ''
        this.left.push({
          tag: '节信息',
          click: () => {
            while (this.select.length > 3) this.select.pop()
            this.select.push(-1)
            this.search = ''
            store.clearChapter()
            this.left = this.left.slice(0, 4)

          }
        })
      },

      appendCourse() {
//        store.appendCourse()
      },
      appendChapter() {
        store.appendChapter()
      },
      appendUnit() {
        store.appendUnit()
      },

      searchFilter(val, key='title') {
        let l = val.filter(x => x[key].search(this.search) > -1)
        if (l.length === 0)
          l = val
        return l
      }
    },
    mounted () {
      this.minHeight = window.innerHeight - 96 + 'px'
    }
  }
</script>
