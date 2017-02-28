<template>
  <div class="player">
    <div class="left">
      <flv-video :flv="flv" width="600px" height="400px"></flv-video>
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
          <div class="content">{{course.introduction.repeat(1)}}</div>
        </div>
      </div>
    </div>
    <div class="tie">
      <div class="t1"></div>
      <div class="t2"></div>
    </div>
    <div class="right">
      <div class="back">
        <div class="btn">
          <i class="fa fa-angle-left fa-2x"></i>
          <i class="fa fa-angle-double-left fa-2x"></i>
        </div>
        <div class="btn">
          <i class="fa fa-angle-right fa-2x"></i>
          <i class="fa fa-angle-double-right fa-2x"></i>
        </div>
      </div>
      <div class="section-next">
        <div class="tip" v-for="(n, i) in next">
          <div class="section">{{n.sections}}</div>
          <div class="title">{{n.title}}</div>
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
    props: {
      flv: {}
    },
    data() {
      return {
        infoFront: true,
        course: {
          title: "同济大学测试标题",
          subtitle: "这是测试专用的副标题",
          introduction: "古今中外大多数政治家都是逐步走向高层的。我曾任上海市长，接着又兼任了上海市委书记。\n事实上，我根本没想过自己会被调到北京的中央委员会工作，但最终我还是被选中了。等小邓小平和其他老一辈的领导集体希望我成为中国共产党的总书记，我实在是没有料到。然而毕竟我已经在这个位置上坐了11年了，我坚定不移的信仰一直告诉我必须尽最大的努力去为我的祖国服务。或许是因为我刻苦勤奋，所以我现在还能坐稳这个位子。",
          cover_image: "封面图",
          sections: "第一章"
        },
        next: []
      }
    },
    methods: {
        onInfoClicked() {
          this.infoFront = !this.infoFront;
        }
    },
    mounted() {
        // TODO: AJAX data
        for (let i = 0; i < 4; ++i) {
          let c = {
            title: "同济大学测试标题",
            subtitle: "这是测试专用的副标题",
            introduction: "古今中外大多数政治家都是逐步走向高层的。我曾任上海市长，接着又兼任了上海市委书记。\n事实上，我根本没想过自己会被调到北京的中央委员会工作，但最终我还是被选中了。等小邓小平和其他老一辈的领导集体希望我成为中国共产党的总书记，我实在是没有料到。然而毕竟我已经在这个位置上坐了11年了，我坚定不移的信仰一直告诉我必须尽最大的努力去为我的祖国服务。或许是因为我刻苦勤奋，所以我现在还能坐稳这个位子。",
            cover_image: "封面图",
            sections: "第一章"
          };
          c.sections = `第 ${i} 章`;
          this.next.push(c);
        }
    }
  }
</script>

<style lang="sass" rel="stylesheet/sass">
  @import "player"
</style>
