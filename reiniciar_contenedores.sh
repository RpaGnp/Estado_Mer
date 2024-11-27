#!/bin/bash

echo "[$(date)] - Iniciando proceso de recreación con Docker Compose"

# Ruta al archivo docker-compose.yml (ajústala según sea necesario)
DOCKER_COMPOSE_FILE="docker-compose.yml"

# Pasos para eliminar y recrear los contenedores
echo "[$(date)] - Deteniendo y eliminando servicios existentes"
docker-compose -f "$DOCKER_COMPOSE_FILE" down || {
    echo "[$(date)] - Error al detener servicios"
    exit 1
}

echo "[$(date)] - Recreando y levantando servicios"
docker-compose -f "$DOCKER_COMPOSE_FILE" up -d || {
    echo "[$(date)] - Error al recrear servicios"
    exit 1
}

echo "[$(date)] - Proceso de recreación completado con éxito"
