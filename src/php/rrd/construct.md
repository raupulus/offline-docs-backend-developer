---
title: RRDCreator::__construct
description: Crea una nueva instancia RRDCreator
source_url: https://www.php.net/manual/es/rrdcreator.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/rrdcreator/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72710
---

RRDCreator::\_\_construct

Crea una nueva instancia

RRDCreator

## Descripción

```php
public RRDCreator::__construct(string $path, [string $startTime], [int $step])
```php

Crea una nueva instancia `RRDCreator`.

## Parámetros

`path`  
Ruta de acceso al nuevo fichero de base de datos RRD creado.

`startTime`  
Fecha/hora para el primer valor de la base de datos RRD. Este argumento admite todos los formatos que son admitidos por la llamada de creación RRD.

int`step`  
Intervalo base, en segundos, de inserción de datos en la base de datos RRD.
