<template>
  <div class="car-sell-in-dashboard">
    <div class="grid">
        <div v-for="car in cars" :key="car">
          <CarCard :car="car"/>
        </div>
    </div> 
  </div>
</template>

<script>
import axios from 'axios';
import CarCard from "./CarCard.vue";
export default {
  components: {
    CarCard,
  },
  data(){
    return{
      cars:[]
    }
  },
  mounted(){
    axios.get('http://127.0.0.1:5000/car/list')
    .then(res => {
      this.cars = res.data
    })
  }
};
</script>

<style scoped>
@media screen  and (max-width: 1400px) {
    .grid{
        display: grid;
        grid-template-columns: auto auto auto auto;
    }
}
.grid{
    padding: 50px 100px;
    display: grid;
    gap: 20px;
    grid-template-columns: auto auto auto auto auto;
}
</style>