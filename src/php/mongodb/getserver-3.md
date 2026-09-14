---
title: MongoDB\Driver\Monitoring\CommandFailedEvent::getServer
description: Devuelve el servidor en el cual se ejecutó el comando
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandfailedevent.getserver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandfailedevent/getserver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49970
---

MongoDB\Driver\Monitoring\CommandFailedEvent::getServer

Devuelve el servidor en el cual se ejecutó el comando

> [!WARNING]
> Este método ha sido *DEPRECADO* a partir de la versión 1.20.0 de la extensión y ha sido eliminado en la versión 2.0. Las aplicaciones deben utilizar MongoDB\Driver\Monitoring\CommandFailedEvent::getHost y MongoDB\Driver\Monitoring\CommandFailedEvent::getPort en su lugar.

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandFailedEvent::getServer(): MongoDB\Driver\Server
```php

Devuelve el `MongoDB\Driver\Server` en el cual se ejecutó el comando.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el `MongoDB\Driver\Server` en el cual se ejecutó el comando.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

| Versión            | Descripción                    |
|--------------------|--------------------------------|
| PECL mongodb 2.0.0 | Este método ha sido eliminado. |

## Véase también

MongoDB\Driver\Monitoring\CommandStartedEvent::getServer
