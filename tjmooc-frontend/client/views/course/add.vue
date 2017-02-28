<template>
  <div class="course-add">
    <h1>上传</h1>
    <div class="upload" v-for="t in row.input">
      <label :for="'add-' + t.id">{{t.name}}</label>
      <div class="input">
        <div v-if="post[t.id]">{{post[t.id]}}</div>
        <div v-if="!post[t.id]">待填写</div>
        <input type="text" :id="'add-' + t.id" v-model="post[t.id]">
      </div>
    </div>
    <div class="upload" v-for="t in row.p">
      <label :for="'add-' + t.id">{{t.name}}</label>
      <div class="input">
        <div v-if="post[t.id]">{{post[t.id]}}</div>
        <div v-if="!post[t.id]">待填写</div>
        <p :id="'add-' + t.id" v-model="post[t.id]">
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    components: {
    },
    data() {
      return {
        post: {
          title: '',
          subtitle: '',
          introduction: '',
          cover_image: '',
          sections: '',
        },
        row: {
            input: [
              {
                id: 'title',
                name: '视频标题'
              },
              {
                id: 'subtitle',
                name: '视频副标题'
              },
            ],
          p: [
            {
              id: 'introduction',
              name: '视频简介'
            }
          ]
        },
        video_uploaded: [
          {
            img: "img",
            title: "title",
            description: "",
            upload_time : "",
            id: ""
          }
        ]
      }
    }
  }
</script>

<style lang="scss">
  @import "add.scss";
</style>
