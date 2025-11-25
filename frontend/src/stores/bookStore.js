import {defineStore} from "pinia";
import {useRoute} from "vue-router";
import {ref} from "vue";
import apiPublic from "@/utils/apiPublic.js";

export const useBookStore = defineStore("books", () => {
    const book = ref(null);
    const books = ref([]);

    async function loadBooks() {
        const res = await apiPublic.get("/books");
        books.value = res.data;
    }

    async function loadBook() {
        const route = useRoute();
        const res = await apiPublic.get(`/books/${route.params.id}`);
        book.value = res.data;
    }

    return {book, books, loadBook, loadBooks}
});