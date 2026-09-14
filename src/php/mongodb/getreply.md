---
title: MongoDB\Driver\Monitoring\CommandFailedEvent::getReply
description: Devuelve el documento de respuesta del comando
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandfailedevent.getreply.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandfailedevent/getreply.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49950
---

MongoDB\Driver\Monitoring\CommandFailedEvent::getReply

Devuelve el documento de respuesta del comando

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandFailedEvent::getReply(): object
```php

El documento de respuesta será convertido de BSON a PHP utilizando las reglas de [deserialización](#mongodb.persistence.deserialization) por omisión (por ejemplo, los documentos BSON serán convertidos en `stdClass`).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el documento de respuesta del comando en forma de un objeto `stdClass`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también
