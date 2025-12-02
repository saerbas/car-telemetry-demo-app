package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

// define data structures as "struct"
// private fields start with lowercase letter, public fields start with uppercase letter
type TelemetryData struct {
	VehicleID string `json:"vehicle_id"`
	Speed     int    `json:"speed"`
}
type TelementryResponse struct {
	Status  string `json:"status"`
	Message string `json:"message"`
	Time    string `json:"server_time"`
}

// function to handle incoming telemetry data like controller in C#
func ingestHandler(w http.ResponseWriter, r *http.Request) {
	// set response header
	w.Header().Set("Content-Type", "application/json")

	// check if Post request
	if r.Method != http.MethodPost {
		w.WriteHeader(http.StatusMethodNotAllowed)
		json.NewEncoder(w).Encode(TelementryResponse{
			Status:  "error",
			Message: "Only Post methods are allowed",
		})
		return
	}

	// simulate data ingestion
	fmt.Println("Load data...")

	// respond to client
	response := TelementryResponse{
		Status:  "success",
		Message: "Telemetry data ingested successfully",
		Time:    time.Now().Format(time.RFC3339),
	}
	json.NewEncoder(w).Encode(response)

}

func main() {
	// define routing
	http.HandleFunc("/telemetry", ingestHandler)

	// start server
	fmt.Println("Starting server on :8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("Server failed to start:", err)
	}
}
