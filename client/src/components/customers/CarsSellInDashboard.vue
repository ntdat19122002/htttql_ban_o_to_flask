<template>
  <div class="car-sell-in-dashboard">
    <div class="grid">
        <CarCard></CarCard>
        <CarCard></CarCard>
    </div> 
  </div>
</template>

<script>
import CarCard from "./CarCard.vue";
export default {
  components: {
    CarCard,
  },
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