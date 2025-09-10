<template>
    <div class="dialog-overlay">
        <div class="dialog">
            <div class="dialog-header">
                <h2>Delete Product</h2>
                <button class="close-btn" @click="$emit('close')">✕</button>
            </div>
            <div class="dialog-content">
                <div class="alert-icon">⚠️</div>
                <h3>Delete Confirmation</h3>
                <p class="message">Are you sure you want to delete <b>{{ product.name }}</b>? This action cannot be undone.</p>
                <div class="actions">
                    <button class="secondary" @click="$emit('close')">Cancel</button>
                    <button class="danger" @click="$emit('delete')">Delete Product</button>
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

.dialog-content {
    padding: 2rem 1.5rem;
    text-align: center;
}

.alert-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
}

.dialog-content h3 {
    margin: 0 0 1rem 0;
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--text);
}

.message {
    color: var(--text-light);
    font-size: 0.875rem;
    line-height: 1.5;
    margin-bottom: 2rem;
}

.message b {
    color: var(--text);
    font-weight: 500;
}

.actions {
    display: flex;
    justify-content: center;
    gap: 0.75rem;
}

.actions button {
    padding: 0.75rem 1.5rem;
    border-radius: var(--radius-sm);
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s;
}

.danger {
    background: var(--danger);
    color: white;
    border: none;
}

.danger:hover {
    filter: brightness(1.1);
}

.secondary {
    background: var(--surface);
    color: var(--text);
    border: 1px solid var(--border);
}

.secondary:hover {
    background: var(--surface-hover);
}
</style>
