---
title: rrd_first
description: Obtiene la marca de tiempo UNIX de la primera muestra desde el archivo
  rrd
source_url: https://www.php.net/manual/es/function.rrd-first.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/functions/rrd-first.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72580
---

rrd_first

Obtiene la marca de tiempo UNIX de la primera muestra desde el archivo rrd

## Descripción

```php
rrd_first(string $file, [int $raaindex]): int
```php

Devuelve la primera muestra de datos desde la especificada RRA del archivo RRD.

## Parámetros

`file`  
Nombre del archivo de la base de datos RRD.

`raaindex`  
El índice numérico de la RRA que se va a examinar. El valor por defecto es 0.

## Valores devueltos

Número entero de timestamp Unix, o `false` si ocurre un error.
