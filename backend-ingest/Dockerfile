# Go image
FROM golang:1.21-alpine AS builder

# Set working directory
WORKDIR /app

# Copy go.mod and go.sum files
COPY go.mod ./

# Download dependencies
RUN go mod download

# Copy the source code
COPY . .

# Build the Go application
RUN go build -o backend-ingest main.go

# Final stage
FROM alpine:latest

WORKDIR /root/

# Copy the built binary from the builder stage
COPY --from=builder /app/backend-ingest .

# Expose port 8080
EXPOSE 8080

# Command to run the executable
CMD ["./backend-ingest"]