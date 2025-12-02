<script setup lang="ts">
import { onMounted, onUnmounted } from 'vue';
import { useTelemetryStore } from '@/stores/telemetry';
import TelemetryChart from '@/components/TelemetryChart.vue';

const store = useTelemetryStore();
let intervalId: number;

onMounted(() => {
  // fetch data immediately and then start interval
  store.fetchTelemetryData();
  intervalId = window.setInterval(() => {
    store.fetchTelemetryData();
  }, 5000); // fetch every 5 seconds
});

onUnmounted(() => {
  clearInterval(intervalId);
});
</script>

<template>
  <main class="dashboard">
    <h1>🚗 Vehicle Telemetry Dashboard</h1>
    
    <div class="stats">
      <div class="card">
        <h3>Live Datenpunkte</h3>
        <p>{{ store.dataPoints.length }}</p>
      </div>
      <div class="card warning" v-if="store.criticalCount > 0">
        <h3>⚠️ Kritische Events</h3>
        <p>{{ store.criticalCount }}</p>
      </div>
      <div class="card ok" v-else>
        <h3>Status</h3>
        <p>Alles OK</p>
      </div>
    </div>

    <div class="chart-box">
      <TelemetryChart />
    </div>
  </main>
</template>

<style scoped>
.dashboard {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  font-family: sans-serif;
}

.stats {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.card {
  border: 1px solid #ddd;
  padding: 1rem;
  border-radius: 8px;
  min-width: 150px;
  text-align: center;
}

.warning {
  background-color: #fff3cd;
  color: #856404;
  border-color: #ffeeba;
}

.ok {
  background-color: #d4edda;
  color: #155724;
}

.chart-box {
  border: 1px solid #eee;
  padding: 1rem;
  border-radius: 8px;
}
</style>

