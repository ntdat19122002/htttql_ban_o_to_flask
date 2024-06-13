<template>
  <div class="information">
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
          title: "Tên",
          dataIndex: "ten",
          key: "ten",
        },
        {
          title: "Email",
          dataIndex: "email",
          key: "email",
        },
        {
          title: "Địa chỉ",
          dataIndex: "dia_chi",
          key: "dia_chi",
        },
        {
          title: "Số điện thoại",
          dataIndex: "so_dien_thoai",
          key: "so_dien_thoai",
        }
      ],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/nguoi_dung/list")
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