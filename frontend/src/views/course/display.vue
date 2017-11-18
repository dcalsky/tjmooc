<template>
  <div id="course-display">
    <div class="left">
      <flv-video :alt="course.cover_image" :url="videoUrl" ></flv-video>


      <div class="info info-first" :class="{'info-hidden': showDetail}">
        <div class="content">
          <div class="title">{{course.title}}</div>
          <div class="subtitle">{{course.subtitle}}</div>
        </div>
        <div class="btn" @click="toggleDetail">
          <i class="fa fa-newspaper-o fa-2x"></i>
          <span>课程简介</span>
        </div>
      </div>

      <div class="info info-last" v-if="showDetail" @click="toggleDetail">
        <h3>{{course.title}}</h3>
        <p>{{course.introduction}}</p>

        <h3>{{chapter.title}}</h3>
        <p>{{chapter.description}}</p>

        <h3>{{unit.title}}</h3>
        <p>{{unit.description}}</p>
      </div>
    </div>
    <div class="tie">
      <div class="t1"></div>
      <div class="t2"></div>
    </div>
      <el-menu
        class="right"
        unique-opened
        @open="openMenu"
        @close="closeMenu"
      >
        <div class="btn" hidden>
          <i class="fa fa-folder-open-o fa-2x"></i>
          <span>选择课程</span>
        </div>
        <!--<el-submenu index="1">-->
          <!--<template slot="title">-->
            <!--<i class="el-icon-location"></i>-->
            <!--<span>导航一</span>-->
          <!--</template>-->
          <!--<el-menu-item-group>-->
            <!--<template slot="title">分组一</template>-->
            <!--<el-menu-item index="1-1">选项1</el-menu-item>-->
            <!--<el-menu-item index="1-2">选项2</el-menu-item>-->
          <!--</el-menu-item-group>-->
          <!--<el-menu-item-group title="分组2">-->
            <!--<el-menu-item index="1-3">选项3</el-menu-item>-->
          <!--</el-menu-item-group>-->
          <!--<el-submenu index="1-4">-->
            <!--<template slot="title">选项4</template>-->
            <!--<el-menu-item index="1-4-1">选项1</el-menu-item>-->
          <!--</el-submenu>-->
        <!--</el-submenu>-->

        <el-submenu v-for="c in course.chapters" :key="c.id" :index="`chapter-${c.id}`">
          <!--<i class="el-icon-menu"></i>-->
          <span slot="title">{{c.title}}</span>

          <div v-if="chapter.id === c.id">
            <el-submenu v-for="u in chapter.units" :index="`unit-${u.id}`" :key="u.id">
              <span slot="title">{{u.title}}</span>

              <div v-if="unit.id === u.id">
                <el-menu-item v-for="v in u.videos" :index="`video-${v.id}`" :key="v.id" @click="playVideo(v.url)">
                  <i class="fa fa-youtube-play"></i>{{/^(.+)\..+$/g.exec(v.title)[1]}}
                </el-menu-item>
                <div v-if="unit.videos.length === 0">
                  <el-menu-item-group title="本节暂无视频"></el-menu-item-group>
                </div>
              </div>
              <div v-else>
                <el-menu-item-group>
                  <template slot="title">
                    <i class="el-icon-loading"></i>
                    视频列表加载中
                  </template>
                </el-menu-item-group>
              </div>
            </el-submenu>
          </div>
          <div v-else>
            <el-menu-item v-for="u in c.units" :index="`unit-${u.id}`" :key="u.id">
              {{u.title}}
            </el-menu-item>
          </div>
          <div v-if="c.units.length === 0">
            <el-menu-item-group title="本章暂无内容"></el-menu-item-group>
          </div>
        </el-submenu>
      </el-menu>
      <!--<el-menu @open="onOpen" @select="onSelect" @close="onOpen" unique-opened>-->
        <!--<div v-for="chapter in chapters">-->

          <!--<el-submenu :index="`${chapter.id}`" v-if="chapter.units.length">-->
            <!--<template slot="title">{{chapter.title}}</template>-->

            <!--<div v-for="unit in chapter.units">-->
              <!--<el-submenu :index="`${chapter.id}-${unit.id}`" v-if="unit.lists && unit.lists.length">-->
                <!--<template slot="title">{{unit.title}}</template>-->
                <!--<el-menu-item :index="`${chapter.id}-${unit.id}-${item}`" v-for="item in unit.lists">-->
                  <!--{{getVideoNameByPath(chapter.id, unit.id, item)}}-->
                <!--</el-menu-item>-->
              <!--</el-submenu>-->

              <!--<el-menu-item :index="`${chapter.id}-${unit.id}`" v-else>{{unit.title}}</el-menu-item>-->
            <!--</div>-->
          <!--</el-submenu>-->

          <!--<el-menu-item :index="`${chapter.id}`" v-else>{{chapter.title}}</el-menu-item>-->

        <!--</div>-->
      <!--</el-menu>-->
  </div>
</template>

