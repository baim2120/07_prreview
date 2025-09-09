import { createRouter, createWebHistory } from "vue-router";
import ProductList from "../views/ProductList.vue";
import ProductDetail from "../views/ProductDetail.vue";
import ProductForm from "../views/ProductForm.vue";

const routes = [
  { path: "/", name: "ProductList", component: ProductList },
  { path: "/products/:id", name: "ProductDetail", component: ProductDetail },
  { path: "/create", name: "CreateProduct", component: ProductForm },
  { path: "/edit/:id", name: "EditProduct", component: ProductForm },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
