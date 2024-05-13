<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="navbar">
    <router-link :to="{name:'dashboard'}" class="navbar-item">Dashboard</router-link>
    <router-link v-if="false" :to="{name:'information'}" class="navbar-item">Information</router-link>
  </div>
  <RouterView />
</template>

<style scoped>
.navbar{
  display: flex;
  background: rgb(39, 40, 27);
}
a{
  padding: 10px 20px;
  color: white;
  text-decoration: none;
}
a.router-link-active{
  background: rgb(79, 82, 93);
}
</style>
