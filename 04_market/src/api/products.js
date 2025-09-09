import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // FastAPI backend URL
});

export const getProducts = () => api.get("/products/");
export const getProduct = (id) => api.get(`/products/${id}`);
export const createProduct = (data) => api.post("/products/", data);
export const updateProduct = (id, data) => api.put(`/products/${id}`, data);
export const deleteProduct = (id) => api.delete(`/products/${id}`);
