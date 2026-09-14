---
title: socket_create
description: Crea un socket
source_url: https://www.php.net/manual/es/function.socket-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 890cc22d3
order: 75650
---

socket_create

Crea un socket

## Descripción

```php
socket_create(int $domain, int $type, int $protocol): Socket
```php

`socket_create` crea un punto de comunicación (un socket) y devuelve una instancia de `Socket` Una conexión típica de red está compuesta por dos sockets: uno que actúa como cliente y otro como servidor.

## Parámetros

`domain`  
El argumento `domain` especifica la familia de protocolos a utilizar por el socket.

| Dominio | Descripción |
|----|----|
| `AF_INET` | Protocolo basado en IPv4. TCP y UDP son los protocolos comunes de esta familia de protocolos. |
| `AF_INET6` | Protocolo basado en IPv6. TCP y UDP son los protocolos comunes de esta familia de protocolos. El soporte fue añadido en PHP 5.0.0. |
| `AF_UNIX` | Familia de protocolos de comunicación local. El alto rendimiento y los menores costos adicionales lo hacen una gran fuerza de IPC (`Interprocess Communication`). |

Familia de direcciones / protocolos disponibles

`type`  
El argumento `type` selecciona el tipo de comunicación a utilizar por el socket.

| Tipo | Descripción |
|----|----|
| `SOCK_STREAM` | Proporciona flujos de bytes ordenados, fiables, full-duplex, conectados en base. Un mecanismo de transmisión de datos "`out-of-band`" puede ser soportado. El protocolo TCP se basa en este tipo de sockets. |
| `SOCK_DGRAM` | Soporte para datagramas (menos conexión, mensaje no garantizado de longitud máxima fija). El protocolo UDP se basa en este tipo de sockets. |
| `SOCK_SEQPACKET` | Proporciona un camino de transmisión de datos secuencial, fiable, conectado en base por dos caminos para los datagramas de longitud máxima fija; un consumidor es requerido para leer la totalidad de un paquete con cada llamada a la lectura. |
| `SOCK_RAW` | Proporciona acceso bruto de protocolo de red. Este tipo especial de socket puede ser utilizado para construir manualmente cualquier tipo de protocolo. Un uso común de este tipo de sockets es el procesamiento de las peticiones ICMP (como el ping). |
| `SOCK_RDM` | Proporciona una capa fiable de datagrama que no garantiza el orden de los datos. Este tipo de socket es el más probable de no estar implementado en su sistema operativo. |

Tipos de sockets disponibles

`protocol`  
El argumento `protocol` define el protocolo específico para el dominio `domain` a utilizar durante las comunicaciones en un socket devuelto. El valor apropiado puede ser encontrado por su nombre utilizando la función `getprotobyname`. Si el protocolo deseado es TCP o UDP, las constantes correspondientes `SOL_TCP` y `SOL_UDP` pueden ser utilizadas.

| Nombre | Descripción |
|----|----|
| `icmp` | El protocolo ICMP (`Internet Control Message Protocol`) es utilizado primero por las pasarelas y los hosts para reportar errores en comunicaciones de datagrama. El comando "`ping`" (presente en los sistemas modernos) es un ejemplo de aplicación utilizando el protocolo ICMP. |
| `udp` | El protocolo UDP (`User Datagramm Protocol`) es un protocolo sin conexión, incierto con longitudes de registros fijas. Por lo tanto, `UDP` requiere una cantidad mínima de protocolo aéreo. |
| `tcp` | El protocolo TCP (`Transmission Control Protocol`) es un protocolo fiable, conectado en base, orientado a flujo y full-duplex. `TCP` garantiza que cada paquete es recibido en el orden en que fue enviado. Si algunos paquetes se pierden durante la comunicación, `TCP` retransmitirá estos paquetes hasta que el host destinatario los haya recibido completamente. Por razones de fiabilidad y rendimiento, la implementación `TCP`, ella misma, decide las fronteras apropiadas de bytes de la capa fundamental de comunicación del datagrama. Por lo tanto, las aplicaciones `TCP` deben permitir la posibilidad de transmisión parcial de registros. |

Protocolos Comunes

## Valores devueltos

`socket_create` devuelve una instancia de `Socket` en caso de éxito y `false` en caso contrario. El código de error generado puede ser obtenido llamando a la función `socket_last_error`. Este código de error puede ser pasado a la función `socket_strerror` para obtener un mensaje de error legible por humanos.

## Errores/Excepciones

Si un valor inválido es especificado en el argumento `domain` o en el argumento `type`, la función `socket_create` tomará como argumentos por defecto respectivamente `AF_INET` y `SOCK_STREAM` y generará un mensaje de advertencia (`E_WARNING`).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora admite la creación de sockets de la familia `AF_PACKET`. |
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `Socket`; anteriormente, se devolvía un `resource`. |

## Véase también

`socket_accept`, `socket_bind`, `socket_connect`, `socket_listen`, `socket_last_error`, `socket_strerror`
