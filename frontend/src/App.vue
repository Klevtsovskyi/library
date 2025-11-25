<script setup>
import Menu from "@/views/Menu.vue";
</script>

<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-2">
        <Menu/>
      </div>
      <div class="col-md-10">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
