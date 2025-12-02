<script setup lang="ts">
// chart registry
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale } from 'chart.js';
import { Line } from 'vue-chartjs';
import { ref, watch, computed } from 'vue';
import { useTelemetryStore } from '@/stores/telemetry';

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, CategoryScale, LinearScale);

const telemetryStore = useTelemetryStore();

// prepare chart data
const chartData = computed(() => {
  return {
    labels: telemetryStore.dataPoints.map(dp => new Date(dp.timestamp).toLocaleTimeString()),
    datasets: [
      {
        label: 'Speed (km/h)',
        data: telemetryStore.dataPoints.map(dp => dp.speed),
        borderColor: 'rgba(75, 192, 192, 1)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        fill: true,
        tension: 0.4,
      },
      {
        label: 'Engine Temperature (°C)',
        data: telemetryStore.dataPoints.map(dp => dp.engineTemp),
        borderColor: 'rgba(255, 99, 132, 1)',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        fill: true,
        tension: 0.4,
      },
    ],
  };
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: true,
    },
  },
};
</script>

<template>
  <div class="telemetry-chart">
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

<style scoped>
.telemetry-chart {
    width: 100%;
    height: 400px;
    position: relative;
}
</style>