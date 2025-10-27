<template>
  <div>
    <h2>Benutzerverwaltung</h2>
    <form @submit.prevent="addUser">
      <input v-model="username" placeholder="Username" />
      <input v-model="email" placeholder="E-Mail" />
      <input type="password" v-model="password" placeholder="Passwort" />
      <button>Neuen Benutzer anlegen</button>
    </form>

    <ul>
      <li v-for="u in users" :key="u.id">{{ u.username }} – {{ u.email }}</li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const users = ref([]);
const username = ref("");
const email = ref("");
const password = ref("");

async function loadUsers() {
  const res = await fetch("http://localhost:8000/users");
  users.value = await res.json();
}

async function addUser() {
  const params = new URLSearchParams({ username: username.value, password: password.value, email: email.value });
  await fetch(`http://localhost:8000/users?${params.toString()}`, { method: "POST" });
  await loadUsers();
}

onMounted(loadUsers);
</script>
