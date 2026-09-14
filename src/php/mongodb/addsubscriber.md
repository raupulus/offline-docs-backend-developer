---
title: MongoDB\Driver\Monitoring\addSubscriber
description: Registra un suscriptor de eventos de monitorización de forma global
source_url: https://www.php.net/manual/es/function.mongodb.driver.monitoring.addsubscriber.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/functions/driver/monitoring/addsubscriber.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48810
---

MongoDB\Driver\Monitoring\addSubscriber

Registra un suscriptor de eventos de monitorización de forma global

## Descripción

```php
MongoDB\Driver\Monitoring\addSubscriber(MongoDB\Driver\Monitoring\Subscriber $subscriber): void
```php

Registra un suscriptor de eventos de monitorización de forma global. El suscriptor será notificado de todos los eventos en la extensión para cualquier Manager.

> [!NOTE]
> Si el `subscriber` ya está registrado de forma global, esta función no realiza ninguna acción. Si el `subscriber` también está registrado con uno o más Managers, solo será notificado una vez de cada evento para cada Manager.

## Parámetros

`subscriber` (`MongoDB\Driver\Monitoring\Subscriber`)  
Un suscriptor de eventos de monitorización para registrar de forma global.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\removeSubscriber

MongoDB\Driver\Monitoring\Subscriber

MongoDB\Driver\Monitoring\CommandSubscriber

MongoDB\Driver\Manager::addSubscriber
