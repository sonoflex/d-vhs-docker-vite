<template>
  <div class="movies">
    <h2>Filmliste</h2>
    <div class="grid">
      <div v-for="m in movies" :key="m.id" class="card">
        <img :src="m.poster_url" />
        <h3>{{ m.title }} ({{ m.year }})</h3>
        <p>{{ m.description.slice(0,100) }}...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const movies = ref([]);

onMounted(async () => {
  const res = await fetch("http://localhost:8000/movies");
  movies.value = await res.json();
});
</script>

<style>
.grid { display: flex; flex-wrap: wrap; gap: 1rem; }
.card { width: 200px; }
img { width: 100%; border-radius: 6px; }
</style>
