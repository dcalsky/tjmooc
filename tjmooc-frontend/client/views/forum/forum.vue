<template>
  <div id="forum">
    <navbar></navbar>
    <div class="wrapper">
      <div class="forum-header">
        <h2>板块一览</h2>
        <hr>
      </div>
      <ul class="content">
       <li class="plate" v-for="item in forums">
        <div class="plate-header">
          {{ item.name }}
        </div>
        <div class="plate-footer">
          所属课程: {{ item.course }}
        </div>
       </li>
      </ul>
      <div v-if="hasNext" class="forum-next">
        <button >下一页</button>
      </div>
    </div>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import footBar from "../../components/foot-bar/foot-bar.vue"
  import Navbar from "../../components/navbar/navbar.vue"
  export default {
    name: 'forum',
    components: {
      footBar,
      Navbar,
    },
    beforeCreate() {
      // Ajax to get data
      this.$store.dispatch('getForumList')
    },
    computed: {
      forums() {
        console.log(this.$store.state.forum.forums)
        return this.$store.state.forum.forums
      },
      hasNext() {
        return this.$store.state.forum.forum_page.next
      }
    }
  }
</script>

<style lang="scss">
@import "forum.scss"
</style>
