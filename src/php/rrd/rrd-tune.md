---
title: rrd_tune
description: Cambia algunas opciones de cabecera del archivo de base de datos RRD
  database
source_url: https://www.php.net/manual/es/function.rrd-tune.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/functions/rrd-tune.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72640
---

rrd_tune

Cambia algunas opciones de cabecera del archivo de base de datos RRD database

## Descripción

```php
rrd_tune(string $filename, array $options): bool
```php

Cambia algunas opciones de cabecera del archivo de base de datos RRD. Por ejemplo, cambia el nombre de la fuente de los datos, etc

## Parámetros

`filename`  
Nombre de archivo de la base de datos RRD.

`options`  
Opciones con las propiedades del archivo de la base de datos RDD que serán cambiadas. Consulte la página del manual rrd tune para mayor detalle.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
