<template>
  <div id="manage-course" :style="{minHeight}">
    <div class="left">
      <h1 class="el-icon-arrow-left" @click="$router.push({ name: 'manage'})" data-text="课程管理" data-text-hover="返 回"></h1>
      <a ref='left' v-for="item in left" @click="item.click">
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
            :rules="courseRules"
            ref="courseForm"
          >
            <el-form-item label="课程图片" prop="cover_image">
              <el-upload
                :action="uploadTo"
                :on-success="onUploadSuccess"
                :show-file-list="false">
                <i v-if="courseForm.cover_image === 'uploading'" class="el-icon-loading"></i>
                <img v-else-if="courseForm.cover_image" :src="courseForm.cover_image">
                <i v-else class="el-icon-plus"></i>
                <div slot="tip" class="el-upload__tip">点击以上传或修改图片</div>
              </el-upload>
            </el-form-item>

            <el-form-item label="课程标题" prop="title">
              <el-input v-model="courseForm.title"></el-input>
            </el-form-item>
            <el-form-item label="课程副标题" prop="subtitle">
              <el-input v-model="courseForm.subtitle"></el-input>
            </el-form-item>
            <el-form-item label="课程描述" prop="introduction">
              <el-input v-model="courseForm.introduction"  type="textarea"
                        :autosize="{ minRows: 2, maxRows: 4}" resize="none"></el-input>
            </el-form-item>
            <el-form-item class="save">
              <el-button type="primary" @click="saveCourse">保存修改</el-button>
              <el-button plain type="primary" @click="removeCourse">删除课程</el-button>
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

              <div class="cards" v-if="searchFilter(chapters).length">
                <div class="cardBox" v-for="c in searchFilter(chapters)" @click="chapterCardClick(c)">
                  <el-card>
                    <span>{{c.title}}</span>
                    <i class="el-icon-edit"></i>
                  </el-card>
                </div>
              </div>
              <div class="none" v-else>暂无{{step}}</div>
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
            :rules="chapterRules"
            ref="chapterForm"
          >


            <el-form-item label="本章标题" prop="title">
              <el-input v-model="chapterForm.title"></el-input>
            </el-form-item>
            <el-form-item label="本章描述" prop="description">
              <el-input v-model="chapterForm.description" type="textarea"
                        :autosize="{ minRows: 1, maxRows: 4}" resize="none"></el-input>
            </el-form-item>
            <el-form-item class="save">
              <el-button type="primary" @click="saveChapter">保存修改</el-button>
              <el-button plain type="primary" @click="removeChapter">删除本章</el-button>
            </el-form-item>


            <div class="divide"></div>

            <el-form-item label="修改节">
              <el-input
                :placeholder="`输入${step}名称以筛选，或点击右侧按钮增加新一${step}`"
                class="filter"
                v-model="search"
                size="small">
                <el-button slot="append" icon="plus" @click="appendUnit"></el-button>
              </el-input>

              <div class="cards" v-if="searchFilter(units).length">
                <div class="cardBox" v-for="c in searchFilter(units)" @click="unitCardClick(c)">
                  <el-card>
                    <span>{{c.title}}</span>
                    <i class="el-icon-edit"></i>
                  </el-card>
                </div>
              </div>
              <div class="none" v-else>暂无{{step}}</div>
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
            :rules="unitRules"
            ref="unitForm"
          >
            <el-form-item label="本节标题" prop="title">
              <el-input v-model="unitForm.title"></el-input>
            </el-form-item>
            <el-form-item label="本节描述" prop="description">
              <el-input v-model="unitForm.description" type="textarea"
                        :autosize="{ minRows: 1, maxRows: 4}" resize="none"></el-input>
            </el-form-item>
            <el-form-item class="save">
              <el-button type="primary" @click="saveUnit">保存修改</el-button>
              <el-button plain type="primary" @click="removeUnit">删除本节</el-button>
            </el-form-item>

            <div class="divide"></div>

            <el-form-item label="修改视频">
              <el-upload
                :action="uploadTo"
                :on-success="onVideoUploadSuccess"
                :on-progress="onVideoUploadProgress"
                :on-remove="onVideoUploadRemove"
                :file-list="videos">
                <el-button size="small" type="primary" :disabled="uploading || unit.id < 0">点击上传</el-button>
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
  import FootBar from "../../components/footbar"
  import Navbar from "../../components/navbar/index.vue"
  import store from "./store"
  import {debounce} from "lodash"
  import { VueEditor } from 'vue2-editor'
  import {server} from '../../config'
  import urlJoin from 'url-join'

  export default {
    name: 'manage-course',
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
        return this.$store.state.manage.courses
      },
      chapters () {
        return this.$store.state.manage.chapters
      },
      units () {
        return this.$store.state.manage.units
      },
      videos () {
        return this.$store.state.manage.videos
      },
      course () {
        return this.$store.state.manage.course
      },
      chapter () {
        return this.$store.state.manage.chapter
      },
      unit () {
        return this.$store.state.manage.unit
      },
      homework () {
        return this.$store.state.manage.homework
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
        courseForm: {},
        chapterForm: {},
        unitForm: {},
        homeworkForm: {},
        uploadTo: server.upload,
        uploading: false,
        imgPreview: '',

        courseRules: {
          cover_image: [
            {required: true, message: '请上传封面图片', trigger: 'blur'},
          ],
          title: [
            {required: true, message: '请输入课程标题', trigger: 'blur'},
          ],
          subtitle: [
            {required: true, message: '请输入课程副标题', trigger: 'blur'},
          ],
          introduction: [
            {required: true, message: '请输入课程描述', trigger: 'blur'},
          ]
        },
        chapterRules: {
          title: [
            {required: true, message: '请输入章标题', trigger: 'blur'},
          ],
          description: [
            {required: true, message: '请输入章描述', trigger: 'blur'},
          ]
        },

        unitRules: {
          title: [
            {required: true, message: '请输入节标题', trigger: 'blur'},
          ],
          description: [
            {required: true, message: '请输入节描述', trigger: 'blur'},
          ]
        },
        minHeight: 0

      }
    },
    methods: {
      onUploadSuccess (res, file, fileList) {
        const t = res.startsWith('http') ? res : urlJoin(server.host, res)
        this.$set(this.courseForm, 'cover_image', t)
      },
      onVideoUploadProgress (event, file, fileList) {
//        this.$set(this.courseForm, 'cover_image', 'uploading')
        this.uploading = true
      },
      onVideoUploadSuccess (res, file, fileList) {
        this.uploading = false
        console.log(res, file, fileList)
        const t = res.startsWith('http') ? res : urlJoin(server.host, res)
        this.$store.dispatch('addVideo', {url: t, fileName: file.name, teacher: this.$store.state.session.userId})
      },
      onVideoUploadRemove (file, fileList) {
        this.uploading = false
        console.log(file, fileList)
        this.$store.dispatch('removeVideo', {fileName: file.name})
      },

      saveCourse () {
        this.$refs.courseForm.validate(valid => {
          if (valid) {
            const f = Object.assign({}, this.courseForm, {obligator: this.$store.state.session.userId})
            this.$store.dispatch('submitCourseForm', {
              courseForm: f,
              cb: () => {
                this.$refs.left[0].click()
              }
            })
          } else {
            return false
          }
        })
      },
      saveChapter () {
        this.$refs.chapterForm.validate(valid => {
          if (valid) {
            const f = Object.assign({}, this.chapterForm, {leacturer: this.$store.state.session.userId})
            this.$store.dispatch('submitChapterForm', {
              courseId: this.course.id,
              chapterForm: f,
              cb: () => {
                this.$refs.left[1].click()
              }
            })
          } else {
            return false
          }
        })
      },
      saveUnit () {
        this.$refs.unitForm.validate(valid => {
          if (valid) {
            const f = Object.assign({}, this.unitForm, {leacturer: this.$store.state.session.userId})
            this.$store.dispatch('submitUnitForm', {
              courseId: this.course.id,
              chapterId: this.chapter.id,
              unitForm: f,
              cb: () => {
                this.$refs.left[2].click()
              }
            })
          } else {
            return false
          }
        })
      },
      removeCourse () {
        this.$confirm(`此操作将永久删除课程 ${this.course.title}, 是否继续?`, '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$store.dispatch('removeCourse', {
            course: this.course,
            cb: () => {
              this.$refs.left[0].click()
            }
          })
        })
      },
      removeChapter () {
        this.$confirm(`此操作将永久删除章 ${this.chapter.title}, 是否继续?`, '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$store.dispatch('removeChapter', {
            courseId: this.course.id,
            chapterId: this.chapter.id,
            cb: () => {
              this.$refs.left[1].click()
            }
          })
        })
      },
      removeUnit () {
        this.$confirm(`此操作将永久删除节 ${this.unit.title}, 是否继续?`, '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.$store.dispatch('removeUnit', {
            courseId: this.course.id,
            chapterId: this.chapter.id,
            unitId: this.unit.id,
            cb: () => {
              this.$refs.left[2].click()
            }
          })
        })
      },

      courseCardClick(c) {
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
          },
        )
      },
      chapterCardClick(c) {
        c = c || this.$store.state.manage.chapters.slice(-1)[0]
        this.select[1] = c.id
        this.$store.dispatch('getChapter', c)
        this.select.push(-1)
        this.search = ''
        this.left.push({
          tag: '章信息',
          click: () => {
            this.$store.dispatch('getAllUnits', this.chapter)
            while (this.select.length > 2) this.select.pop()
            this.select.push(-1)
            this.search = ''
            this.$store.commit('clearUnit')
            this.left = this.left.slice(0, 3)
          }
        })
      },
      unitCardClick(c) {
        c = c || this.$store.state.manage.units.slice(-1)[0]
        this.select[2] = c.id
        this.$store.dispatch('getUnit', c)
        this.select.push(-1)
        this.search = ''
        this.left.push({
          tag: '节信息',
          click: () => {
//            while (this.select.length > 3) this.select.pop()
//            this.select.push(-1)
//            this.search = ''
//            this.left = this.left.slice(0, 4)

          }
        })
      },

      appendCourse() {
        this.courseForm = Object()
        this.$store.dispatch('appendBlankCourse')
        this.courseCardClick()
      },
      appendChapter() {
        this.chapterForm = Object()
        this.$store.dispatch('appendBlankChapter')
        this.chapterCardClick()
      },
      appendUnit() {
        this.unitForm = Object()
        this.$store.dispatch('appendBlankUnit')
        this.unitCardClick()
      },

      searchFilter(val, key='title') {
        val = val || [] // Ready for empty
        let l = val.filter(x => x[key].search(this.search) > -1)
        if (l.length === 0)
          l = val
        return l
      }
    },
    mounted () {
      this.$store.dispatch('getAllCourses')
      this.minHeight = window.innerHeight - 96 + 'px'
    }
  }
</script>
