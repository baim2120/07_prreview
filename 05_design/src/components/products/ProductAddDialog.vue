<template>
    <div class="dialog-overlay">
        <div class="dialog">
            <div class="dialog-header">
                <h2>Add New Product</h2>
                <button class="close-btn" @click="$emit('close')">✕</button>
            </div>
            <form @submit.prevent="onSubmit" class="form-content">
                <div class="form-group">
                    <label>Name
                        <input v-model="form.name" required placeholder="Enter product name" />
                    </label>
                </div>
                <div class="form-group">
                    <label>Description
                        <textarea v-model="form.description" required placeholder="Enter product description" rows="3"></textarea>
                    </label>
                </div>
                <div class="form-row">
                    <div class="form-group">
                        <label>Price ($)
                            <input v-model.number="form.price" type="number" min="0" step="0.01" required placeholder="0.00" />
                        </label>
                    </div>
                    <div class="form-group">
                        <label>Stock
                            <input v-model.number="form.stock" type="number" min="0" required placeholder="0" />
                        </label>
                    </div>
                </div>
                <div class="actions">
                    <button type="button" class="secondary" @click="$emit('close')">Cancel</button>
                    <button type="submit" class="primary">Add Product</button>
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

.form-content {
    padding: 1.5rem;
}

.form-group {
    margin-bottom: 1.25rem;
}

.form-group:last-child {
    margin-bottom: 0;
}

.form-group label {
    display: block;
    color: var(--text);
    font-size: 0.875rem;
    font-weight: 500;
    margin-bottom: 0.5rem;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid var(--border);
    border-radius: var(--radius-sm);
    background: var(--surface);
    color: var(--text);
    font-size: 0.875rem;
    transition: border-color 0.2s;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--primary);
}

.form-group input::placeholder,
.form-group textarea::placeholder {
    color: var(--text-light);
}

.form-row {
    display: flex;
    gap: 1rem;
}

.form-row .form-group {
    flex: 1;
}

.actions {
    display: flex;
    justify-content: flex-end;
    gap: 0.75rem;
    margin-top: 2rem;
}

.actions button {
    padding: 0.75rem 1.5rem;
    border-radius: var(--radius-sm);
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
}

button.primary {
    background: var(--primary);
    color: white;
    border: none;
}

button.primary:hover {
    filter: brightness(1.1);
}

button.secondary {
    background: var(--surface);
    color: var(--text);
    border: 1px solid var(--border);
}

button.secondary:hover {
    background: var(--surface-hover);
}
</style>
