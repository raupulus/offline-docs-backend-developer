---
title: MongoDB\Driver\Monitoring\ServerChangedEvent::getNewDescription
description: Devuelve la nueva descripción del servidor
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-serverchangedevent.getnewdescription.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/serverchangedevent/getnewdescription.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50410
---

MongoDB\Driver\Monitoring\ServerChangedEvent::getNewDescription

Devuelve la nueva descripción del servidor

## Descripción

```php
final public MongoDB\Driver\Monitoring\ServerChangedEvent::getNewDescription(): MongoDB\Driver\ServerDescription
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la nueva `MongoDB\Driver\ServerDescription` del servidor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
