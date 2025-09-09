<template>
    <div class="dialog-overlay">
        <div class="dialog">
            <h2>Add New Product</h2>
            <form @submit.prevent="onSubmit">
                <label>Name<input v-model="form.name" required /></label>
                <label>Description<input v-model="form.description" required /></label>
                <label>Price<input v-model.number="form.price" type="number" min="0" required /></label>
                <label>Stock<input v-model.number="form.stock" type="number" min="0" required /></label>
                <div class="actions">
                    <button type="submit">Add</button>
                    <button type="button" @click="$emit('close')">Cancel</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
import { reactive } from 'vue'
const emit = defineEmits(['add', 'close'])
const form = reactive({ name: '', description: '', price: 0, stock: 0 })
function onSubmit() {
    emit('add', { ...form })
}
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
</style>
