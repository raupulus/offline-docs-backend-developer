---
title: rrd_lastupdate
description: Obtiene información sobre los últimos datos actualizados
source_url: https://www.php.net/manual/es/function.rrd-lastupdate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/functions/rrd-lastupdate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72620
---

rrd_lastupdate

Obtiene información sobre los últimos datos actualizados

## Descripción

```php
rrd_lastupdate(string $filename): array
```php

Obtiene un array de la marca de tiempo UNIX y de los valores almacenados para cada fecha en la actualización más reciente del archivo de base de datos RRD.

## Parámetros

`file`  
Nombre del archivo de la base de datos RRD.

## Valores devueltos

Array de información sobre la última actualización, o `false` si ocurre un error.
