<template>
  <form @submit.prevent="login">
    <input v-model="username" placeholder="Benutzername" />
    <input type="password" v-model="password" placeholder="Passwort" />
    <button>Anmelden</button>
  </form>
</template>

<script setup>
import { ref } from "vue";
const username = ref("");
const password = ref("");

async function login() {
  const res = await fetch("http://localhost:8000/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username: username.value, password: password.value })
  });
  if (res.ok) alert("Login erfolgreich");
  else alert("Fehlerhafte Anmeldung");
}
</script>
