<template>
  <div>
    <h1>{{ isEdit ? "Edit Product" : "Create Product" }}</h1>
    <form @submit.prevent="submitForm">
      <input v-model="form.name" placeholder="Name" required />
      <input v-model.number="form.price" placeholder="Price" type="number" required />
      <textarea v-model="form.description" placeholder="Description"></textarea>
      <input v-model.number="form.stock" placeholder="Stock" type="number" required />
      <button type="submit">{{ isEdit ? "Update" : "Create" }}</button>
    </form>
  </div>
</template>

<script>
import { createProduct, updateProduct, getProduct } from "../api/products";

export default {
  data() {
    return {
      form: { name: "", price: 0, description: "", stock: 0 },
      isEdit: false
    };
  },
  async created() {
    if (this.$route.params.id) {
      this.isEdit = true;
      const { data } = await getProduct(this.$route.params.id);
      this.form = data;
    }
  },
  methods: {
    async submitForm() {
      if (this.isEdit) {
        await updateProduct(this.$route.params.id, this.form);
      } else {
        await createProduct(this.form);
      }
      this.$router.push("/");
    }
  }
};
</script>
