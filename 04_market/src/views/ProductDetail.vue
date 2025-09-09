<template>
  <div v-if="product">
    <a-space>
      <a-typography-title>
        {{ product.name }}
      </a-typography-title>
      <a-button type="link">
        <router-link :to="`/edit/${product.id}`">
          <EditOutlined />
        </router-link>
      </a-button>
    </a-space>
    <p>Price: ${{ product.price }}</p>
    <p>{{ product.description }}</p>
    <p>Stock: {{ product.stock }}</p>
  </div>
</template>

<script>
import { getProduct } from "../api/products";

export default {
  data() {
    return { product: null };
  },
  async created() {
    const { id } = this.$route.params;
    const { data } = await getProduct(id);
    this.product = data;
  }
};
</script>