<script>
  import flvVideo from '../../components/flv-video/flv-video.vue'
  export default {
    name: 'course-display',
    components: {
      flvVideo
    },
    data () {
      return {
        showDetail: false,
        videoUrl: null
      }
    },
    computed: {
      course () {
        return this.$store.state.course.course
      },
      chapter () {
        return this.$store.state.course.chapter
      },
      unit () {
        return this.$store.state.course.unit
      }
    },
    methods: {
      toggleDetail () {
        this.showDetail = !this.showDetail
      },
      playVideo (url) {
        this.videoUrl = url
      },
      openMenu (key, keyPath) {
        console.log(key, keyPath)
        if (key.startsWith('chapter')) {
          const id = key.split('-').pop()
          this.$store.dispatch('getChapterById', {id})
        } else if (key.startsWith('unit')) {
          const id = key.split('-').pop()
          this.$store.dispatch('getUnitById', {id})
        }
      },
      closeMenu (key, keyPath) {
        console.log('close', key, keyPath)
        if (key.startsWith('chapter')) {
          this.$store.commit('GET_CHAPTER_SUCCESS', {})
        }
      }
    },
    created () {
      const id = this.$route.params.courseId
      this.$store.commit('clearMaterial')
      this.$store.commit('clearCourse')
      this.$store.dispatch('getCourseById', {id})
    }
  }
//    computed: {
//      // course data
//      course() {
//
//        let
//          sc = this.$store.state.course.course,
//          c = {
//            title: "加",
//            subtitle: "Loading...",
//            introduction: "加载中...",
//            cover_image: "",
//          };
//
//        if (sc.id) {
//          c.title = sc.title;
//          c.subtitle = sc.subtitle;
//          c.introduction = sc.introduction;
//          c.cover_image = sc.cover_image;
//
//          this.intro[0] = c.introduction
//        }
//
//        return c;
//      },
//      userId() {
//        return this.$store.state.session.userId;
//      },
//      token() {
//        return this.$store.state.session.token;
//      },
//      chapters() {
//        let c = this.$store.state.course.chapters;
//        if (c.length !== 0) {
//          console.log(c[0].id);
//          this.chapterId = c[0].id;
//        }
//        return Array.from(c);
//      },
//      flv() {
//        return {
//          type: 'mp4',
//          url: this.video.url,
//        };
//      },
//      videos() {
//        return this.$store.state.material.videos;
//      },
//      videosLen() {
//        return this.$store.state.material.videosLen;
//      },
//      video() {
//        return this.videos[this.path] || {
//          "id": 0,
//          "title": "",
//          "description": "",
//          "upload_time": "",
//          "url": "",
//          "teacher": ""
//        };
//      },
//      getVideoNameByPath() {
//        console.log('getVideoNameByPath')
//        return function (chapterId, unitId, videoId) {
//          const path = `${this.courseId}-${chapterId}-${unitId}-${videoId}`;
// //          console.log('path', path, this.videos);
//          return this.videos[path] && this.videos[path].title.slice(0, -4);
//        }
//      },
//    },
// //    watch: {
// //        '$store.state.material' : {
// //            handler (val) {
// //                console.log('store', val)
// //            },
// //          deep: true
// //        }
// //    },
//    methods: {
//      getChapterById(id) {
//        return this.chapters.find(x => x.id == id);
//      },
// //      getUnitById(chapterId, unitId) {
// //        let chapter = this.getChapterById(chapterId);
// //        return chapter.units.find(x => x.id == unitId);
// //      },
//      hasUnitsInfo(chapterId) {
//        let chapter = this.getChapterById(chapterId);
//        return chapter && chapter.units.length && typeof(chapter.units[0]) === 'object';
//      },
//
//      onSelect(key, keyPath) {
//        this.path = `${this.courseId}-${keyPath[keyPath.length - 1]}`;
//        this.pathLen = keyPath.length
//
//        if (keyPath.length === 1) {
//          // chapter
//          let chapterId = keyPath[0];
//          console.log(this.hasUnitsInfo(chapterId))
//          if (!this.hasUnitsInfo(chapterId)) {
//            this.$store.dispatch('getUnits', {courseId: this.courseId, chapterId: chapterId});
//          }
//          this.$store.dispatch('getHomework', {courseId: this.courseId, chapterId: chapterId})
//        }
//      },
//      onOpen(key, keyPath) {
//        this.pathLen = keyPath.length
//
//        if (keyPath.length === 1) {
//          // chapter
//          let chapterId = keyPath[0];
//          console.log(this.hasUnitsInfo(chapterId))
//          if (!this.hasUnitsInfo(chapterId)) {
//            this.$store.dispatch('getUnits', {courseId: this.courseId, chapterId: chapterId});
//          }
//          this.$store.dispatch('getHomework', {courseId: this.courseId, chapterId: chapterId})
//        }
//        if (keyPath.length === 2) {
//          // unit
//          const [chapterId, unitId] = keyPath[1].split('-')
//
//
//          this.$store.dispatch('getVideos', {
//            courseId: this.courseId,
//            chapterId: chapterId,
//            unitId: unitId
//          });
//        }
//      },
//      onInfoClicked() {
//        this.infoFront = !this.infoFront;
//      },
//    },
//    created() {
//      this.courseId = this.$route.params.courseId;
//      this.$store.dispatch('getCourseById', {courseId: this.courseId});
//      this.$store.dispatch('getChapters', {courseId: this.courseId});
//    }
//  }
</script>

<!--<style lang="sass" rel="stylesheet/sass">-->
  <!--@import "player"-->
<!--</style>-->
