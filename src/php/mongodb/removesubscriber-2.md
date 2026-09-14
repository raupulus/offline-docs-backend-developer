---
title: MongoDB\Driver\Manager::removeSubscriber
description: Elimina un observador de eventos de supervisión de este Manager
source_url: https://www.php.net/manual/es/mongodb-driver-manager.removesubscriber.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/removesubscriber.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49840
---

MongoDB\Driver\Manager::removeSubscriber

Elimina un observador de eventos de supervisión de este Manager

## Descripción

```php
final public MongoDB\Driver\Manager::removeSubscriber(MongoDB\Driver\Monitoring\Subscriber $subscriber): void
```php

Elimina un observador de eventos de supervisión de este Manager.

> [!NOTE]
> Si `subscriber` no está ya registrado con este Manager, esta función no hace nada.

## Parámetros

`subscriber` (`MongoDB\Driver\Monitoring\Subscriber`)  
Un observador de eventos de supervisión a eliminar de este Manager.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Manager::addSubscriber

MongoDB\Driver\Monitoring\Subscriber

MongoDB\Driver\Monitoring\CommandSubscriber

MongoDB\Driver\Monitoring\removeSubscriber
