---
title: MongoDB\Driver\Monitoring\CommandFailedEvent::getDatabaseName
description: Devuelve el nombre de la base de datos sobre la cual se ejecutó el comando
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandfailedevent.getdatabasename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandfailedevent/getdatabasename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49890
---

MongoDB\Driver\Monitoring\CommandFailedEvent::getDatabaseName

Devuelve el nombre de la base de datos sobre la cual se ejecutó el comando

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandFailedEvent::getDatabaseName(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la base de datos sobre la cual se ejecutó el comando.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también
