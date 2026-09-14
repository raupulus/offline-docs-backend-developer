---
title: dio_write
description: Escribe datos en el descriptor de fichero con un truncado opcional
source_url: https://www.php.net/manual/es/function.dio-write.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dio/functions/dio-write.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dio
translation_status: ready
translation_revision: 96c9d88ba
order: 11930
---

dio_write

Escribe datos en el descriptor de fichero con un truncado opcional

## Descripción

```php
dio_write(resource $fd, string $data, [int $len]): int
```php

`dio_write` escriba hasta `len` bytes de `data` al fichero `fd`.

## Parámetros

`fd`  
Descriptor de fichero devuelto por `dio_open`.

`data`  
Datos a escribir.

`len`  
Longitud en bytes de los datos a escribir. Si no se especifica, la función escribe todos los datos al fichero especificado.

## Valores devueltos

Devuelve el número de bytes escritos en `fd`.

## Véase también

`dio_read`
