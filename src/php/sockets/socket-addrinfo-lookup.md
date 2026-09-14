---
title: socket_addrinfo_lookup
description: Devuelve un array que contiene la información de getaddrinfo sobre el
  nombre de host dado
source_url: https://www.php.net/manual/es/function.socket-addrinfo-lookup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-addrinfo-lookup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 890cc22d3
order: 75560
---

socket_addrinfo_lookup

Devuelve un array que contiene la información de getaddrinfo sobre el nombre de host dado

## Descripción

```php
socket_addrinfo_lookup(string $host, [string $service], [array $hints]): array
```php

Busca las diferentes formas de conectarse a `host`. El array devuelto contiene un conjunto de instancias de `AddressInfo` a las cuales se puede vincular utilizando `socket_addrinfo_bind`.

## Parámetros

`host`  
El nombre de host a buscar.

`service`  
El servicio al cual conectarse. Si service es una cadena numérica, designa el puerto. De lo contrario, designa un nombre de servicio de red, que es mapeado a un puerto por el sistema operativo.

`hints`  
Permite especificar criterios para la selección de las direcciones devueltas. Se pueden especificar los hints tal como se definen en getaddrinfo.

## Valores devueltos

Devuelve un array de instancias de `AddressInfo` que pueden ser utilizadas con la familia de funciones `socket_addrinfo_*`. En caso de fallo, `false` es devuelto.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Ahora lanza un TypeError si algún valor del array `hints` no puede ser convertido a int, y puede lanzar un ValueError si alguno de esos valores produce un desbordamiento. |
| 8.0.0 | En caso de éxito, esta función devuelve ahora un array de instancias de `AddressInfo`; antes, se devolvía un array de `resource`s. |
| 8.0.0 | `service` ahora es nullable. |

## Véase también

`socket_addrinfo_bind`, `socket_addrinfo_connect`, `socket_addrinfo_explain`
