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
          title: "Màu",
          dataIndex: "mau",
          key: "mau",
        },
        {
          title: "Số khung",
          dataIndex: "so_khung",
          key: "so_khung",
        },
        {
          title: "Số máy",
          dataIndex: "so_may",
          key: "so_may",
        },
        {
          title: "Ngày sản xuất",
          dataIndex: "ngay_san_xuat",
          key: "ngay_san_xuat",
        },
        {
          title: "Giá nhập",
          dataIndex: "gia_nhap",
          key: "gia_nhap",
        },
        {
          title: "Giá bán",
          dataIndex: "gia_ban",
          sorter: true,
          key: "gia_ban",
        },
        {
          title: "Tình trạng",
          dataIndex: "tinh_trang",
          sorter: true,
          key: "tinh_trang",
        },
        {
          title: "Tên khách hàng",
          dataIndex: "ten",
          sorter: true,
          key: "ten",
        },
        {
          title: "Email",
          dataIndex: "email",
          sorter: true,
          key: "email",
        },
        {
          title: "Địa chỉ",
          dataIndex: "dia_chi",
          sorter: true,
          key: "dia_chi",
        },
      ],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/hoa_don_temp/list")
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