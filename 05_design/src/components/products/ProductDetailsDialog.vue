<template>
    <div class="dialog-overlay">
        <div class="dialog">
            <h2>Product Details</h2>
            <div class="details">
                <div><strong>Name:</strong> {{ product.name }}</div>
                <div><strong>Description:</strong> {{ product.description }}</div>
                <div><strong>Price:</strong> {{ product.price }}</div>
                <div><strong>Stock:</strong> {{ product.stock }}</div>
            </div>
            <div class="actions">
                <button @click="$emit('close')">Close</button>
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
    background: rgba(0, 0, 0, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.dialog {
    background: #fff;
    padding: 2rem;
    border-radius: 8px;
    min-width: 320px;
    box-shadow: 0 2px 16px rgba(0, 0, 0, 0.1);
}

.details {
    margin-bottom: 1.5rem;
}

.actions {
    display: flex;
    justify-content: flex-end;
}
</style>
