---
title: rrd_create
description: Crea un archivo de base de datos rrd
source_url: https://www.php.net/manual/es/function.rrd-create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/functions/rrd-create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72550
---

rrd_create

Crea un archivo de base de datos rrd

## Descripción

```php
rrd_create(string $filename, array $options): bool
```php

Crea el archivo de base de datos RDD.

## Parámetros

`filename`  
Nombre de archivo para el nuevo archivo de base de datos rrd.

`options`  
Opciones para la creación del archivo de base de datos rrd - lista de cadenas. Ver página de manual de creación de archivos de base de datos rrd para obtener una lista completa de opciones.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
