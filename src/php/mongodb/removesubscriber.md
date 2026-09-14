---
title: MongoDB\Driver\Monitoring\removeSubscriber
description: Deregistra un suscriptor de eventos de supervisión globalmente
source_url: https://www.php.net/manual/es/function.mongodb.driver.monitoring.removesubscriber.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/functions/driver/monitoring/removesubscriber.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48820
---

MongoDB\Driver\Monitoring\removeSubscriber

Deregistra un suscriptor de eventos de supervisión globalmente

## Descripción

```php
MongoDB\Driver\Monitoring\removeSubscriber(MongoDB\Driver\Monitoring\Subscriber $subscriber): void
```php

Deregistra un suscriptor de eventos de supervisión globalmente.

> [!NOTE]
> Si el `subscriber` no está registrado globalmente, esta función no realiza ninguna acción.

## Parámetros

`subscriber` (`MongoDB\Driver\Monitoring\Subscriber`)  
Un suscriptor de eventos de supervisión que se desregistrará globalmente.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\addSubscriber

MongoDB\Driver\Monitoring\Subscriber

MongoDB\Driver\Monitoring\CommandSubscriber

MongoDB\Driver\Manager::removeSubscriber
