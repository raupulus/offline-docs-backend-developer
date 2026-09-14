---
title: RRDGraph::saveVerbose
description: Guarda una consulta de base de datos RRD en la imagen y devuelve las
  informaciones verbosas sobre el gráfico generado.
source_url: https://www.php.net/manual/es/rrdgraph.saveverbose.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/rrdgraph/saveverbose.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72760
---

RRDGraph::saveVerbose

Guarda una consulta de base de datos RRD en la imagen y devuelve las informaciones verbosas sobre el gráfico generado.

## Descripción

```php
public RRDGraph::saveVerbose(): array
```php

Guarda la consulta de base de datos RRD en el fichero de imagen definido por el método RRDGraph::\_\_construct y devuelve las informaciones verbosas sobre el gráfico generado; si "-" es utilizado como nombre de fichero de imagen, los datos de la imagen serán también devueltos en el array resultante.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array que contiene las informaciones detalladas sobre la imagen generada, o `false` si ocurre un error.
