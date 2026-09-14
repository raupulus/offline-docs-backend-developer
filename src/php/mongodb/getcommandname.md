---
title: MongoDB\Driver\Monitoring\CommandFailedEvent::getCommandName
description: Devuelve el nombre de la orden
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandfailedevent.getcommandname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandfailedevent/getcommandname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49880
---

MongoDB\Driver\Monitoring\CommandFailedEvent::getCommandName

Devuelve el nombre de la orden

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandFailedEvent::getCommandName(): string
```php

Devuelve el nombre de la orden (por ejemplo `"find"`, `"aggregate"`).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre de la orden.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también
