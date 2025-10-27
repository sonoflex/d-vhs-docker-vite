<template>
  <div v-if="movie">
    <h2>{{ movie.title }} ({{ movie.year }})</h2>
    <img :src="movie.poster_url" />
    <p>{{ movie.description }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
const route = useRoute();
const movie = ref(null);

onMounted(async () => {
  const res = await fetch(`http://localhost:8000/movies/${route.params.id}`);
  movie.value = await res.json();
});
</script>
