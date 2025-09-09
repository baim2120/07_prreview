<template>
    <div class="dialog-overlay">
        <div class="dialog">
            <h2>Delete Product</h2>
            <p>Are you sure you want to delete <strong>{{ product.name }}</strong>?</p>
            <div class="actions">
                <button class="danger" @click="$emit('delete')">Delete</button>
                <button @click="$emit('close')">Cancel</button>
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

.actions {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
}

.danger {
    background: #ef4444;
    color: #fff;
    border: none;
    padding: 0.5rem 1.2rem;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
}
</style>
