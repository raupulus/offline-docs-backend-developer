---
title: MongoDB\Driver\Monitoring\CommandSucceededEvent::getServiceId
description: Devuelve el identificador del servicio del balanceador de carga para
  la orden
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandsucceededevent.getserviceid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandsucceededevent/getserviceid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50260
---

MongoDB\Driver\Monitoring\CommandSucceededEvent::getServiceId

Devuelve el identificador del servicio del balanceador de carga para la orden

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandSucceededEvent::getServiceId(): MongoDB\BSON\ObjectId
```php

Cuando el controlador está conectado a un clúster MongoDB a través de un balanceador de carga, el identificador del servicio corresponde al campo `serviceId` en la respuesta de la orden `hello`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador del servicio del balanceador de carga, o `null` si el controlador no está conectado a un balanceador de carga.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
