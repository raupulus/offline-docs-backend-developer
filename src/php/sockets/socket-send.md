---
title: socket_send
description: Envía datos a un socket conectado
source_url: https://www.php.net/manual/es/function.socket-send.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-send.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75790
---

socket_send

Envía datos a un socket conectado

## Descripción

```php
socket_send(Socket $socket, string $data, int $length, int $flags): int
```php

La función `socket_send` envía `length` bytes al socket `socket` desde el buffer `data`.

## Parámetros

`socket`  
Una instancia de `Socket` creada por `socket_create` o `socket_accept`.

`data`  
Un buffer que contiene los datos que serán enviados al host remoto.

`length`  
El número de bytes que deben ser enviados al host remoto desde el buffer `data`.

`flags`  
El valor del parámetro `flags` puede ser una combinación de los siguientes flags, unidos por un OR a nivel de bits (`|`).

|  |  |
|----|----|
| `MSG_OOB` | Trata los datos OOB (out-of-band). |
| `MSG_EOR` | Indica un marcador de registro. Los datos enviados completan el registro. |
| `MSG_EOF` | Termina el envío a través del socket e incluye una notificación apropiada al final de los datos enviados. Los datos enviados completan la transacción. |
| `MSG_DONTROUTE` | Ignora el enrutamiento, utiliza una interfaz directa. |

Valores posibles para `flags`

## Valores devueltos

Devuelve el número de bytes enviados, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `socket` ahora es una instancia de `Socket` ; anteriormente, era un `resource`. |

## Véase también

`socket_sendto`
