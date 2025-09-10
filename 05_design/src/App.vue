<script setup>
import { ref, onMounted } from 'vue'
import ProductList from './components/products/ProductList.vue'
import CartList from './components/products/CartList.vue'
import ProductAddDialog from './components/products/ProductAddDialog.vue'
import ProductEditDialog from './components/products/ProductEditDialog.vue'
import ProductDetailsDialog from './components/products/ProductDetailsDialog.vue'
import ProductDeleteDialog from './components/products/ProductDeleteDialog.vue'
import { addProductToCart, fetchProducts, addProduct, updateProduct, deleteProduct } from './api.js'

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

const cartRefreshKey = ref(0)
async function handleAddToCart(product) {
  try {
    await addProductToCart(product)
    cartRefreshKey.value++
    await loadProducts()
  } catch (e) {
    error.value = e.response?.data?.detail || e.message
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
  <div class="app-container">
    <header class="app-header">
      <h1>Product Management</h1>
    </header>
    <main class="app-main">
      <ProductList
        :products="products"
        @add-product="handleAddProduct"
        @edit-product="handleEditProduct"
        @view-product="handleViewProduct"
        @delete-product="handleDeleteProduct"
        @add-to-cart="handleAddToCart"
      />
      <CartList :refreshKey="cartRefreshKey" />
      <ProductAddDialog v-if="showAdd" @add="handleAdd" @close="showAdd = false" />
      <ProductEditDialog v-if="showEdit" :product="selectedProduct" @edit="handleEdit" @close="showEdit = false" />
      <ProductDetailsDialog v-if="showDetails" :product="selectedProduct" @close="showDetails = false" />
      <ProductDeleteDialog v-if="showDelete" :product="selectedProduct" @delete="handleDelete" @close="showDelete = false" />
      <div v-if="loading" class="loading">Loading...</div>
      <div v-if="error" class="error">{{ error }}</div>
    </main>
  </div>
</template>

<style>
.app-container {
  min-height: 100vh;
  background: var(--bg);
  display: flex;
  flex-direction: column;
}
.app-header {
  background: var(--surface);
  box-shadow: 0 2px 8px rgba(30,41,59,0.04);
  padding: 2rem 2rem 1rem 2rem;
  border-bottom: 1px solid var(--border);
}
.app-header h1 {
  margin: 0;
  font-size: 2rem;
  color: var(--primary);
}
.app-main {
  flex: 1;
  max-width: 900px;
  margin: 2rem auto;
  width: 100%;
}
.loading {
  color: var(--text-light);
  margin-top: 1rem;
}
.error {
  color: var(--danger);
  margin-top: 1rem;
}
</style>
