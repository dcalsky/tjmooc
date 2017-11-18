<template>
<el-row :gutter="50" style="padding: 60px;">
  <el-col :md="8" :xs="24" :sm="12" v-for="(forum, i) in forums" :key="i" style="margin: 10px auto;">
    <el-card>
      <div style="padding: 14px;">
        <span>{{ forum.name }}</span>
        <div class="bottom clearfix">
          <time class="time">帖子数: {{ forum.posts_length }}</time>
          <el-button type="text" class="button" v-on:click="enterDetail(forum.id)">进入板块</el-button>
        </div>
      </div>
    </el-card>
  </el-col>
</el-row>

</template>

<script>
  export default {
    name: 'forum-list',
    created () {
      // Ajax to get data
      this.$store.dispatch('getForumList', this.$route.params.forumId)
    },
    computed: {
      forums () {
        return this.$store.state.forum.forums
      },
      hasNext () {
        return this.$store.state.forum.forumPage.next
      }
    },
    methods: {
      enterDetail (forumId) {
        this.$router.push({
          name: `forumDetail`,
          params: {forumId}
        })
      }
    }
  }
</script>


<style>
  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }
</style>
