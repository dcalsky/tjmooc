<template>
  <div id="floors">

    <el-row style="max-width: 900px; margin: 20px auto; padding: 50px 20px;">
      <div class="info">
        <h3 style="display: inline-block; padding-right: 10px;">{{ floor.title }}</h3>
        <p>{{ floor.content }}</p>
      </div>

      <el-col :span="24" v-for="(post, i) in posts" :key="i" style="margin: 0px auto;">
        <div class="post-item">
          <div style="padding: 8px;">
            <span>{{ post.content }}</span>
            <el-badge :value="post.floor" class="item"></el-badge>
            <!-- <el-button type="text" class="button" v-on:click="enterDetail(forum.id)">进入帖子</el-button> -->
          </div>
        </div>
      </el-col>

      <div class="reply">
        <textarea name="" id="" cols="30" rows="10" placeholder="尽情回复吧..." v-model="replyContent">

        </textarea>
        <el-button type="primary" id="submit" v-on:click="submit">发表回复</el-button>
      </div>
    </el-row>

  </div>

</template>

<script>
  export default {
    name: 'post-detail',
    created () {
      this.$store.dispatch('getFloorDetail', this.$route.params.floorId)
      this.$store.dispatch('getPostDetail', this.$route.params.floorId)
    },
    data () {
      return {
        replyContent: ''
      }
    },
    computed: {
      floor () {
        return this.$store.state.forum.currentFloor
      },
      posts () {
        return this.$store.state.forum.posts
      },
      hasNext () {
        return this.$store.state.forum.floorPage.next
      }
    },
    methods: {
      submit () {
        this.$store.dispatch('addPost', {floorId: this.$route.params.floorId, content: this.replyContent})
      },
      enterDetail (forumId) {
        this.$router.push({
          name: `floorDetail`,
          params: {forumId}
        })
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
  }
  .post-item {
    position: relative;
    padding: 15px;
    min-height: 100px;
    border: 1px solid #d1dbe5;
    border-radius: 2px;
    background-color: #fff;
    overflow: hidden;
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.12), 0 0 6px 0 rgba(0,0,0,.04);
  }
  .reply {
    position: relative;
    margin: 10px 0;
  }
  .reply textarea {
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
