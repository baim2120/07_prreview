<template>
  <div>
    <h1>Products</h1>
    <a-button type="default" to="/create">
      <router-link to="/create">+ Add Product</router-link>
    </a-button>
    <ul>
      <li v-for="product in products" :key="product.id">
        <a-typography-paragraph>
          <a-space>
            <router-link :to="`/products/${product.id}`">
              {{ product.name }}
            </router-link>
            <a-button danger default @click="removeProduct(product.id)"><DeleteOutlined /></a-button>
          </a-space>
        </a-typography-paragraph>
      </li>
    </ul>
  </div>
</template>

<script>
import { getProducts, deleteProduct } from "../api/products";

export default {
  data() {
    return { products: [] };
  },
  async created() {
    const { data } = await getProducts();
    this.products = data;
  },
  methods: {
    async removeProduct(id) {
      if (confirm("Delete this product?")) {
        await deleteProduct(id);
        this.products = this.products.filter(p => p.id !== id);
      }
    }
  }
};
</script>
