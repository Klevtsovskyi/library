<script setup>

import {useBookStore} from "@/stores/bookStore.js";
import {onMounted, ref} from "vue";
import {useRoute, useRouter} from "vue-router";

const bookStore = useBookStore();
const route = useRoute();
const router = useRouter();

const form = ref({
  "due_back": "",
  "status": "a",
  "imprint": "",
  "borrower": ""
});

const result = ref("");

onMounted(async () => {
  await bookStore.loadBook();
});

const submitForm = async () => {
  try {
    const payload = {...form.value};
    payload['book'] = route.params.id;

    if (!payload.due_back) payload.due_back = null;
    if (!payload.imprint) payload.imprint = null;
    if (!payload.borrower) payload.borrower = null;

    await bookStore.addBookInstance(payload);
    result.value = "succes";

    await router.push({name: 'BookDetail', params: {id: route.params.id}});
  }
  catch (e) {
    console.log(e);
    result.value = "error";
  }
};
</script>

<template>

  <form @submit.prevent="submitForm">
    <div class="form-group">
      <label for="due_back">Дата повернення</label>
      <input class="form-control" id="due_back" type="date" v-model="form.due_back">
    </div>
    <div class="form-group">
      <label for="status">Статус</label>
      <select class="form-control" id="status" v-model="form.status">
        <option value="a">Доступно</option>
        <option value="r">Зарезервовано</option>
        <option value="m">На обслуговуванні</option>
        <option value="o">Орендована</option>
      </select>
    </div>
        <div class="form-group">
      <label for="imprint">Видавництво</label>
      <input class="form-control" id="imprint" type="text" v-model="form.imprint">
    </div>
    <div class="form-group">
      <input class="btn btn-success" type="submit" value="Додати">
    </div>
  </form>

</template>

<style scoped>
  .form-control {
    margin-bottom: 10px;
  }
</style>