import {createWebHistory, createRouter} from "vue-router";

const router = createRouter({
        "history": createWebHistory(),
        "routes": [
            {
                path: "/",
                name: "Home",
                component: () => import("@/views/Home.vue")
            },
            {
                path: "/books",
                name: "Books",
                component: () => import("@/views/Books.vue")
            },
            {
                path: "/book/:id",
                name: "BookDetail",
                component: () => import("@/views/BookDetail.vue")
            }
        ]
    }
);

export default router;
