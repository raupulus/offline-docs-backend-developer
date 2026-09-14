---
title: wddx_deserialize
description: Deserializa un paquete WDDX
source_url: https://www.php.net/manual/es/function.wddx-deserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wddx/functions/wddx-deserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wddx
translation_status: ready
translation_revision: fc74d0ee2
order: 101210
---

wddx_deserialize

Deserializa un paquete WDDX

> [!WARNING]
> Esta función ha sido *ELIMINADA* a partir de PHP 7.4.0.

## Descripción

```php
wddx_deserialize(string $packet): mixed
```php

Deserializa un paquete `packet` WDDX.

> [!WARNING]
> No se debe pasar entrada de usuario no verificada a `wddx_deserialize`. La deserialización puede hacer que el código sea cargado y ejecutado durante la instancia y el autocargado del objeto, y un usuario malintencionado puede ser capaz de alojar un exploit. Utilice un formato seguro, estándar de intercambio de datos como JSON (usando `json_decode` y `json_encode`) si se deben pasar datos serializados al usuario.

## Parámetros

`packet`  
Un paquete WDDX, en forma de `string` o de flujo.

## Valores devueltos

Devuelve el valor deserializado, que puede ser un `string`, un número o un array. Observe que las estructuras son deserializadas en arrays asociativos.
