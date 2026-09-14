---
title: MongoDB\Driver\Monitoring\LogSubscriber::log
description: Método de notificación para un mensaje de registro
source_url: https://www.php.net/manual/es/mongodb-driver-monitoring-logsubscriber.log.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/monitoring/logsubscriber/log.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50280
---

MongoDB\Driver\Monitoring\LogSubscriber::log

Método de notificación para un mensaje de registro

## Descripción

```php
abstract public MongoDB\Driver\Monitoring\LogSubscriber::log(int $level, string $domain, string $message): void
```php

Si el observador está registrado, este método es llamado para cada mensaje de registro registrado.

## Parámetros

`level`  
El nivel de gravedad. Será uno de los [constantes de interfaz](#mongodb-driver-monitoring-logsubscriber.constants).

`domain`  
El nombre del componente del controlador que emitió el mensaje de registro.

`message`  
El mensaje de registro.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Monitoring\addSubscriber
