<template>
  <div class="player">
    <div class="left">
      <flv-video :flv="flv" width="100%"></flv-video>
      <div class="info" :class="{flipper: !infoFront}">
        <div class="front">
          <div class="content">
            <div class="title">{{course.title}}</div>
            <div class="subtitle">{{course.subtitle}}</div>
          </div>
          <div class="btn" @click="onInfoClicked">
            <i class="fa fa-newspaper-o fa-2x"></i>
            <span>课程简介</span>
          </div>
        </div>
        <div class="back" @click="onInfoClicked">
          <div class="content">{{course.introduction}}</div>
        </div>
      </div>
    </div>
    <div class="tie">
      <div class="t1"></div>
      <div class="t2"></div>
    </div>
    <div class="right">
      <div hidden>{{videosLen}}{{videos}}</div>
      <el-menu @open="onOpen" @select="onSelect" @close="onOpen" unique-opened>
        <div v-for="chapter in chapters">

          <el-submenu :index="`${chapter.id}`" v-if="chapter.units.length">
            <template slot="title">{{chapter.title}}</template>

            <div v-for="unit in chapter.units">
              <el-submenu :index="`${chapter.id}-${unit.id}`" v-if="unit.lists && unit.lists.length">
                <template slot="title">{{unit.title}}</template>
                <el-menu-item :index="`${chapter.id}-${unit.id}-${item}`" v-for="item in unit.lists">
                  {{getVideoNameByPath(chapter.id, unit.id, item)}}
                </el-menu-item>
              </el-submenu>

              <el-menu-item :index="`${chapter.id}-${unit.id}`" v-else>{{unit.title}}</el-menu-item>
            </div>
          </el-submenu>

          <el-menu-item :index="`${chapter.id}`" v-else>{{chapter.title}}</el-menu-item>

        </div>
      </el-menu>
    </div>
  </div>
</template>

<script>
  import flvVideo from "../flv-video/flv-video.vue"
  export default {
    name: "player",
    components: {
      flvVideo
    },
    data() {
      return {
        infoFront: true,
        courseId: 0,

        path: '',
        refresh: true
      }
    },
    computed: {
      // course data
      course() {

        let
          sc = this.$store.state.course.course,
          c = {
            title: "加",
            subtitle: "Loading...",
            introduction: "加载中...",
            cover_image: "",
          };

        if (sc.id) {
          c.title = sc.title;
          c.subtitle = sc.subtitle;
          c.introduction = sc.introduction;
          c.cover_image = sc.cover_image;

//          console.log(c.sections);
//          let that = this;
//          if (c.sections.map)
//            c.sections = c.sections.map(s => {
//              return s;
//            });
        }

        return c;
      },
      userId() {
        return this.$store.state.session.userId;
      },
      token() {
        return this.$store.state.session.token;
      },
      chapters() {
        let c = this.$store.state.course.chapters;
        if (c.length !== 0) {
            console.log(c[0].id);
          this.chapterId = c[0].id;
        }
        return Array.from(c);
      },
      flv() {
        return {
          type: 'mp4',
          url: this.video.url,
        };
      },
      videos() {
          return this.$store.state.material.videos;
      },
      videosLen() {
          return this.$store.state.material.videosLen;
      },
      video() {
        return this.videos[this.path] || {
            "id": 0,
            "title": "",
            "description": "",
            "upload_time": "",
            "url": "",
            "teacher": ""
          };
      },
      getVideoNameByPath() {
          console.log('getVideoNameByPath')
        return function (chapterId, unitId, videoId) {
          const path = `${this.courseId}-${chapterId}-${unitId}-${videoId}`;
//          console.log('path', path, this.videos);
          return this.videos[path] && this.videos[path].title.slice(0, -4);
        }
      },
    },
//    watch: {
//        '$store.state.material' : {
//            handler (val) {
//                console.log('store', val)
//            },
//          deep: true
//        }
//    },
    methods: {
        getChapterById(id) {
            return this.chapters.find(x => x.id == id);
        },
      getUnitById(chapterId, unitId) {
            let chapter = this.getChapterById(chapterId);
            return chapter.units.find(x => x.id == unitId);
      },
      hasUnitsInfo(chapterId) {
        let chapter = this.getChapterById(chapterId);
        return chapter && chapter.units.length && typeof(chapter.units[0]) === 'object';
      },

      onSelect(key, keyPath) {
        this.path = `${this.courseId}-${keyPath[keyPath.length - 1]}`;

        if (keyPath.length === 1) {
          // chapter
          let chapterId = keyPath[0];
          console.log(this.hasUnitsInfo(chapterId))
          if (!this.hasUnitsInfo(chapterId)) {
            this.$store.dispatch('getUnits', {courseId: this.courseId, chapterId: chapterId});
          }
          this.$store.dispatch('getHomework', {courseId: this.courseId, chapterId: chapterId})
        }
      },
      onOpen(key, keyPath) {

        console.log(key, keyPath);
        if (keyPath.length === 1) {
          // chapter
          let chapterId = keyPath[0];
          console.log(this.hasUnitsInfo(chapterId))
          if (!this.hasUnitsInfo(chapterId)) {
            this.$store.dispatch('getUnits', {courseId: this.courseId, chapterId: chapterId});
          }
          this.$store.dispatch('getHomework', {courseId: this.courseId, chapterId: chapterId})
        }
        if (keyPath.length === 2) {
          // unit
          let
            [chapterId, unitId] = keyPath[1].split('-'),
            unit = this.getUnitById(chapterId, unitId);


          this.$store.dispatch('getVideos', {
            courseId: this.courseId,
            chapterId: chapterId,
            unitId: unitId
          });

          for (let i in unit.lists) {
            console.log(unit.lists[i]);
            let videoId = unit.lists[i];
//            if (!(`${this.courseId}-${chapterId}-${unitId}-${videoId}` in this.videos)) {
//              this.$store.dispatch('getVideo', {
//                courseId: this.courseId,
//                chapterId: chapterId,
//                unitId: unitId,
//                videoId: videoId
//              });
//            }
          }
        }
      },
      onInfoClicked() {
        this.infoFront = !this.infoFront;
      },
    },
    created() {

      // TODO: AJAX data
      this.courseId = this.$route.params.courseId;
      this.$store.dispatch('getCourseById', {courseId: this.courseId});
      this.$store.dispatch('getChapters', {courseId: this.courseId});
    },
    filters: {
        textLimit(s, max) {
            if (s.length <= max)
                return s;
            else
                return s.substr(0, max - 2) + ' …';
        }
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "player"
</style>
