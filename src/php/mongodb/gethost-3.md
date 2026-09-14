---
title: MongoDB\Driver\Monitoring\CommandSucceededEvent::getHost
description: Devuelve el nombre de host del servidor para el comando
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandsucceededevent.gethost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandsucceededevent/gethost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50190
---

MongoDB\Driver\Monitoring\CommandSucceededEvent::getHost

Devuelve el nombre de host del servidor para el comando

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandSucceededEvent::getHost(): string
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre de host del servidor en el que se ejecutó el comando.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
