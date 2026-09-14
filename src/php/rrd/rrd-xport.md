---
title: rrd_xport
description: Exporta la información acerca de la base de datos RRD
source_url: https://www.php.net/manual/es/function.rrd-xport.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/functions/rrd-xport.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72670
---

rrd_xport

Exporta la información acerca de la base de datos RRD

## Descripción

```php
rrd_xport(array $options): array
```php

Exporta la información sobre el archivo de base de datos RRD. Estos datos se pueden convertir a archivo XML a través del espacio de usuario PHP script y posteriormente restaurarlo de nuevo como un archivo de base de datos RRD.

## Parámetros

`options`  
Array de opciones para la exportación, consulte la página del manual rrd xport.

## Valores devueltos

Array con información sobre el fichero de base de datos RRD, o `false` si ocurre un error.
