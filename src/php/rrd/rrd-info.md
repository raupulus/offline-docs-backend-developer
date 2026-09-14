---
title: rrd_info
description: Obtiene información sobre el archivo rrd
source_url: https://www.php.net/manual/es/function.rrd-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/functions/rrd-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72600
---

rrd_info

Obtiene información sobre el archivo rrd

## Descripción

```php
rrd_info(string $filename): array
```php

Devuelve información acerca sobre determinado archivo de base de datos RRD.

## Parámetros

`file`  
Nombre del archivo de base de datos RRD.

## Valores devueltos

Array con información sobre el fichero RRD solicitado, o `false` si ocurre un error.
