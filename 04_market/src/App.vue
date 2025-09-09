<template>
  <div id="app">
    <header>
      <h1>Market Manager</h1>
      <nav>
        <router-link to="/">Products</router-link>
        <router-link to="/create">Add Product</router-link>
      </nav>
    </header>

    <main>
      <!-- Router outlet: loads ProductList by default -->
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #2c3e50;
  padding: 0.75rem 1rem;
  color: white;
}

nav a {
  color: white;
  margin-left: 1rem;
  text-decoration: none;
}

nav a.router-link-exact-active {
  font-weight: bold;
  text-decoration: underline;
}

main {
  padding: 1rem;
}
</style>
