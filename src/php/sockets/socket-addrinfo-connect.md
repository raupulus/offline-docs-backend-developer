---
title: socket_addrinfo_connect
description: Crea e inicia la conexión de un socket a una dirección dada
source_url: https://www.php.net/manual/es/function.socket-addrinfo-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-addrinfo-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 7ba008401
order: 75540
---

socket_addrinfo_connect

Crea e inicia la conexión de un socket a una dirección dada

## Descripción

```php
socket_addrinfo_connect(AddressInfo $address): Socket
```php

Crea una instancia de `Socket` y la conecta a la `AddressInfo` proporcionada. El valor de retorno de esta función puede ser utilizado con el resto de las funciones de socket.

## Parámetros

`address`  
La instancia de `AddressInfo` creada por `socket_addrinfo_lookup`.

## Valores devueltos

Devuelve una instancia de `Socket` en caso de éxito o `false` en caso de fallo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | En caso de éxito, esta función devuelve ahora una instancia de `Socket`; antes, se devolvía un `resource`. |
| 8.0.0 | `address` ahora es una instancia de `AddressInfo` ; anteriormente, era un `resource`. |

## Véase también

`socket_addrinfo_bind`, `socket_addrinfo_explain`, `socket_addrinfo_lookup`
