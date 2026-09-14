---
title: rrd_graph
description: Crea la imagen de un conjunto de datos
source_url: https://www.php.net/manual/es/function.rrd-graph.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/functions/rrd-graph.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72590
---

rrd_graph

Crea la imagen de un conjunto de datos

## Descripción

```php
rrd_graph(string $filename, array $options): array
```php

Crea la imagen de un conjunto de datos particulares desde el archivo de RRD.

## Parámetros

`filename`  
El nombre del archivo de salida del gráfico. Este generalmente tiene una terminación `.png`, `.svg` o `.eps`, dependiendo del formato de salida que desee.

`options`  
Las opciones para la generación de la imagen. Consulte la página del manual de gráficos rrd para conocer todas las posibles opciones. Todas las opciones (definiciones de datos, definiciones de variables, etc.) son permitidas.

## Valores devueltos

Array con información sobre la imagen generada es devuelto, o `false` si ocurre un error.
