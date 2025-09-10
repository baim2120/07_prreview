<template>
    <div class="product-list-page">
        <div class="list-header">
            <div class="search-section">
                <div class="search-input">
                    <span class="search-icon">🔍</span>
                    <input 
                        type="text" 
                        placeholder="Search products..." 
                        v-model="searchQuery"
                    />
                </div>
            </div>
            <button class="add-btn" @click="$emit('add-product')">
                <span>Add Product</span>
                <span class="plus-icon">+</span>
            </button>
        </div>
        <div class="product-grid">
            <div v-for="product in filteredProducts" :key="product.id" class="product-card">
                <div class="card-content">
                    <h4 class="product-title">{{ product.name }}</h4>
                    <p class="product-description">{{ product.description }}</p>
                    <div class="card-footer">
                        <span class="stock">Stock: {{ product.stock }}</span>
                        <span class="price">${{ product.price }}</span>
                    </div>
                </div>
                <div class="card-actions">
                    <button class="action-btn" @click="$emit('view-product', product)" title="View Details">
                        <span>View</span>
                        <span class="icon">🔍</span>
                    </button>
                    <button class="action-btn" @click="$emit('edit-product', product)" title="Edit">
                        <span>Edit</span>
                        <span class="icon">✏️</span>
                    </button>
                    <button class="action-btn delete" @click="$emit('delete-product', product)" title="Delete">
                        <span class="icon">🗑️</span>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
    products: {
        type: Array,
        required: true,
        default: () => []
    }
})

const searchQuery = ref('')

const filteredProducts = computed(() => {
    if (!searchQuery.value) return props.products
    
    const query = searchQuery.value.toLowerCase()
    return props.products.filter(product => {
        return (
            product.name.toLowerCase().includes(query) ||
            product.description.toLowerCase().includes(query) ||
            product.price.toString().includes(query) ||
            product.stock.toString().includes(query)
        )
    })
})
</script>

<style scoped>
.product-list-page {
    padding: 1rem;
    width: 100%;
    max-width: 1120px;
    margin: 0 auto;
}

.list-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
    gap: 1rem;
}

.search-section {
    flex: 1;
    max-width: 392px;
}

.search-input {
    position: relative;
    width: 100%;
}

.search-input input {
    width: 100%;
    padding: 8px 8px 8px 35px;
    border: none;
    background: var(--bg);
    border-radius: var(--radius);
    font-size: 0.875rem;
    color: var(--text);
}

.search-icon {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-light);
    font-size: 0.875rem;
}

.add-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--primary);
    color: #fff;
    border: none;
    border-radius: var(--radius);
    padding: 0.5rem 1rem;
    font-weight: 500;
    font-size: 0.875rem;
}

.add-btn:hover {
    background: var(--primary-hover);
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
}

/* Make it responsive for smaller screens */
@media (max-width: 1024px) {
    .product-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media (max-width: 640px) {
    .product-grid {
        grid-template-columns: repeat(1, minmax(0, 1fr));
    }
}

.product-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    overflow: hidden;
}

.card-content {
    padding: 1rem;
}

.product-title {
    margin: 0;
    font-size: 1rem;
    font-weight: 400;
    color: var(--text);
    margin-bottom: 0.5rem;
}

.product-description {
    color: var(--text-light);
    font-size: 0.875rem;
    line-height: 1.5;
    margin-bottom: 1rem;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: auto;
}

.stock {
    color: var(--text-light);
    font-size: 0.875rem;
}

.price {
    color: var(--text);
    font-weight: 500;
    font-size: 1rem;
}

.card-actions {
    display: flex;
    gap: 0.5rem;
    padding: 1rem;
    background: var(--bg);
    border-top: 1px solid var(--border);
}

.action-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    background: none;
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 0.4rem 0.8rem;
    font-size: 0.75rem;
    color: var(--text);
    transition: all 0.2s;
}

.action-btn:hover {
    background: var(--bg);
    border-color: var(--text);
}

.action-btn.delete {
    background: var(--danger);
    border-color: var(--danger);
    color: white;
    padding: 0.4rem;
}

.action-btn.delete:hover {
    background: var(--danger-hover);
    border-color: var(--danger-hover);
}

.icon {
    font-size: 1rem;
    line-height: 1;
    background: var(--surface);
    border-radius: var(--radius);
    overflow: hidden;
}
.product-table th, .product-table td {
    padding: 1em;
    text-align: left;
}
.product-table th {
    background: var(--bg);
    color: var(--text-light);
    font-weight: 500;
    border-bottom: 1px solid var(--border);
}
.product-table td {
    border-bottom: 1px solid var(--border);
}
.product-table tr:last-child td {
    border-bottom: none;
}
.product-table button {
    margin-left: 0.2em;
    margin-right: 0.2em;
    padding: 0.3em 0.7em;
    font-size: 1em;
    border-radius: var(--radius);
    border: none;
    background: var(--bg);
    color: var(--primary);
    cursor: pointer;
    transition: background 0.2s, color 0.2s;
}
.product-table button:hover {
    background: var(--primary);
    color: #fff;
}
.product-table button.danger {
    background: var(--danger);
    color: #fff;
}
.product-table button.danger:hover {
    background: var(--danger-hover);
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
