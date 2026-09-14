---
title: MongoDB\Driver\Monitoring\CommandFailedEvent::getError
description: Devuelve la excepción asociada al comando fallido
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandfailedevent.geterror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandfailedevent/geterror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49910
---

MongoDB\Driver\Monitoring\CommandFailedEvent::getError

Devuelve la excepción asociada al comando fallido

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandFailedEvent::getError(): Exception
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la `Exception` asociada al comando fallido.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también
