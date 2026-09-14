---
title: RRDCreator::addArchive
description: Añade RRA - archivo de valores de datos para cada fuente de datos
source_url: https://www.php.net/manual/es/rrdcreator.addarchive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/rrdcreator/addarchive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72690
---

RRDCreator::addArchive

Añade RRA - archivo de valores de datos para cada fuente de datos

## Descripción

```php
public RRDCreator::addArchive(string $description): void
```php

Añade definición RRA por descripción de archivo. Archivo consta de un número de valores de datos o estadísticas para cada una de las fuentes de datos definidas (DS). Las fuentes de datos son definidos a través del método RRDCreator::addDataSource. Es necesario llamar a este método para cada archivo solicitado.

## Parámetros

`description`  
Definición del archivo - RRA. Esta tiene el mismo formato que la definición RRA en el comando rrd create. Ver página de manual de rrd create para obtener más detalles.

## Valores devueltos

No se retorna ningún valor.
