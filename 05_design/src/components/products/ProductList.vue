<template>
    <div class="product-list-page">
        <header class="header">
            <h1>Product Management</h1>
            <button class="add-btn" @click="$emit('add-product')">Add New Product</button>
        </header>
        <table class="product-table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Price</th>
                    <th>Stock</th>
                    <th>Actions</th>
                    <th>Add to Cart</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="product in products" :key="product.id">
                    <td>{{ product.name }}</td>
                    <td>{{ product.description }}</td>
                    <td>{{ product.price }}</td>
                    <td>{{ product.stock }}</td>
                    <td>
                        <button @click="$emit('view-product', product)">Details</button>
                        <button @click="$emit('edit-product', product)">Edit</button>
                        <button @click="$emit('delete-product', product)">Delete</button>
                    </td>
                    <td>
                        <button @click="$emit('add-to-cart', product)" :disabled="product.stock < 1" title="Add to cart">
                            <span style="font-size:1.3em;">+</span>
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
defineProps({
    products: Array
})
</script>

<style scoped>
.product-list-page {
    padding: 2rem;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
}

.add-btn {
    background: #3b82f6;
    color: #fff;
    border: none;
    padding: 0.5rem 1.2rem;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
}

.product-table {
    width: 100%;
    border-collapse: collapse;
}

.product-table th,
.product-table td {
    border: 1px solid #e5e7eb;
    padding: 0.75rem 1rem;
    text-align: left;
}

.product-table th {
    background: #f3f4f6;
}
</style>
