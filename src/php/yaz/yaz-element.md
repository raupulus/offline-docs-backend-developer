---
title: yaz_element
description: Especifica el nombre del elemento establecido para recuperar
source_url: https://www.php.net/manual/es/function.yaz-element.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-element.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107800
---

yaz_element

Especifica el nombre del elemento establecido para recuperar

## Descripción

```php
yaz_element(resource $id, string $elementset): bool
```php

Esta función especifica el nombre del elemento establecido para recuperar.

Llama esta función antes de `yaz_search` o `yaz_present` para especificar el nombre del elemento establecido para los registros a ser recuperados.

> [!NOTE]
> Si la función parece no tener efecto, ve la descripción de la opción `piggybacking` en `yaz_connect`.

## Parámetros

`id`  
El recurso de conexión retornado por `yaz_connect`.

`elementset`  
Más servidores soportan `F` (para registros completos) y `B` (para registros breves).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
