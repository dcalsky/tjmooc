<template>
  <div id="floors">

    <el-row style="max-width: 900px; margin: 20px auto; padding: 50px 20px;">
      <div class="info">
        <h3 style="display: inline-block; padding-right: 10px;">板块详情</h3>
        <el-button type="primary" v-on:click="sendPost">发帖</el-button>
      </div>

      <el-col :span="24" v-for="(floor, i) in floors" :key="i" style="margin: 0px auto;">
        <div class="floor-item">
          <div style="padding: 5px;">
            <span>{{ floor.title }}</span>
            <el-badge :value="12" class="item"></el-badge>
            <el-button type="text" class="button" v-on:click="enterDetail(floor.id, i)">进入帖子</el-button>
          </div>
        </div>
      </el-col>
      <div class="reply" v-show="replyShow">
        <input v-model="replyTitle" placeholder="帖子标题"/>
        <textarea name="" id="" cols="30" rows="10" placeholder="请输入内容..." v-model="replyContent">

        </textarea>
        <el-button type="primary" id="submit" v-on:click="submit">发布帖子</el-button>
      </div>
    </el-row>

  </div>

</template>

<script>
  export default {
    name: 'floor-list',
    created() {
      this.$store.dispatch('getFloorList', this.$route.params.forumId)
    },
    data() {
      return {
        replyShow: false,
        replyTitle: '',
        replyContent: ''
      }
    },
    computed: {
      floors() {
        return this.$store.state.forum.floors
      },
      hasNext() {
        return this.$store.state.forum.floorPage.next
      }
    },
    methods: {
      enterDetail(floorId, floorIndex) {
        this.$router.push({
          name: `postDetail`,
          params: { floorId, floorIndex }
        });
      },
      sendPost() {
        this.replyShow = !this.replyShow
      },
      submit() {
        this.$store.dispatch('addFloor', {forumId: this.$route.params.forumId, content: this.replyContent, title: this.replyTitle})
      }
    }
  }
</script>


<style>

  body {
    background: #fafbfc;
  }
  .info {
    margin-bottom: 10px;
  }
  .button {
    padding: 0;
    float: right;
  }
  .item {
    position: absolute;
    right: 5px;
    top: 10px;
    opacity: .65;
  }
  .floor-item {
    position: relative;
    padding: 15px;
    border: 1px solid #d1dbe5;
    border-radius: 2px;
    background-color: #fff;
    overflow: hidden;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.12), 0 0 6px 0 rgba(0,0,0,.04);
  }
  .reply {
    position: relative;
    float: left;
    width: 100%;
    margin: 30px 0;
  }
  .reply textarea, input {
    box-sizing: border-box;
    width: 100%;
    border: 1px solid #d1dbe5;
    border-radius: 2px;
    background-color: #fff;
    overflow: hidden;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.12), 0 0 6px 0 rgba(0,0,0,.04);
    padding: 10px;
  }

  .reply #submit {
    position: absolute;
    bottom: 30px;
    right: 15px;
  }

</style>
