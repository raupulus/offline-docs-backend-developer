---
title: dio_truncate
description: Trunca un descriptor de fichero fd a un determinado número de bytes
source_url: https://www.php.net/manual/es/function.dio-truncate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dio/functions/dio-truncate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dio
translation_status: ready
translation_revision: 96c9d88ba
order: 11920
---

dio_truncate

Trunca un descriptor de fichero fd a un determinado número de bytes

## Descripción

```php
dio_truncate(resource $fd, int $offset): bool
```php

`dio_truncate` trunca un fichero a, como mucho, un tamaño de `offset` bytes.

Si el fichero excediera este tamaño, el contenido extra se perdería. Si fuera inferior en tamaño, no se especifica si el fichero se mantiene sin cambios o si se completa. En este último caso, la parte completada se haría con ceros.

## Parámetros

`fd`  
Descriptor de fichero devuelto por `dio_open`.

`offset`  
Tamaño en bytes.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Notas

> [!NOTE]
> Esta función no está implementada en las plataformas Windows.
