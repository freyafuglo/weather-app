<script setup>
import { ref, onMounted } from "vue";


const city = ref("");
const weather = ref(null);

//const message = ref("");



async function getWeather() {
  const response = await fetch(`http://127.0.0.1:8000/api/weather/?city=${city.value}`);
  weather.value = await response.json();
}
</script>

<template>
  <div>
    <h1>Weather App</h1>

    <!--p>Message is: {{ message }}</p-->

    <input v-model="city" placeholder="edit me" />

    <button @click="getWeather">Submit</button>

    <div v-if="weather">
      <p>City: {{ weather.city }}</p>
      <p>Temperature: {{ weather.temperature }} °C</p>
      <p>Wind speed: {{ weather.wind_speed }} km/h</p>
      <p>Time: {{ weather.time }}</p>
      
    </div>

    <div v-else>
      Loading...
    </div>
  </div>
</template>