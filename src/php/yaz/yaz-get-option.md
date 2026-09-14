---
title: yaz_get_option
description: Devuelve el valor de opción para la conexión
source_url: https://www.php.net/manual/es/function.yaz-get-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-get-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107850
---

yaz_get_option

Devuelve el valor de opción para la conexión

## Descripción

```php
yaz_get_option(resource $id, string $name): string
```php

Devuelve el valor de la opción especificada con `name`.

## Parámetros

`id`  
El recurso de conexión retornado por `yaz_connect`.

`name`  
La opción del nombre.

## Valores devueltos

Devuelve el valor de la opción especificada o una cadena vacía si la opción wno está establecida.

## Véase también

La descripción de `yaz_set_option` para las opciones disponibles
