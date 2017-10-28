<template>
  <div id="player">
    <div class="left">
      <flv-video :url="course.cover_image"></flv-video>
      <transition name="fade">
        <div class="info info-last" v-if="showDetail">
          <h3>{{course.title}}</h3>
          <p>{{course.introduction}}</p>
        </div>
      </transition>
      <div class="info info-first">
        <div class="content">
          <div class="title">{{course.title}}</div>
          <div class="subtitle">{{course.subtitle}}</div>
        </div>
        <div class="btn" @click="toggleDetail">
          <i class="fa fa-newspaper-o fa-2x"></i>
          <span>课程简介</span>
        </div>
      </div>
    </div>
    <div class="tie">
      <div class="t1"></div>
      <div class="t2"></div>
    </div>
      <el-menu
        class="right"
        unique-opened
        @open="handleOpen"
        @close="handleClose">
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

        <div v-for="chapter in course.chapters" :key="chapter.id">
          <el-menu-item :index="chapter.id">
            <!--<i class="el-icon-menu"></i>-->
            <span slot="title">{{chapter.title}}</span>
          </el-menu-item>
        </div>
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
  import flvVideo from '../../../components/flv-video/flv-video.vue'
  export default {
    name: 'player',
    components: {
      flvVideo
    },
    data () {
      return {
        showDetail: false
      }
    },
    computed: {
      course () {
        return this.$store.state.course.course
      }
    },
    methods: {
      toggleDetail () {
        this.showDetail = !this.showDetail
      }
    },
    created () {
      const courseId = this.$route.params.courseId
      this.$store.dispatch('getCourseById', {courseId})
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
