---
title: MongoDB\Driver\Monitoring\CommandStartedEvent::getCommandName
description: Devuelve el nombre del comando
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandstartedevent.getcommandname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandstartedevent/getcommandname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50020
---

MongoDB\Driver\Monitoring\CommandStartedEvent::getCommandName

Devuelve el nombre del comando

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandStartedEvent::getCommandName(): string
```php

Devuelve el nombre del comando (por ejemplo, `"find"`, `"aggregate"`).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el nombre del comando.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también
