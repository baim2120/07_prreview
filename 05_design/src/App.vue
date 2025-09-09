<script setup>
import { ref, onMounted } from 'vue'
import ProductList from './components/products/ProductList.vue'
import ProductAddDialog from './components/products/ProductAddDialog.vue'
import ProductEditDialog from './components/products/ProductEditDialog.vue'
import ProductDetailsDialog from './components/products/ProductDetailsDialog.vue'
import ProductDeleteDialog from './components/products/ProductDeleteDialog.vue'
import { fetchProducts, addProduct, updateProduct, deleteProduct } from './api.js'

const products = ref([])
const loading = ref(false)
const error = ref('')

async function loadProducts() {
  loading.value = true
  error.value = ''
  try {
    products.value = await fetchProducts()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

onMounted(loadProducts)

const showAdd = ref(false)
const showEdit = ref(false)
const showDetails = ref(false)
const showDelete = ref(false)
const selectedProduct = ref(null)

function handleAddProduct() {
  showAdd.value = true
}
async function handleAdd(product) {
  // Ensure 'description' is sent, not 'category'
  const { name, description, price, stock } = product
  try {
    await addProduct({ name, description, price, stock })
    await loadProducts()
  } catch (e) {
    error.value = e.message
  }
  showAdd.value = false
}
function handleEditProduct(product) {
  selectedProduct.value = { ...product }
  showEdit.value = true
}
async function handleEdit(product) {
  // Ensure 'description' is sent, not 'category'
  const { name, description, price, stock } = product
  try {
    await updateProduct(selectedProduct.value.id, { name, description, price, stock })
    await loadProducts()
  } catch (e) {
    error.value = e.message
  }
  showEdit.value = false
}
function handleViewProduct(product) {
  selectedProduct.value = { ...product }
  showDetails.value = true
}
function handleDeleteProduct(product) {
  selectedProduct.value = { ...product }
  showDelete.value = true
}
async function handleDelete() {
  try {
    await deleteProduct(selectedProduct.value.id)
    await loadProducts()
  } catch (e) {
    error.value = e.message
  }
  showDelete.value = false
}
</script>

<template>
  <div>
    <div v-if="loading">Loading...</div>
    <div v-if="error" style="color: red;">{{ error }}</div>
    <ProductList :products="products" @add-product="handleAddProduct" @edit-product="handleEditProduct"
      @view-product="handleViewProduct" @delete-product="handleDeleteProduct" />

    <ProductAddDialog v-if="showAdd" @add="handleAdd" @close="showAdd = false" />
    <ProductEditDialog v-if="showEdit" :product="selectedProduct" @edit="handleEdit" @close="showEdit = false" />
    <ProductDetailsDialog v-if="showDetails" :product="selectedProduct" @close="showDetails = false" />
    <ProductDeleteDialog v-if="showDelete" :product="selectedProduct" @delete="handleDelete"
      @close="showDelete = false" />
  </div>
</template>

<style scoped></style>
