#!/bin/bash

echo "[$(date)] - Iniciando proceso de recreación con Docker Compose"

DOCKER_COMPOSE_FILE="docker-compose.yml"

echo "[$(date)] - Deteniendo y eliminando servicios existentes"
docker compose -f "$DOCKER_COMPOSE_FILE" down || {
    echo "[$(date)] - Error al detener servicios"
    exit 1
}

echo "[$(date)] - Recreando y levantando servicios"
docker compose -f "$DOCKER_COMPOSE_FILE" up -d --build || {
    echo "[$(date)] - Error al recrear servicios"
    exit 1
}

echo "[$(date)] - Proceso de recreación completado con éxito"