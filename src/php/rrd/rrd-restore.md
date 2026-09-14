---
title: rrd_restore
description: Restaura el archivo RRD desde el XML dump
source_url: https://www.php.net/manual/es/function.rrd-restore.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/functions/rrd-restore.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72630
---

rrd_restore

Restaura el archivo RRD desde el XML dump

## Descripción

```php
rrd_restore(string $xml_file, string $rrd_file, [array $options]): bool
```php

Restaura el archivo RRD desde el XML dump.

## Parámetros

`xml_file`  
Nombre del archivo XML con el dump del archivo de la base de datos RRD original.

`rrd_file`  
Nombre del archivo de la base de datos RRD restaurada.

`options`  
Array de opciones para la restauración. Consulte la página de manual de restauración rrd.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
