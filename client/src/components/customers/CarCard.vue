<template>
  <div class="car-card">
    <img src="@/assets/images/cars/car1.webp" alt="" />
    <div class="car-name">{{car.ten}}</div>
    <button @click="redirect(`/cars/new/${car.id}`)">Buy now</button>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  props:['car'],
  methods:{
    redirect(url){
      this.$router.push({ path:url})
    }
  }
};
</script>

<style scoped>
img {
  width: 100%;
  height: 220px;
}
.car-card {
  border: 1px rgb(109, 109, 109) solid;
}
.car-name{
    padding: 5px 10px;
    font-size: 18px;
}
button{
    width: 100%;
    padding: 10px;
    background: black;
    color: white;
}
</style>