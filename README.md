# Chat Punto a Punto en Python

Este proyecto implementa un chat básico en Python utilizando sockets, que permite la comunicación punto a punto entre dos clientes (Cliente 1 y Cliente 2) a través de un servidor.

## Estructura del Proyecto

- `servidor.py`: Código del servidor que gestiona las conexiones y la comunicación entre los clientes.
- `cliente1.py`: Código del Cliente 1 que se conecta al servidor y permite enviar y recibir mensajes.
- `cliente2.py`: Código del Cliente 2 que se conecta al servidor y permite enviar y recibir mensajes.

## Funcionamiento del Chat

1. **Servidor**: 
   - El servidor se ejecuta primero y se queda a la espera de conexiones de clientes.
   - Una vez que ambos clientes están conectados, el servidor redirige los mensajes entre ellos.

2. **Clientes**:
   - Cada cliente se conecta al servidor y puede enviar mensajes.
   - Cuando un cliente envía un mensaje, el servidor lo recibe y lo retransmite al otro cliente.
