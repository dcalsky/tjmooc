<template>
  <div id="manage-afterclass" :style="{minHeight}">
    <div class="left">
      <h1 class="el-icon-arrow-left" @click="$router.push({ name: 'manage'})" data-text="课后管理" data-text-hover="返 回"></h1>
      <a ref='left' v-for="item in left" @click="item.click">
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
          <div class="cards" v-if="searchFilter(courses).length">
            <div v-for="c in searchFilter(courses)" @click="courseCardClick(c)" class="cardBox">
              <el-card :body-style="{ padding: '0px' }">
                <div class="img">
                  <img :src="c.cover_image" class="image">
                </div>
                <div class="detail">
                  <div class="title">{{c.title}}</div>
                  <div class="subtitle">{{c.subtitle}}</div>
                </div>
              </el-card>
            </div>
          </div>
          <div class="none" v-else style="margin-left: 10%;">暂无{{step}}</div>
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
            ref="homeworkForm"
            :rules="homeworkRules"
            :model="homeworkForm"
            label-width="80px"
            label-position="top"
          >
            <div v-if="false">
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

                  <template slot-scope="scope">
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


            <!--<el-form-item :label="`未提交 (${homework.unsubmit.length})`">-->
              <!--<el-table-->
                <!--class="unsubmit"-->
                <!--ref="singleTable"-->
                <!--:data="homework.unsubmit.slice(0, (homework.unsubmit.length + 1) / 2)"-->
                <!--:show-header="false">-->
                <!--<el-table-column-->
                  <!--property="id"-->
                  <!--label="学号"-->
                  <!--width="140">-->
                <!--</el-table-column>-->
                <!--<el-table-column-->
                  <!--property="name"-->
                  <!--label="姓名"-->
                  <!--width="140">-->
                <!--</el-table-column>-->
              <!--</el-table>-->

              <!--<el-table-->
                <!--class="unsubmit"-->
                <!--ref="singleTable"-->
                <!--:data="homework.unsubmit.slice((homework.unsubmit.length + 1) / 2)"-->
                <!--:show-header="false">-->
                <!--<el-table-column-->
                  <!--property="id"-->
                  <!--label="学号"-->
                  <!--width="140">-->
                <!--</el-table-column>-->
                <!--<el-table-column-->
                  <!--property="name"-->
                  <!--label="姓名"-->
                  <!--width="140">-->
                <!--</el-table-column>-->
              <!--</el-table>-->

            <!--</el-form-item>-->

            <div class="divide"></div>
            </div>

            <el-form-item label="作业标题" prop="title">
              <el-input v-model="homeworkForm.title"></el-input>
            </el-form-item>
            <el-form-item label="截止时间">
              <el-date-picker
              v-model="homeworkForm.deadline"
              type="datetime"
              placeholder="选择作业截止时间">
              </el-date-picker>
            </el-form-item>
            <el-form-item label="作业描述" prop="desc"></el-form-item>
              <vue-editor v-model="homeworkForm.desc" style="transform: translateY(-20px)"></vue-editor>

            <!--:editorToolbar="[-->
            <!--['bold', 'italic', 'underline'],-->
            <!--[{ 'list': 'ordered'}, { 'list': 'bullet' }],-->
            <!--['image', 'code-block', 'formula', 'code-block']-->
            <!--]"-->

            <el-form-item label="作业文件" prop="file">
              <el-upload
                :action="uploadTo"
                :on-success="onHomeworkFileUploadSuccess"
                :on-remove="onHomeworkFileUploadRemove">
                <el-button
                  size="small"
                  plain
                  type="primary"
                  v-if="!homeworkForm.file"
                >点击上传</el-button>
                <div v-else>作业文件仅能有一个，删除当前文件以替换</div>
              </el-upload>
            </el-form-item>

            <el-form-item class="save">
              <el-button type="primary" @click="saveHomework">保存修改</el-button>
            </el-form-item>
          </el-form>

        </div>

      </transition>

      <transition name="fade">
        <div id="test" v-if="select.length === 3 && select[2] === -2">

          <el-form
            :model="testForm"
            label-width="80px"
            label-position="top"
          >
            <el-form-item :label="`已提交 (${test.submitted.length})`">

              <el-table
                ref="singleTable"
                :data="test.submitted"
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
                  property="score"
                  label="测试成绩"
                  width="120">

                  <template slot-scope="scope">
                    {{scope.row.score}} 分
                  </template>
                </el-table-column>
              </el-table>

            </el-form-item>

            <div class="divide"></div>

            <el-form-item label="截止时间">
              <el-date-picker
                v-model="testForm.deadline"
                type="datetime"
                placeholder="选择作业截止时间">
              </el-date-picker>
            </el-form-item>

            <el-form-item :label="'测试题目' + (questionsForm.length ? '' : ' - 请添加测试题目')">
              <div v-if="questionsForm.length" style="margin-top: -20px;">
                <div ref='question' class="question" v-for="(q, i) in questionsForm">
                  <el-card
                    v-if="q.type === 'select'"
                  >
                    <div slot="header">
                      <el-button-group>
                        <el-button type="primary" size="small" icon="arrow-left" @click="questionUp(i)"></el-button>
                        <el-button type="primary" size="small" icon="close" @click="questionRemove(i)"></el-button>
                        <el-button type="primary" size="small" icon="arrow-right" @click="questionDown(i)"></el-button>
                      </el-button-group>
                    </div>

                    <div class="flex">
                      <span class="text">题干：</span>
                      <!--<el-input size="small" v-model="q.question"></el-input>-->
                      <click-input
                        size="small"
                        v-model="q.question"
                        style="margin-left: -10px;"
                        textarea
                      ></click-input>
                    </div>
                    <div class="flex">
                      <span class="text">选项：</span>
                      <div class="box">
                        <el-radio-group v-model="q.answer">
                          <el-radio :label="i" v-for="o, i in q.options" :key="q.id">
                            <click-input
                              size="small"
                              v-model="q.options[i]"
                              v-on:remove="q.options.splice(i, 1)"
                            ></click-input>
                          </el-radio>
                        </el-radio-group>
                        <el-button size="small" plain icon="plus" @click="addOption(i)">新建选项</el-button>
                      </div>
                    </div>
                    <div class="flex">
                      <span class="text">答案：</span>
                      <span>{{q.options[q.answer] || '请选择正确答案'}}</span>
                    </div>
                  </el-card>


                  <el-card
                    v-if="q.type === 'check'"
                  >
                    <div slot="header">
                      <el-button-group>
                        <el-button type="primary" size="small" icon="arrow-left" @click="questionUp(i)"></el-button>
                        <el-button type="primary" size="small" icon="close" @click="questionRemove(i)"></el-button>
                        <el-button type="primary" size="small" icon="arrow-right" @click="questionDown(i)"></el-button>
                      </el-button-group>
                    </div>

                    <div class="flex">
                      <span class="text">题干：</span>
                      <!--<el-input size="small" v-model="q.question"></el-input>-->
                      <click-input
                        size="small"
                        v-model="q.question"
                        style="margin-left: -10px;"
                        textarea
                      ></click-input>
                    </div>
                    <div class="flex">
                      <span class="text">选项：</span>
                      <div class="box">
                        <el-checkbox-group v-model="q.answer">
                          <el-checkbox :label="i" v-for="o, i in q.options" :key="q.id">
                            <click-input
                              size="small"
                              v-model="q.options[i]"
                              v-on:remove="q.options.splice(i, 1)"
                            ></click-input>
                          </el-checkbox>
                        </el-checkbox-group>
                        <el-button size="small" plain icon="plus" @click="addOption(i)">新建选项</el-button>
                      </div>
                    </div>
                    <div class="flex">
                      <span class="text">答案：</span>
                      <span v-if="q.answer.length === 0">请选择正确答案</span>
                      <span v-for="i in q.answer" :style="{order: i, marginRight: '10px'}">{{q.options[i]}}</span>
                    </div>
                  </el-card>

                  <el-card
                    v-if="q.type == 'blank'"
                  >
                    <div slot="header">
                      <el-button-group>
                        <el-button type="primary" size="small" icon="arrow-left" @click="questionUp(i)"></el-button>
                        <el-button type="primary" size="small" icon="close" @click="questionRemove(i)"></el-button>
                        <el-button type="primary" size="small" icon="arrow-right" @click="questionDown(i)"></el-button>
                      </el-button-group>
                    </div>

                    <div class="flex">
                      <span class="text">题干：</span>
                      <!--<el-input size="small" v-model="q.question"></el-input>-->
                      <click-input
                        size="small"
                        v-model="q.question"
                        style="margin-left: -10px;"
                        textarea
                      ></click-input>
                    </div>
                    <div class="flex">
                      <span class="text">答案：</span>
                      <click-input
                      size="small"
                      v-model="q.answer"
                      class="box"
                      textarea
                      style="margin-left: -10px;"
                    ></click-input>
                    </div>
                  </el-card>

                </div>
              </div>
              <div>
                <el-button type="primary" plain @click="addQuestion('select')">添加单选题</el-button>
                <el-button type="primary" plain @click="addQuestion('check')">添加多选题</el-button>
                <el-button type="primary" plain @click="addQuestion('blank')">添加填空题</el-button>
              </div>
            </el-form-item>


            <el-form-item class="save" style="margin-top: 50px;">
              <el-button type="primary">保存修改</el-button>
            </el-form-item>
          </el-form>
        </div>

      </transition>

    </div>
  </div>
