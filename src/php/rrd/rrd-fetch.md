---
title: rrd_fetch
description: Recuperar los datos de gráfico como un array
source_url: https://www.php.net/manual/es/function.rrd-fetch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/functions/rrd-fetch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72570
---

rrd_fetch

Recuperar los datos de gráfico como un array

## Descripción

```php
rrd_fetch(string $filename, array $options): array
```php

Obtiene datos para la salida gráfica del archivo desde la base de datos RRD como un array. Esta función tiene el mismo resultado que `rrd_graph`, pero los datos obtenidos son devueltos como una matriz, no se crea el archivo de imagen.

## Parámetros

`filename`  
Nombre de archivo de la base de datos RRD.

`options`  
Array de opciones para la resolución solicitada.

## Valores devueltos

Devuelve información acerca de los datos del gráfico recuperados.
