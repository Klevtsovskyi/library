import {defineStore} from "pinia";
import {useRoute} from "vue-router";
import {ref} from "vue";
import apiPublic from "@/utils/apiPublic.js";

export const useBookStore = defineStore("books", () => {
    const book = ref(null);
    const books = ref([]);
    const booksinstances = ref([]);

    async function loadBooks() {
        const res = await apiPublic.get("/books");
        books.value = res.data;
    }

    async function loadBook() {
        const route = useRoute();
        const res = await apiPublic.get(`/books/${route.params.id}`);
        book.value = res.data;
    }

    async function loadBooksInstances(){
        const route = useRoute();
        const id = route.params.id;
        const res = await apiPublic.get(`/booksinstances/?book_id=${id}`);
        booksinstances.value = res.data;
    }

    async function addBookInstance(payload){
        try {
            const res = await apiPublic.post(`/bookinstanceadd/`, payload);
            return res.data;
        } catch (e) {
            console.log(e);
        }
    }

    return {book, books, booksinstances, loadBook, loadBooks, loadBooksInstances, addBookInstance}
});