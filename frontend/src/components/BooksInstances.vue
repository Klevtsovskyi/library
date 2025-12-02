<script setup>
import {useBookStore} from "@/stores/bookStore.js";
import {onMounted} from "vue";

const bookStore = useBookStore();

onMounted(async () => {
  await bookStore.loadBooksInstances();
});
</script>

<template>
  <div v-if="bookStore.booksinstances.length > 0">
    <ul>
      <li v-for="(instance, index) in bookStore.booksinstances" :key="index">
        {{ instance.id }} {{ instance.imprint }}
      </li>
    </ul>
  </div>
</template>

<style scoped>

</style>