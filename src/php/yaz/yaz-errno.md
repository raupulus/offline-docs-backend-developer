---
title: yaz_errno
description: Devuelve el número de error
source_url: https://www.php.net/manual/es/function.yaz-errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107810
---

yaz_errno

Devuelve el número de error

## Descripción

```php
yaz_errno(resource $id): int
```php

Devuelve un número de error del servidor (la última solicitud) identificado por `id`.

`yaz_errno` debe ser llamado después de la actividad de red para cada servidor - (después del retorno de `yaz_wait`) para determinar el éxito o el fracaso de la última operación (p. ej. búsqueda).

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

## Valores devueltos

Devuelve un código de error. El código de error es un código de diagnóstico Z39.50 (por lo general un diagnóstico de Bib-1) o el código de error del lado del cliente que es generado por PHP/YAZ, como "Error de conexión", "Init rechazado", etc

## Véase también

`yaz_error`, `yaz_addinfo`
