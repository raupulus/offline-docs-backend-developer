---
title: rrd_update
description: Actualizar la base de datos RRD
source_url: https://www.php.net/manual/es/function.rrd-update.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/functions/rrd-update.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72650
---

rrd_update

Actualizar la base de datos RRD

## Descripción

```php
rrd_update(string $filename, array $options): bool
```php

Actualiza el archivo de base de datos RRD. Los datos de entrada es el tiempo interpolado de acuerdo con las propiedades del archivo de base de datos RRD.

## Parámetros

`filename`  
Nombre de archivo de la base de datos RRD. Esta base de datos será actualizada.

`options`  
Opciones para actualizar la base de datos RRD. Esta es una lista de cadenas. Ver página del manual de actualización rrd para conocer el listado de opciones.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
