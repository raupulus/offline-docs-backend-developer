---
title: rrd_last
description: Obtiene la marca de tiempo UNIX de la última muestra
source_url: https://www.php.net/manual/es/function.rrd-last.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/functions/rrd-last.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72610
---

rrd_last

Obtiene la marca de tiempo UNIX de la última muestra

## Descripción

```php
rrd_last(string $filename): int
```php

Devuelve la marca de tiempo UNIX (UNIX timestamp) de la actualización más reciente de la base de datos RRD.

## Parámetros

`filename`  
Nombre de archivo de la base de datos RRD.

## Valores devueltos

Devuelve un número entero como marca de tiempo Unix de los datos más recientes de la base de datos RRD.
