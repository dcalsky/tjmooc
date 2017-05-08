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
      <div class="goto">
        <div class="select-box">
          <div class="select chapter" :class="{selected: selectChapter}" @click="onChapterTagSelected">章</div>
          <div class="select unit" :class="{selected: !selectChapter}" @click="onUnitTagSelected">节</div>
        </div>
        <div class="btn" @click="onLeftBtnClicked" :class="{forbid: !leftBtnAllowed}">
          <i class="fa fa-angle-left fa-2x"></i>
          <i class="fa fa-angle-double-left fa-2x"></i>
        </div>
        <div class="btn" @click="onRightBtnClicked" :class="{forbid: !rightBtnAllowed}">
          <i class="fa fa-angle-right fa-2x"></i>
          <i class="fa fa-angle-double-right fa-2x"></i>
        </div>
      </div>
      <div class="section-next">
        <div class="tip" v-for="(n, i) in chapters.slice(chaptersDisplayFrom, chaptersDisplayFrom + 4)" :class="{tipNow: n.id == chapterId}" v-if="selectChapter && chaptersDisplayFrom <= i && i < chaptersDisplayFrom + 4" @click="onChapterClicked(i)">
          <div class="title">{{n.title}}</div>
          <div class="desc">{{n.description | textLimit(60)}}</div>
        </div>
        <div class="tip" v-for="(n, i) in units.slice(unitsDisplayFrom, unitsDisplayFrom + 4)" v-if="!selectChapter" @click="onUnitClicked(i)">
          <div class="title">{{n.title}}</div>
          <div class="desc">{{n.description | textLimit(60)}}</div>
        </div>
      </div>
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
        flv: {
          type: 'mp4',
          url: 'http://ohp6g3bar.bkt.clouddn.com/job_IMG_1603.MOV',
        },

        infoFront: true,
        chaptersDisplayFrom: 0,
        selectChapter: true,
        unitsDisplayFrom: 0,

        courseId: 0,
        chapterId: 0,
        unitId: 0,
      }
    },
    computed: {

      leftBtnAllowed() {
        return (this.selectChapter ? this.chaptersDisplayFrom : this.unitsDisplayFrom) >= 4;
      },
      rightBtnAllowed() {
        if (this.selectChapter)
          return this.chaptersDisplayFrom < this.chapters.length - 4;
        else
          return this.unitsDisplayFrom < this.units.length - 4;
      },

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
      units() {
        let u = this.$store.state.course.units;
        return Array.from(u);
      }

    },
    methods: {
      onInfoClicked() {
        this.infoFront = !this.infoFront;
      },
      onLeftBtnClicked() {
        if (this.leftBtnAllowed) {
          if (this.selectChapter) {
            this.chaptersDisplayFrom -= 4;
          }
          else {
            this.unitsDisplayFrom -= 4;
          }
        }
      },
      onRightBtnClicked() {
        if (this.rightBtnAllowed) {
          if (this.selectChapter) {
            this.chaptersDisplayFrom += 4;
          }
          else {
            this.unitsDisplayFrom += 4;
          }
        }
      },
      onChapterTagSelected() {
        this.selectChapter = true;
      },
      onUnitTagSelected() {
        this.$store.dispatch('getUnits', {courseId: this.courseId, chapterId: this.chapterId});
        this.selectChapter = false;
      },

      onChapterClicked(i) {
        i += this.chaptersDisplayFrom;
        let c = this.chapters[i];
        console.log(c.id)
        console.log(i);
        this.chapterId = c.id;
        this.onUnitTagSelected();
        this.$store.dispatch('getHomework', {course: this.courseId, chapter: this.chapterId});
        if (this.userId)
          this.$store.dispatch('getHomeworkSubmit', {chapter: this.chapterId, user: this.userId});
      },
      onUnitClicked(i) {
          i += this.unitsDisplayFrom;
          console.log(i);
      }
    },
    created() {

      // TODO: AJAX data
      this.courseId = this.$route.params.courseId;
      this.$store.dispatch('getCourseById', {courseId: this.courseId});
      this.$store.dispatch('getChapters', {courseId: this.courseId});
//      for (let i = 0; i < 10; ++i) {
//        let c = {
//          title: "同济大学测试标题",
//          subtitle: "这是测试专用的副标题",
//          introduction: "古今中外大多数政治家都是逐步走向高层的。我曾任上海市长，接着又兼任了上海市委书记。\n事实上，我根本没想过自己会被调到北京的中央委员会工作，但最终我还是被选中了。等小邓小平和其他老一辈的领导集体希望我成为中国共产党的总书记，我实在是没有料到。然而毕竟我已经在这个位置上坐了11年了，我坚定不移的信仰一直告诉我必须尽最大的努力去为我的祖国服务。或许是因为我刻苦勤奋，所以我现在还能坐稳这个位子。",
//          cover_image: "封面图",
//        };
//        c.title = `第 ${i} 章`;
//        this.chapters.push(c);
//      }
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
