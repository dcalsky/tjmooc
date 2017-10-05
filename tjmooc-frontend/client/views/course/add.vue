<template>
  <div id="course-add">
    <h1>上传</h1>
    <div class="upload" v-for="t in row.input" :class="{filled: input[t.id]}">
      <label :for="'add-' + t.id">{{t.name}}</label>
      <div class="input">
        <div v-if="post[t.id]">{{post[t.id]}}</div>
        <div v-if="!post[t.id]">待填写</div>
        <input type="text" :id="'add-' + t.id" v-model="input[t.id]">
      </div>
    </div>
    <div class="upload" v-for="t in row.p" :class="{filled: input[t.id]}">
      <label :for="'add-' + t.id">{{t.name}}</label>
      <div class="input">
        <div v-if="input[t.id]">{{input[t.id]}}</div>
        <div v-if="!input[t.id]">待填写</div>
        <textarea :id="'add-' + t.id" v-model="input[t.id]" :rows="input[t.id] | getRows"></textarea>
      </div>
    </div>
    <div class="upload" :class="{filled: input.cover_image}">
      <label for="add-cover_image">上传封面图片</label>
      <div class="input">
        <div v-if="input.cover_image">
          <span style="padding-right: 12px;">当前上传</span>{{input.cover_image}}</div>
        <div v-if="!input.cover_image">待上传</div>
        <input type="file" id="add-cover_image" @change="changeImg">
      </div>
    </div>
    <div class="upload" :class="{filled: input.sections}">
      <label for="add-sections">上传章节</label>
      <div class="tip-box">
        <div class="scroll">
          <div class="tip" v-for="(section, index) in video_uploaded" @click="onTipClicked(index)" :class="{selected: section.id == input.sections}">
            <img :src="section.img" alt="">
            <h1>{{section.title}}</h1>
            <p>{{section.description}}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="btn" @click="submit" :class="{forbid: submitStatus.step == 1}">{{submitStatus.text}}</div>
  </div>
</template>

<script>
  export default {
    components: {},
    data() {
      return {
        input: {
          title: '',
          subtitle: '',
          introduction: '',
          cover_image: '',
          sections: '',
        },
        submitStatus: {
            text: "上 传",
          step: 0,
        },
        row: {
          input: [
            {
              id: 'title',
              name: '视频标题',
              limit: 30
            },
            {
              id: 'subtitle',
              name: '视频副标题',
              limit: 30
            },
          ],
          p: [
            {
              id: 'introduction',
              name: '视频简介',
              limit: 200
            }
          ]
        },
        video_uploaded: [
          {
            img: "slide/gdsx.jpg",
            title: "title1",
            description: "descdescdesc",
            upload_time: "",
            id: "id1"
          },
          {
            img: "slide/gdsx.jpg",
            title: "title2",
            description: "descdescdesc",
            upload_time: "",
            id: "id2"
          },
          {
            img: "slide/gdsx.jpg",
            title: "title3",
            description: "descdescdesc",
            upload_time: "",
            id: "id3"
          },
          {
            img: "slide/gdsx.jpg",
            title: "title4",
            description: "descdescdesc",
            upload_time: "",
            id: "id4"
          },
        ]
      }
    },
    filters: {
      getRows(s) {
        let ans = 0;
        for (let i in s) {
          if (s[i] === '\n')
            ++ans;
        }
        if (s.endsWith('\n'))
          return ans + 1;
        else
          return ans + 1;
      }
    },
    computed: {
      post() {
        for (let i in this.input) {
            let r = [], limit;
            for (let t in this.row)
                r = r.concat(this.row[t]);
            r = r.filter(x => x.id === i);
            if (r.length) {
              limit = r[0].limit;
              this.input[i] = this.input[i].substring(0, limit);
            }
        }
        return this.input;
      }
    },
    methods: {
        changeImg(e) {
            let f = e.target.files[0];
            console.log(f);
            this.input.cover_image = f.name;
        },
      onTipClicked(i) {
            this.input.sections = this.video_uploaded[i].id;
      },
      submit() {
            this.submitStatus = {
                text: "上传中",
              step: 1
            };
      }
    }
  }
</script>

<style lang="scss">
  @import "add.scss";
</style>
