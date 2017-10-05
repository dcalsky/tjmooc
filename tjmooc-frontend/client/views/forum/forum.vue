<template>
  <div id="forum">
    <navbar></navbar>
    <div class="wrapper">
      <div class="forum-header">
        <h2>板块一览</h2>
        <hr>
      </div>
      <ul class="content">
       <li class="plate" v-for="item in forums" @click="enterDetail(item.id)">
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
    created() {
      // Ajax to get data
      this.$store.dispatch('getForumList')
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
        this.$store.dispatch('getPostList', forumId)
      },
    }
  }
</script>

<style lang="scss">
  $lightColor: #dd5b82;

  #forum .wrapper {
    padding: 25px;
    background: #fafafa;
  }


  .forum-header {
    h2 {
      font-size: 3rem;
    }
  }

  .content {
    padding: 20px;
    min-height: 250px;
    list-style: none;
    .plate {
      position: relative;
      display: inline-block;
      box-sizing: border-box;
      box-shadow: 1px 2px 1px 1px rgba(0, 0, 0, .17);
      border-radius: 5px;
      border: 1px solid #f5f5f5;
      width: 30%;
      height: 120px;
      margin: 1.5%;
      cursor: pointer;
      transition: all .3s;
      @media (max-width: 768px) {
        width: 45%;
      }
      .plate-header {
        box-sizing: border-box;
        padding: 20px;
        font-size: 1.3rem;
        background: white;
        height: 100%;
      }
      .plate-footer {
        box-sizing: border-box;
        font-size: .8rem;
        position: absolute;
        bottom: 0;
        padding: 10px;
        height: 30px;
        width: 100%;
        background: #f5f5f5;
      }
    }
  }


  .plate:hover {
    box-shadow: 3px 4px 2px 1px rgba(0, 0, 0, .17);
  }

  .forum-next {
    width: 100%;
    margin: 30px 0;
    text-align: center;
    button {
      padding: 7.5px 15px;
      background: transparent;
      border: 1px solid $lightColor;
      color: $lightColor;
      font-size: 1.1rem;
      border-radius: 20px;
      width: 120px;
      cursor: pointer;
      transition: all .5s;
      &:hover {
        background: $lightColor;
        color: white;
      }
    }
  }

</style>
