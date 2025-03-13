# Servidor y Cliente TCP para Ejecución Remota de Comandos

## Descripción

Este repositorio contiene dos scripts en Python que implementan una comunicación TCP para la ejecución remota de comandos:
- **servidorTCP.py**: Actúa como servidor, escucha en el puerto designado y envía comandos al cliente.
- **clienteTCP.py**: Se conecta al servidor, recibe comandos, los ejecuta y devuelve los resultados.

Estos scripts son ideales para aprender sobre redes y comunicación en Python, y sirven como base para comprender cómo se pueden implementar controles remotos. **¡Úsalos siempre en entornos controlados y con fines educativos!**

## Contenido del Repositorio

- **servidorTCP.py**  
  - Escucha en todas las interfaces (`0.0.0.0`) en el puerto `4444`.
  - Envía un mensaje de bienvenida al cliente.
  - Permite ingresar comandos desde la consola, enviándolos al cliente y mostrando la respuesta.
  
- **clienteTCP.py**  
  - Se conecta al servidor en la IP y puerto especificados.
  - Recibe comandos, los ejecuta en la máquina local y envía el resultado de vuelta al servidor.

## Requisitos

- Python 3.x
- Conexión de red entre las máquinas (o una misma máquina usando diferentes terminales).
- Permisos para ejecutar comandos en el sistema.

## Uso

### 1. Configuración

- Verifica que la dirección IP y el puerto sean correctos para tu entorno:
  - En `servidorTCP.py`, se utiliza `HOST = "0.0.0.0"` para escuchar en todas las interfaces.
  - En `clienteTCP.py`, asegúrate de que `HOST` apunte a la IP del servidor.
  
### 2. Ejecución del Servidor

Abre una terminal en la máquina que actuará como servidor y ejecuta:

```bash
python3 servidorTCP.py