</template>

<script>
  import FootBar from '../../components/footbar'
  import Navbar from '../../components/navbar/index.vue'
  import ClickInput from '../../components/click-input/click-input.vue'
  import store from './store'
//  import {debounce} from 'lodash'
  import { VueEditor } from 'vue2-editor'
  import {server} from '../../config'
  import urlJoin from 'url-join'

  export default {
    name: 'manage-afterclass',
    components: {
      ClickInput,
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
      homework: {
        deep: true,
        handler (val) {
          this.homeworkForm = Object.assign({}, this.homeworkForm, val)
        }
      },
      test: {
        deep: true,
        handler (val) {
          this.testForm = Object.assign({}, this.testForm, val)
        }
      },
      questions: {
        deep: true,
        handler (val) {
          this.questionsForm = [...val]
        }
      }
    },
    computed: {
      courses () {
        return this.$store.state.manage.courses
      },
      chapters () {
        return this.$store.state.manage.chapters
      },
      assistants () {
        return store.assistants
      },
      course () {
        return this.$store.state.manage.course
      },
      homework () {
        return this.$store.state.manage.homework
      },
      test () {
        return store.test
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
              this.$store.dispatch('getAllCourses')
              this.$store.commit('clearCourse')
              while (this.select.length) this.select.pop()
              this.select.push(-1)
              this.search = ''
              this.left = this.left.slice(0, 1)
            }
          }
        ],
        afterclass: 0,

        homeworkForm: {},
        testForm: {},
        questionsForm: [],
        uploadTo: server.upload,

        minHeight: 0,

        assistantVisible: false,
        assistantValue: '',

        homeworkRules: {
          title: [
            {required: true, message: '请输入作业标题', trigger: 'blur'}
          ],
          //          file: [
          //            {required: true, message: '请上传课程文件', trigger: 'blur'},
          //          ],
          desc: [
            {required: true, message: '请输入课程描述', trigger: 'blur'}
          ],
          ddl: [
            {type: 'date', required: true, message: '请选择作业提交截止时间', trigger: 'change'}
          ]
        }
      }
    },
    methods: {
      onHomeworkFileUploadSuccess (res, file, fileList) {
        this.uploading = false
        console.log(res, file, fileList)
        const t = res.startsWith('http') ? res : urlJoin(server.host, res)
        this.$set(this.homeworkForm, 'file', t)
        //        this.$store.dispatch('addVideo', {url: t, fileName: file.name, teacher: this.$store.state.session.userId})
      },
      onHomeworkFileUploadRemove (file, fileList) {
        this.$set(this.homeworkForm, 'file', '')
      },

      questionUp (i) {
        if (i > 0) {
          const p = this.$refs.question[i - 1]
          const q = this.$refs.question[i]
          const ph = p.getBoundingClientRect().height
          const qh = q.getBoundingClientRect().height
          q.setAttribute('style', `transform: translateY(-${ph + 20 + 'px'});transition: all .2s;`)
          p.setAttribute('style', `transform: translateY(${qh + 20 + 'px'});transition: all .2s;`)

          setTimeout(() => {
            p.removeAttribute('style')
            q.removeAttribute('style')
            const t = this.questionsForm[i - 1]
            this.$set(this.questionsForm, i - 1, this.questionsForm[i])
            this.$set(this.questionsForm, i, t)
          }, 200)
        }
      },
      questionDown (i) {
        if (i < this.questionsForm.length - 1) {
          const p = this.$refs.question[i]
          const q = this.$refs.question[i + 1]
          const ph = p.getBoundingClientRect().height
          const qh = q.getBoundingClientRect().height
          q.setAttribute('style', `transform: translateY(-${ph + 20 + 'px'});transition: all .2s;`)
          p.setAttribute('style', `transform: translateY(${qh + 20 + 'px'});transition: all .2s;`)

          setTimeout(() => {
            p.removeAttribute('style')
            q.removeAttribute('style')
            const t = this.questionsForm[i + 1]
            this.$set(this.questionsForm, i + 1, this.questionsForm[i])
            this.$set(this.questionsForm, i, t)
          }, 200)
        }
      },
      questionRemove (i) {
        const p = this.$refs.question[i]
        const ph = p.getBoundingClientRect().height
        const pw = p.getBoundingClientRect().width
        p.setAttribute('style', `transform: translateX(${pw / 2 + 'px'});opacity: 0;transition: all .2s;`)

        for (let t = i + 1; t < this.questionsForm.length; ++t) {
          const q = this.$refs.question[t]
          q.setAttribute('style', `transform: translateY(-${ph + 20 + 'px'});transition: all .2s;`)
        }
        setTimeout(() => {
          for (let t = i; t < this.questionsForm.length; ++t) {
            const q = this.$refs.question[t]
            q.removeAttribute('style')
          }
          this.questionsForm.splice(i, 1)
        }, 200)
      },

      courseCardClick (c) {
        c = c || this.$store.state.manage.courses.slice(-1)[0]
        this.select[0] = c.id
        this.$store.dispatch('getCourse', c)
        this.select.push(-1)
        this.search = ''
        this.left.push(
          {
            tag: '课程信息',
            click: () => {
              this.$store.dispatch('getAllChapters', this.course)
              while (this.select.length > 1) this.select.pop()
              this.select.push(-1)
              this.search = ''
              this.$store.commit('clearChapter')
              this.left = this.left.slice(0, 2)
            }
          }
        )
      },
      homeworkCardClick (c) {
        this.select[1] = c.id
        this.$store.dispatch('getHomework', c)
        this.chapter = c
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
      },
      testCardClick (c) {
        this.select[1] = c.id
        this.chapter = c
        this.select.push(-2)
        this.search = ''
        this.left.push({
          tag: '测试管理',
          click: () => {
            while (this.select.length > 2) this.select.pop()
            this.select.push(-2)
            this.search = ''
            store.clearChapter()
            this.left = this.left.slice(0, 3)
          }
        })
        store.getTest()
      },

      saveHomework () {
        this.$refs.homeworkForm.validate(valid => {
          if (valid) {
            const f = Object.assign({}, this.homeworkForm, {chapter: this.chapter.id})
            console.log(f)
            this.$store.dispatch('submitHomeworkForm', {
              homeworkForm: f,
              cb: () => {
                this.$refs.left[2].click()
              }
            })
          } else {
            return false
          }
        })
      },

      addQuestion (type) {
        const f = {
          select: () => {
            this.questionsForm.push({
              type,
              question: '',
              options: [],
              answer: -1
            })
          },

          check: () => {
            this.questionsForm.push({
              type,
              question: '',
              options: [],
              answer: []
            })
          },
          blank: () => {
            this.questionsForm.push({
              type,
              question: '',
              options: null,
              answer: ''
            })
          }
        }
        f[type] && f[type]()
      },
      addOption (index) {
        this.questionsForm[index].options.push('')
      },

      searchFilter (val, key = 'title') {
        val = val || [] // Ready for empty
        let l = val.filter(x => x[key].search(this.search) > -1)
        if (l.length === 0) {
          l = val
        }
        return l
      },

      handleClose (tag) {
        store.removeAssistant(tag)
      },

      showInput () {
        this.assistantVisible = true
        this.$nextTick(_ => {
          this.$refs.assistantSaveTagInput.$refs.input.focus()
        })
      },

      handleInputConfirm () {
        let assistantValue = this.assistantValue
        if (assistantValue) {
          store.appendAssistant(assistantValue)
        }
        this.assistantVisible = false
        this.assistantValue = ''
      },
      download (url) {
        console.log('download', url)
      }
    },
    mounted () {
      this.$store.dispatch('getAllCourses')
      this.minHeight = window.innerHeight - 96 + 'px'
    }
  }
</script>
