---
title: MongoDB\Driver\Monitoring\SDAMSubscriber::serverChanged
description: Método de notificación para un cambio de descripción de servidor
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-sdamsubscriber.serverchanged.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/sdamsubscriber/serverchanged.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50300
---

MongoDB\Driver\Monitoring\SDAMSubscriber::serverChanged

Método de notificación para un cambio de descripción de servidor

## Descripción

```php
abstract public MongoDB\Driver\Monitoring\SDAMSubscriber::serverChanged(MongoDB\Driver\Monitoring\ServerChangedEvent $event): void
```php

Si un observador está registrado, este método es llamado cuando una descripción de servidor cambia. Por ejemplo, el tipo de un servidor pasando de secundario a primario resultaría en un cambio de la descripción de ese servidor.

## Parámetros

`event` (`MongoDB\Driver\Monitoring\ServerChangedEvent`)  
Un objeto de evento que encapsula información sobre la descripción de servidor modificada.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\ServerChangedEvent

MongoDB\Driver\Monitoring\addSubscriber

MongoDB\Driver\Manager::addSubscriber
