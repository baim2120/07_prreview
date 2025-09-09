// Update this URL to match your FastAPI backend location if needed
const API_BASE = 'http://localhost:8000'

export async function fetchProducts() {
	const res = await fetch(`${API_BASE}/products`)
	if (!res.ok) throw new Error('Failed to fetch products')
	return await res.json()
}

export async function addProduct(product) {
	const res = await fetch(`${API_BASE}/products`, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(product)
	})
	if (!res.ok) throw new Error('Failed to add product')
	return await res.json()
}

export async function updateProduct(id, product) {
	const res = await fetch(`${API_BASE}/products/${id}`, {
		method: 'PUT',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(product)
	})
	if (!res.ok) throw new Error('Failed to update product')
	return await res.json()
}

export async function deleteProduct(id) {
	const res = await fetch(`${API_BASE}/products/${id}`, {
		method: 'DELETE'
	})
	if (!res.ok) throw new Error('Failed to delete product')
	return true
}
