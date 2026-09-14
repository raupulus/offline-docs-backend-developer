---
title: socket_addrinfo_explain
description: Proporciona información sobre addrinfo
source_url: https://www.php.net/manual/es/function.socket-addrinfo-explain.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-addrinfo-explain.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 7ba008401
order: 75550
---

socket_addrinfo_explain

Proporciona información sobre addrinfo

## Descripción

```php
socket_addrinfo_explain(AddressInfo $address): array
```php

`socket_addrinfo_explain` expone la estructura `addrinfo` subyacente.

## Parámetros

`address`  
Una instancia de `AddressInfo` creada por `socket_addrinfo_lookup`.

## Valores devueltos

Devuelve un array que contiene los campos de la estructura `addrinfo`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `address` ahora es una instancia de `AddressInfo` ; anteriormente, era un `resource`. |

## Véase también

`socket_addrinfo_bind`, `socket_addrinfo_connect`, `socket_addrinfo_lookup`
