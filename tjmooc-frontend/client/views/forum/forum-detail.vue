<template>
  <div class="forum-detail">
      <div class="forum-header">
        <h2>板块一览</h2>
        <hr>
      </div>
    <div class="class">

    </div>
  </div>
</template>

<script>
  export default {
    name: 'forum-detail',
    created() {
      // Ajax to get data
      this.$store.dispatch('getPostList', this.$route.params.forumId)
    },
    computed: {
      forums() {
        return this.$store.state.forum.forums
      },
      hasNext() {
        return this.$store.state.forum.forumPage.next
      }
    },
    methods: {
      enterDetail(forumId) {
        this.$router.push({
          name: `forumDetail`,
          params: { forumId }
        });
      },
    }
  }
</script>

<style lang="scss">
</style>
