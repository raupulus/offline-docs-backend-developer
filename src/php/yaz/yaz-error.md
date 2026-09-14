---
title: yaz_error
description: Devuelve la descripción del error
source_url: https://www.php.net/manual/es/function.yaz-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107820
---

yaz_error

Devuelve la descripción del error

## Descripción

```php
yaz_error(resource $id): string
```php

`yaz_error` retorna un mensaje textual en Inglés correspondiente al último error numérico como devuelto por `yaz_errno`.

## Parámetros

`id`  
El recurso de conexión retornado por `yaz_connect`.

## Valores devueltos

Devuelve un mensaje textual por el servidor (último requerimiento), identificado por el parámetro `id`. Una cadenma vacia es retornada si la última operación fue satisfactoria.

## Véase también

`yaz_errno`, `yaz_addinfo`
