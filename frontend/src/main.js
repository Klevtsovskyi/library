import { createApp } from 'vue';
import App from './App.vue';
import router from "@/utils/routes.js";
import {createBootstrap} from "bootstrap-vue-next";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue-next/dist/bootstrap-vue-next.css";
import {createPinia} from "pinia";

const pinia = createPinia();
const bootstrap = createBootstrap();

createApp(App)
    .use(pinia)
    .use(bootstrap)
    .use(router)
    .mount('#app');
