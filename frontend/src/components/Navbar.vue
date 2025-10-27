<template>
  <nav class="nav">
    <a href="/">🎞️ D-VHS</a>
    <router-link to="/">Filme</router-link>
    <router-link to="/admin/users">Benutzer</router-link>
  </nav>
</template>

<style>
.nav {
  display: flex;
  gap: 1rem;
  background: #333;
  color: white;
  padding: 0.5rem 1rem;
}
a { color: white; text-decoration: none; }
</style>
