---
title: MongoDB\Driver\Monitoring\CommandFailedEvent::getServiceId
description: Devuelve el identificador del servicio del equilibrador de carga para
  la comanda
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-commandfailedevent.getserviceid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/commandfailedevent/getserviceid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49990
---

MongoDB\Driver\Monitoring\CommandFailedEvent::getServiceId

Devuelve el identificador del servicio del equilibrador de carga para la comanda

## Descripción

```php
final public MongoDB\Driver\Monitoring\CommandFailedEvent::getServiceId(): MongoDB\BSON\ObjectId
```php

Cuando el controlador está conectado a un clúster MongoDB a través de un equilibrador de carga, el identificador del servicio corresponde al campo `serviceId` en la respuesta de la comanda `hello`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el identificador del servicio del equilibrador de carga, o `null` si el controlador no está conectado a un equilibrador de carga.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
