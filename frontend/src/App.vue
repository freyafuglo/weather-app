<script setup>
import { ref, onMounted } from "vue";

const weather = ref(null);

onMounted(async () => {
  const response = await fetch("http://127.0.0.1:8000/api/weather/");
  weather.value = await response.json();
});
</script>

<template>
  <div>
    <h1>Weather App</h1>

    <div v-if="weather">
      <p>City: {{ weather.city }}</p>
      <p>Temperature: {{ weather.temperature }}°C</p>
    </div>

    <div v-else>
      Loading...
    </div>
  </div>
</template>