<script setup>


import {useBookStore} from "@/stores/bookStore.js";
import {onMounted} from "vue";

const bookStore = useBookStore();

onMounted(async () => {
  await bookStore.loadBook();
})
</script>

<template>
  <div v-if="bookStore.book">
    <h1 v-text="bookStore.book.title"></h1>
    <div>Автор: {{ bookStore.book.author.first_name }} {{ bookStore.book.author.last_name }}</div>
    <div>Опис: {{ bookStore.book.summary }}</div>
    <div>ISBN: {{ bookStore.book.isbn }}</div>
  </div>
</template>

<style scoped>

</style>