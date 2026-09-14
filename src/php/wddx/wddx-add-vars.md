---
title: wddx_add_vars
description: Se utiliza para añadir variables a un paquete WDDX con el ID especificado
source_url: https://www.php.net/manual/es/function.wddx-add-vars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wddx/functions/wddx-add-vars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wddx
translation_status: ready
translation_revision: 9e0f03ac3
order: 101200
---

wddx_add_vars

Se utiliza para añadir variables a un paquete WDDX con el ID especificado

> [!WARNING]
> Esta función ha sido *ELIMINADA* a partir de PHP 7.4.0.

## Descripción

```php
wddx_add_vars(resource $packet_id, mixed $var_name, mixed ...$var_names): bool
```php

Serializa las variables pasadas y añade el resultado al paquete dado.

## Parámetros

Esta función acepta un número variable de argumentos.

`packet_id`  
Un paquete WDDX, devuelto por la función `wddx_packet_start`.

`var_name`  
Puede ser una `string` que nombre una variable o un array que contenga nombres de variables o de otros arrays, etc..

`var_names`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
