<template>
    <div class="cart-list">
        <header class="cart-header">
            <h3>Shopping Cart</h3>
            <span class="item-count" v-if="cart.length">{{ cartItemCount }} items</span>
        </header>
        <div class="cart-items" v-if="cart.length">
            <div v-for="item in cart" :key="item.id" class="cart-item">
                <div class="item-info">
                    <div class="item-name">{{ item.name }}</div>
                    <div class="item-price">${{ item.price.toLocaleString() }}</div>
                </div>
                <div class="item-quantity">
                    <button class="quantity-btn" @click="removeOne(item)" :disabled="item.quantity < 1">
                        <span>−</span>
                    </button>
                    <span class="quantity">{{ item.quantity }}</span>
                </div>
            </div>
            <div class="cart-total">
                <span>Total:</span>
                <span>${{ totalPrice.toLocaleString() }}</span>
            </div>
        </div>
        <div v-else class="empty-cart">
            Your cart is empty
        </div>
    </div>
</template>

<script setup>
import { ref, watch, onMounted, computed } from 'vue'
import { getCart, removeProductFromCart } from '../../api'

const props = defineProps({
    refreshKey: {
        type: Number,
        default: 0
    }
})
const emit = defineEmits(['cart-updated'])

const cart = ref([])

const cartItemCount = computed(() => {
    return cart.value.reduce((sum, item) => sum + item.quantity, 0)
})

const totalPrice = computed(() => {
    return cart.value.reduce((sum, item) => sum + (item.price * item.quantity), 0)
})

async function fetchCart() {
    cart.value = await getCart()
}

async function removeOne(item) {
    try {
        await removeProductFromCart(item)
        await fetchCart()
        emit('cart-updated')
    } catch (e) {
        console.error('Failed to remove item from cart:', e)
    }
}

onMounted(fetchCart)
watch(() => props.refreshKey, fetchCart)
</script>

<style scoped>
.cart-list {
    position: fixed;
    left: 1rem;
    bottom: 1rem;
    background: #fff;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    width: 320px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    z-index: 1000;
}

.cart-header {
    padding: 1rem;
    border-bottom: 1px solid #e5e7eb;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.cart-header h3 {
    margin: 0;
    font-size: 1.1rem;
    font-weight: 600;
    color: #111827;
}

.item-count {
    font-size: 0.875rem;
    color: #6b7280;
}

.cart-items {
    max-height: 400px;
    overflow-y: auto;
}

.cart-item {
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #f3f4f6;
}

.item-info {
    flex: 1;
}

.item-name {
    font-weight: 500;
    color: #111827;
    margin-bottom: 0.25rem;
}

.item-price {
    font-size: 0.875rem;
    color: #6b7280;
}

.item-quantity {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.quantity-btn {
    background: #f3f4f6;
    border: none;
    border-radius: 6px;
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    color: #374151;
    font-weight: bold;
    transition: all 0.2s;
}

.quantity-btn:hover:not(:disabled) {
    background: #e5e7eb;
}

.quantity-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.quantity {
    font-weight: 500;
    min-width: 20px;
    text-align: center;
}

.cart-total {
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    font-weight: 600;
    color: #111827;
    border-top: 1px solid #e5e7eb;
    background: #f9fafb;
    border-radius: 0 0 12px 12px;
}

.empty-cart {
    padding: 2rem 1rem;
    text-align: center;
    color: #6b7280;
    font-size: 0.875rem;
}
</style>
