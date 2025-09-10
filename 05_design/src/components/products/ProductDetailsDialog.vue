<template>
    <div class="dialog-overlay">
        <div class="dialog">
            <div class="dialog-header">
                <h2>Product Details</h2>
                <button class="close-btn" @click="$emit('close')">✕</button>
            </div>
            <div class="product-info">
                <h3>{{ product.name }}</h3>
                <p class="description">{{ product.description }}</p>
                <div class="separator"></div>
                <div class="info-row">
                    <span class="label">Price:</span>
                    <span class="value price">${{ product.price }}</span>
                </div>
                <div class="info-row">
                    <span class="label">Stock:</span>
                    <span class="value">{{ product.stock }} units</span>
                </div>
                <div class="info-row">
                    <span class="label">Product ID:</span>
                    <span class="value">{{ product.id }}</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
const props = defineProps({ product: Object })
</script>

<style scoped>
    .dialog-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1000;
    }

    .dialog {
        background: var(--surface);
        border-radius: var(--radius);
        width: 100%;
        max-width: 444px;
        box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1), 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .dialog-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.5rem;
        border-bottom: 1px solid var(--border);
    }

    .dialog-header h2 {
        margin: 0;
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--text);
    }

    .close-btn {
        background: none;
        border: none;
        color: var(--text);
        font-size: 1.25rem;
        padding: 0.5rem;
        cursor: pointer;
        opacity: 0.7;
        transition: opacity 0.2s;
    }

    .close-btn:hover {
        opacity: 1;
    }

    .product-info {
        padding: 1.5rem;
    }

    .product-info h3 {
        margin: 0 0 1rem 0;
        font-size: 1.125rem;
        font-weight: 500;
        color: var(--text);
    }

    .description {
        color: var(--text-light);
        font-size: 1rem;
        line-height: 1.5;
        margin-bottom: 1.5rem;
    }

    .separator {
        height: 1px;
        background: var(--border);
        margin: 1.5rem 0;
    }

    .info-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }

    .info-row:last-child {
        margin-bottom: 0;
    }

    .label {
        color: var(--text-light);
        font-size: 0.875rem;
    }

    .value {
        color: var(--text);
        font-size: 0.875rem;
    }

    .price {
        color: var(--text);
        font-size: 1rem;
        font-weight: 500;
    }
</style>
