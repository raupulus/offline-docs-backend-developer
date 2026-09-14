---
title: RRDCreator::addDataSource
description: Añade una definición de fuente de datos para la base de datos RRD
source_url: https://www.php.net/manual/es/rrdcreator.adddatasource.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/rrdcreator/adddatasource.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72700
---

RRDCreator::addDataSource

Añade una definición de fuente de datos para la base de datos RRD

## Descripción

```php
public RRDCreator::addDataSource(string $description): void
```php

RRD puede aceptar entradas desde diversas fuentes de datos (DS), es decir, tráfico entrante y saliente. Este método añade una fuente de datos mediante su descripción. Debe llamarse a este método para cada fuente de datos.

## Parámetros

`description`  
Definición de la fuente de datos (DS). El formato es idéntico a la definición de un DS en el comando de creación RRD. Consúltese la página del manual de creación RRD para más detalles.

## Valores devueltos

No se retorna ningún valor.
