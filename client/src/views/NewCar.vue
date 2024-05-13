<template>
  <div class="new-car">
    <div class="main">
      <div class="lelf">
        <img src="@/assets/images/cars/car1.webp" alt="">
      </div>
      <div class="right">
        <div class="title">
          {{information.ten}}
        </div>
        <div class="description">
          {{information.mo_ta}}
        </div>
        <div class="detail">
          <div class="sub-detail">
            <span class="sub-detail-title">Hãng: </span><span>{{information.hang}}</span>
          </div>
          <div class="sub-detail">
            <span class="sub-detail-title">Nhiên liệu: </span><span>{{information.nhien_lieu}}</span>
          </div>
          <div class="sub-detail">
            <span class="sub-detail-title">Phiên bản: </span><span>{{information.phien_ban}}</span>
          </div>
          <div class="sub-detail">
            <span class="sub-detail-title">Xuất sứ: </span><span>{{information.xuat_su}}</span>
          </div>
        </div>
        <button class="contact-us">Contact us</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return{
      information:null,
    }
  },
  async beforeMount(){
    console.log(1);
    await axios.post('http://127.0.0.1:5000/car/new',{
      loai_xe_id:this.$route.params.loai_xe_id
    }).then(res => this.information = res.data)
  }
}
</script>

<style scoped>
.main{
  margin: 10px 10%;
  display: flex;
}
.left{
  width: 60%;
}
.left img{
  width: 100%;
}
.right{
  padding: 20px 40px;
}
.title{
  font-size: 36px;
  font-weight: 600;
}
.description{
  font-size: 14px;
  color: rgb(145, 145, 145);
}

.detail{
  margin: 30px 0;
}

.sub-detail{
  margin: 15px 0;
}
.sub-detail-title{
  font-weight: 600;
}
.contact-us{
  padding: 10px 40px;
  font-size: 24px;
  font-weight: 600;
  color: white;
  background: black;
}
</style>