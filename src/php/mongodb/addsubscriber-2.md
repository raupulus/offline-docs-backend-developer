---
title: MongoDB\Driver\Manager::addSubscriber
description: Registra un observador de eventos de monitoreo con este manager
source_url: https://www.php.net/manual/es/mongodb-driver-manager.addsubscriber.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/addsubscriber.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49690
---

MongoDB\Driver\Manager::addSubscriber

Registra un observador de eventos de monitoreo con este manager

## Descripción

```php
final public MongoDB\Driver\Manager::addSubscriber(MongoDB\Driver\Monitoring\Subscriber $subscriber): void
```php

Registra un observador de eventos de monitoreo con este Manager. El observador será notificado de todos los eventos para este Manager.

> [!NOTE]
> Si `subscriber` ya está registrado con este manager, esta función no hace nada. Si `subscriber` también está registrado globalmente, solo será notificado una vez de cada evento para este manager.

## Parámetros

`subscriber` (`MongoDB\Driver\Monitoring\Subscriber`)  
Un observador de eventos de monitoreo a registrar con este Manager.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\InvalidArgumentException

si

subscriber

es un

MongoDB\Driver\Monitoring\LogSubscriber

, ya que los observadores solo pueden ser registrados globalmente.

## Véase también

MongoDB\Driver\Manager::removeSubscriber

MongoDB\Driver\Monitoring\Subscriber

MongoDB\Driver\Monitoring\CommandSubscriber

MongoDB\Driver\Monitoring\addSubscriber
