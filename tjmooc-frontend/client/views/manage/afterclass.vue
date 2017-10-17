<template>
  <div id="manage-afterclass" :style="{minHeight}">
    <div class="left">
      <h1 class="el-icon-arrow-left" @click="$router.push({ name: 'manage'})" data-text="课后管理" data-text-hover="返 回"></h1>
      <a v-for="item in left" @click="item.click">
        {{item.tag}}
      </a>
    </div>
    <div class="right">
      <transition name="fade">
        <div id="courses" v-if="select.length === 1">
          <el-input
            :placeholder="`输入${step}名称以筛选`"
            icon="search"
            v-model="search"
            class="filter"
            size="small">
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

            <el-form-item label="助教" class="assistant">
              <el-tag
                :key="a"
                v-for="a in assistants"
                :closable="true"
                :close-transition="false"
                @close="handleClose(a)"
                type="gray"
              >
                {{a.id}} - {{a.name}}
              </el-tag>

              <el-input
                v-if="assistantVisible"
                v-model="assistantValue"
                ref="assistantSaveTagInput"
                size="mini"
                @keyup.enter.native="handleInputConfirm"
                @blur="handleInputConfirm"
              ></el-input>
              <el-button v-else size="mini" @click="showInput">+ 输入学工号以添加</el-button>

            </el-form-item>

            <div class="divide"></div>

            <el-form-item label="选择章" class="changeChapter">
              <el-input
                :placeholder="`输入${step}名称以筛选`"
                class="filter"
                v-model="search"
                size="small">
                <el-button slot="append" icon="plus" @click="appendChapter"></el-button>
              </el-input>

              <div class="cards">
                <div class="cardBox" v-for="c in searchFilter(chapters)">
                  <el-card :body-style="{ padding: '0px', background: 'currentColor' }">
                    <div slot="header" class="dark">
                      <div class="title">{{c.title}}</div>
                      <div class="subtitle">作业
                        <span v-if="1">已布置</span>
                        <span class="dim" v-else>未布置</span>
                        <span class="right">5/60</span>
                      </div>
                      <div class="subtitle">测试
                        <span v-if="0">10题</span>
                        <span class="dim" v-else>未布置</span>
                        <span class="right">5/60</span>
                      </div>
                    </div>
                    <el-button @click="homeworkCardClick(c)">查看作业</el-button>
                    <el-button @click="testCardClick(c)">查看测试</el-button>
                  </el-card>
                </div>
              </div>
            </el-form-item>
          </el-form>
        </div>
      </transition>


      <transition name="fade">
        <div id="homework" v-if="select.length === 3 && select[2] === -1">

          <el-form
            :model="homeworkForm"
            label-width="80px"
            label-position="top"
          >
            <el-form-item :label="`已提交 (${homework.submitted.length})`">

              <el-table
                ref="singleTable"
                :data="homework.submitted"
                style="width: 100%"
                :show-header="false">
                <el-table-column
                  property="id"
                  label="学号"
                  width="120">
                </el-table-column>
                <el-table-column
                  property="name"
                  label="姓名"
                  width="120">
                </el-table-column>
                <el-table-column
                  property="time"
                  label="提交时间">
                </el-table-column>
                <el-table-column
                  property="url"
                  label="提交作业"
                  width="120">

                  <template scope="scope">
                    <el-button
                      size="small"
                      @click="download(scope.row.url)">下载作业</el-button>
                  </template>
                </el-table-column>
              </el-table>

              <el-button
                type="primary"
                plain
                @click="download('all homework')"
                style="margin-top: 20px;"
              >下载全部作业</el-button>

            </el-form-item>


            <el-form-item :label="`未提交 (${homework.unsubmit.length})`">
              <el-table
                class="unsubmit"
                ref="singleTable"
                :data="homework.unsubmit.slice(0, (homework.unsubmit.length + 1) / 2)"
                :show-header="false">
                <el-table-column
                  property="id"
                  label="学号"
                  width="140">
                </el-table-column>
                <el-table-column
                  property="name"
                  label="姓名"
                  width="140">
                </el-table-column>
              </el-table>

              <el-table
                class="unsubmit"
                ref="singleTable"
                :data="homework.unsubmit.slice((homework.unsubmit.length + 1) / 2)"
                :show-header="false">
                <el-table-column
                  property="id"
                  label="学号"
                  width="140">
                </el-table-column>
                <el-table-column
                  property="name"
                  label="姓名"
                  width="140">
                </el-table-column>
              </el-table>

            </el-form-item>

            <div class="divide"></div>

            <el-form-item label="作业标题">
              <el-input v-model="homeworkForm.title"></el-input>
            </el-form-item>
            <el-form-item label="截止时间">
              <el-date-picker
              v-model="homeworkForm.deadline"
              type="datetime"
              placeholder="选择作业截止时间">
              </el-date-picker>
            </el-form-item>
            <el-form-item label="作业描述"></el-form-item>
              <vue-editor v-model="homeworkForm.introduction" style="transform: translateY(-20px)"></vue-editor>


            <!--:editorToolbar="[-->
            <!--['bold', 'italic', 'underline'],-->
            <!--[{ 'list': 'ordered'}, { 'list': 'bullet' }],-->
            <!--['image', 'code-block', 'formula', 'code-block']-->
            <!--]"-->

            <el-form-item class="save">
              <el-button type="primary">保存修改</el-button>
            </el-form-item>
          </el-form>

        </div>

      </transition>

      <transition name="fade">
        <div id="test" v-if="select.length === 3 && select[2] === -2">
          <el-form
            :model="homeworkForm"
            label-width="80px"
            label-position="top"
          >

            <el-form-item label="作业标题">
              <el-input v-model="homeworkForm.title"></el-input>
            </el-form-item>
            <el-form-item label="截止时间">
              <el-date-picker
                v-model="homeworkForm.deadline"
                type="datetime"
                placeholder="选择作业截止时间">
              </el-date-picker>
            </el-form-item>
            <el-form-item label="作业描述"></el-form-item>
            <vue-editor v-model="homeworkForm.introduction" style="transform: translateY(-20px)"></vue-editor>


            <!--:editorToolbar="[-->
            <!--['bold', 'italic', 'underline'],-->
            <!--[{ 'list': 'ordered'}, { 'list': 'bullet' }],-->
            <!--['image', 'code-block', 'formula', 'code-block']-->
            <!--]"-->

            <el-form-item class="save">
              <el-button type="primary">保存修改</el-button>
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
      assistants () {
        return store.assistants;
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
        const u = ['课程', '章']
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

        minHeight: 0,

        assistantVisible: false,
        assistantValue: ''


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
      homeworkCardClick(c) {
        this.select[1] = c.id
        store.getChapter(c.id)
        this.select.push(-1)
        this.search = ''
        this.left.push({
          tag: '作业管理',
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
      testCardClick(c) {
        this.select[1] = c.id
        store.getChapter(c.id)
        this.select.push(-2)
        this.search = ''
        this.left.push({
          tag: '测试管理',
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
      },


      handleClose(tag) {
        store.removeAssistant(tag)
      },

      showInput() {
        this.assistantVisible = true;
        this.$nextTick(_ => {
          this.$refs.assistantSaveTagInput.$refs.input.focus();
        });
      },

      handleInputConfirm() {
        let assistantValue = this.assistantValue;
        if (assistantValue) {
          store.appendAssistant(assistantValue)
        }
        this.assistantVisible = false;
        this.assistantValue = '';
      },
      download (url) {
        console.log('download', url)
      }
    },
    mounted () {
      this.minHeight = window.innerHeight - 96 + 'px'
    }
  }
</script>
