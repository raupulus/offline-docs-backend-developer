---
title: MongoDB\Driver\Monitoring\CommandStartedEvent::getDatabaseName
description: Devuelve la base de datos sobre la cual se ejecutó el comando
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandstartedevent.getdatabasename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandstartedevent/getdatabasename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50030
---

MongoDB\Driver\Monitoring\CommandStartedEvent::getDatabaseName

Devuelve la base de datos sobre la cual se ejecutó el comando

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandStartedEvent::getDatabaseName(): string
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
