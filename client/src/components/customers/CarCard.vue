<template>
  <div class="car-card">
    <img src="@/assets/images/cars/car1.webp" alt="" />
    <div class="car-name">Tesla model-3</div>
    <button>Buy now</button>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
img {
  width: 100%;
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