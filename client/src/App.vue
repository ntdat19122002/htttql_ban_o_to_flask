<script>
import { RouterLink, RouterView } from "vue-router";
export default {
  computed: {
    isAdmin() {
      return this.$route.path.includes("admin");
    },
  },
};
</script>

<template>
  <div class="navbar" v-if="!isAdmin">
    <router-link :to="{ name: 'dashboard' }" class="navbar-item"
      >Dashboard</router-link
    >
    <router-link v-if="false" :to="{ name: 'information' }" class="navbar-item"
      >Information</router-link
    >
  </div>
  <div class="navbar-admin" v-else>
    <router-link :to="{ name: 'admin' }" class="navbar-item"
      >Dashboard</router-link
    >
    <router-link :to="{ name: 'admin_livetime' }" class="navbar-item"
      >Lifetime</router-link
    >
    <router-link :to="{ name: 'admin_hoadon' }" class="navbar-item"
      >Bill</router-link
    >
    <router-link :to="{ name: 'admin_oto' }" class="navbar-item"
      >Car</router-link
    >
   
    <router-link :to="{ name: 'admin_loaixe' }" class="navbar-item"
      >Model</router-link
    >
    <router-link :to="{ name: 'admin_nguoidung' }" class="navbar-item"
      >Customer</router-link
    >
    <router-link :to="{ name: 'admin_hoadontemp' }" class="navbar-item"
      >Đơn hàng</router-link
    >
  </div>
  <RouterView />
</template>

<style scoped>
.navbar {
  display: flex;
  background: rgb(39, 40, 27);
}
a {
  padding: 10px 20px;
  color: white;
  text-decoration: none;
}
a.router-link-active {
  background: rgb(79, 82, 93);
}

.navbar-admin{
  display: flex;
  background: rgb(118, 128, 184);
}
.navbar-admin a{
  padding: 10px 20px;
  color: white;
  text-decoration: none;
}
.navbar-admin a.router-link-active{
  background: rgb(70 87 175);
  border-radius: 5px;
}
</style>
