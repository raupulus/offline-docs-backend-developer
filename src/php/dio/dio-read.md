---
title: dio_read
description: Leer bytes de un descriptor de fichero
source_url: https://www.php.net/manual/es/function.dio-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dio/functions/dio-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dio
translation_status: ready
translation_revision: 96c9d88ba
order: 11880
---

dio_read

Leer bytes de un descriptor de fichero

## Descripción

```php
dio_read(resource $fd, [int $len]): string
```php

La función `dio_read` lee y devuelve `len` bytes de fichero con descriptor `fd`.

## Parámetros

`fd`  
El fichero descriptor devuelto por`dio_open`.

`len`  
El número de bytes a leer. Si no se especifica la lectura es de bloques de 1K `dio_read`

## Valores devueltos

La bytes leídos desde `fd`.

## Véase también

`dio_write`
