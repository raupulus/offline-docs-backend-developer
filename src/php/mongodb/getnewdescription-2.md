---
title: MongoDB\Driver\Monitoring\TopologyChangedEvent::getNewDescription
description: Devuelve la nueva descripción de la topología
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-topologychangedevent.getnewdescription.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/topologychangedevent/getnewdescription.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50710
---

MongoDB\Driver\Monitoring\TopologyChangedEvent::getNewDescription

Devuelve la nueva descripción de la topología

## Descripción

```php
final public MongoDB\Driver\Monitoring\TopologyChangedEvent::getNewDescription(): MongoDB\Driver\TopologyDescription
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la nueva `MongoDB\Driver\TopologyDescription` para la topología.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
