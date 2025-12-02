import axios from "axios";
import { defineStore } from "pinia";
import { computed, ref } from "vue";

interface TelemetryData {
    vehicle_id: string;
    temperature: number;
    speed: number;
    timestamp: string;
}

export const useTelemetryStore = defineStore('telemetry', () => {
    // State
    const dataPoints = ref<TelemetryData[]>([]);
    const isLoading = ref(false);

    // Computed (getters or selectors)
    const criticalCount = computed(() => {
        return dataPoints.value.filter(dp => dp.temperature > 100).length;
    });

    // Actions
    async function fetchTelemetryData() {
        isLoading.value = true;
        try {
            // simulate api call
            await new Promise(resolve => setTimeout(resolve, 1000));
            // Dummy data for illustration
            const mockData: TelemetryData = {
                vehicle_id: 'SIM-' + Math.floor(Math.random() * 100),
                temperature: 80 + Math.floor(Math.random() * 40), // 80-120 Grad
                speed: 50 + Math.floor(Math.random() * 100),
                timestamp: new Date().toISOString()
            };

            const response = await axios.post("http://0.0.0.0:6001/analyze", [mockData]);
            const analyzedData: TelemetryData = response.data;
            console.log("Analyzed Data:", analyzedData);

            // In real scenario, fetch from backend API
            // const response = await fetch('/api/telemetry');
            // dataPoints.value = await response.json();
            dataPoints.value.push(mockData);
            if (dataPoints.value.length > 20) dataPoints.value.shift(); // keep only last 20 entries

        } catch (error) {
            console.error("Failed to fetch telemetry data:", error);
        } finally {
            isLoading.value = false;
        }
    }
    return {
        dataPoints,
        isLoading,
        criticalCount,
        fetchTelemetryData
    };
});