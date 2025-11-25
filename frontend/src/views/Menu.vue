<script setup>
import router from "@/utils/routes.js";

</script>

<template>
  <h5>Меню</h5>
  <ul>
    <li><router-link :to="{name: 'Home'}">Головна</router-link></li>
    <li><router-link :to="{name: 'Books'}">Книги</router-link></li>
  </ul>
</template>

<style scoped>

</style>