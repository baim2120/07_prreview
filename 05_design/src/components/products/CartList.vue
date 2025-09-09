<template>
    <div class="cart-list">
        <h3>Cart</h3>
        <ul>
            <li v-for="item in cart" :key="item.id">
                {{ item.name }} | {{ item.quantity }} | Price: {{ item.price }}
                <button @click="removeOne(item)" :disabled="item.quantity < 1" style="margin-left:8px;">-</button>
            </li>
        </ul>
    </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { getCart, removeProductFromCart } from '../../api'

const props = defineProps({
    refreshKey: {
        type: Number,
        default: 0
    }
})

const cart = ref([])

async function fetchCart() {
    cart.value = await getCart()
}

async function removeOne(item) {
    try {
        await removeProductFromCart(item)
        await fetchCart()
    } catch (e) {
+        console.error('Failed to remove item from cart:', e)
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
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 1rem;
    min-width: 180px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    z-index: 1000;
}

.cart-list h3 {
    margin: 0 0 0.5rem 0;
    font-size: 1.1rem;
}

.cart-list ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.cart-list li {
    font-size: 0.98rem;
    margin-bottom: 0.3rem;
}
</style>
