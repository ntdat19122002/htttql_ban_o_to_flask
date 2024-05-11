<template>
  <div class="information">
    <div class="action">
      <div class="action-item">Extract words</div>
      <div class="action-item">Extract features</div>
      <div class="action-item" @click="getAudioList()">Get audio list</div>
      <div class="action-item" @click="removeAllAudioInformation()">
        Delete all
      </div>
    </div>
    <div class="information-table">
      <Table :columns="columns" :data-source="audio_data">
        <template #headerCell="{ column }">
          <template v-if="column.key === 'name'">
            <span> Name </span>
          </template>
        </template>

        <template #bodyCell="{ index, column, record }">
          <template v-if="column.key === 'index'">
            <div>
              {{ index + 1 }}
            </div>
          </template>
          <template v-if="column.key === 'name'">
            <a>
              {{ limitTextLength(record.name, 20) }}
            </a>
          </template>
          <template v-if="column.key === 'content'">
            {{ limitTextLength(record.content, 300) }}
          </template>
          <template v-else-if="column.key === 'action'">
            <div class="detail-action">
              <div
                class="detail-action-item"
                @click="extractContentAudio(record.id)"
              >
                Extract words
              </div>
              <div class="detail-action-item remove-button">X</div>
            </div>
          </template>
        </template>
      </Table>
    </div>
  </div>
</template>

<script>
import { Table } from "ant-design-vue";
import axios from "axios";
export default {
  components: { Table },
  data() {
    return {
      audio_data: [],
      columns: [
        {
          name: "Index",
          dataIndex: "index",
          key: "index",
        },
        {
          name: "Name",
          dataIndex: "name",
          key: "name",
        },
        {
          title: "Content",
          dataIndex: "content",
          key: "content",
        },
        {
          title: "Action",
          key: "action",
        },
      ],
    };
  },
  methods: {
    limitTextLength(text, length) {
      if (text.length >= length) {
        return `${text.slice(0, length)}...`;
      }
      return text;
    },
    extractContentAudio(id) {
      axios
        .post("http://127.0.0.1:5000/information/extract_content_audio",{
            id:id
        })
        .then((res) => {
            console.log(res.data);
            let recordIndex = this.audio_data.findIndex(e => e.id == id)
            console.log(recordIndex);
            this.audio_data[recordIndex].content = res.data.content;
        })
        .catch((e) => console.log(e));
    },
    getAudioList() {
      axios
        .get("http://127.0.0.1:5000/information/get_audio_list")
        .then((res) => {
          this.audio_data = res.data;
        })
        .catch((e) => console.log(e));
    },
    removeAllAudioInformation() {
      axios
        .get("http://127.0.0.1:5000/information/remove_all_audio_information")
        .then((res) => {
          this.audio_data = [];
        })
        .catch((e) => console.log(e));
    },
  },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/information/get_information_list")
      .then((res) => {
        this.audio_data = res.data;
      })
      .catch((e) => console.log(e));
  },
};
</script>

<style scoped>
.information {
}

.action {
  display: flex;
  justify-content: end;
}

.action-item {
  margin: 10px 20px;
  padding: 10px 20px;
  border-radius: 4px;
  background: rgb(95, 95, 192);
  color: white;
  cursor: pointer;
}

.detail-action {
  display: flex;
  justify-content: end;
}

.detail-action-item {
  margin: 0 10px;
  padding: 5px 10px;
  border-radius: 4px;
  background: rgb(129, 129, 201);
  color: white;
  cursor: pointer;
}

.remove-button {
  background: rgb(252, 149, 149);
}
</style>