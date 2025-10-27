import { createRouter, createWebHistory } from "vue-router";
import MovieList from "./components/MovieList.vue";
import MovieDetail from "./components/MovieDetail.vue";
import Login from "./components/Login.vue";
import AdminUsers from "./components/AdminUsers.vue";

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: MovieList },
    { path: "/login", component: Login },
    { path: "/movies/:id", component: MovieDetail },
    { path: "/admin/users", component: AdminUsers }
  ]
});
