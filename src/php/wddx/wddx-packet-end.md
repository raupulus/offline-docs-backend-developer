---
title: wddx_packet_end
description: Cierra un paquete WDDX con el ID especificado
source_url: https://www.php.net/manual/es/function.wddx-packet-end.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wddx/functions/wddx-packet-end.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wddx
translation_status: ready
translation_revision: fc74d0ee2
order: 101220
---

wddx_packet_end

Cierra un paquete WDDX con el ID especificado

> [!WARNING]
> Esta función ha sido *ELIMINADA* a partir de PHP 7.4.0.

## Descripción

```php
wddx_packet_end(resource $packet_id): string
```php

Cierra y devuelve un paquete WDDX dado.

## Parámetros

`packet_id`  
Un paquete WDDX, devuelto por la función `wddx_packet_start`.

## Valores devueltos

Devuelve un `string` que contiene el paquete WDDX.
