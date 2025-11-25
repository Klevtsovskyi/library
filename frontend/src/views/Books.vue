<script setup>

import {useBookStore} from "@/stores/bookStore.js";
import {onMounted} from "vue";

const bookStore = useBookStore();
onMounted(async () => {
  await bookStore.loadBooks();
})
</script>

<template>
<h1>Перелік книг</h1>

  <div v-for="(book, index) in bookStore.books" :key="index">
    <router-link :to="{name: 'BookDetail', params: {id: book.id}}">{{ book.title }} </router-link>
    {{ book.author.first_name }} {{ book.author.last_name }}
  </div>
  <div v-if="bookStore.books.length === 0">Книги в бібліотеці відсутні</div>
</template>

<style scoped>

</style>