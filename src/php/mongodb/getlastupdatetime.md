---
title: MongoDB\Driver\ServerDescription::getLastUpdateTime
description: Devuelve la hora de la última actualización del servidor en microsegundos
source_url: https://www.php.net/manual/es/mongodb-driver-serverdescription.getlastupdatetime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/serverdescription/getlastupdatetime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51200
---

MongoDB\Driver\ServerDescription::getLastUpdateTime

Devuelve la hora de la última actualización del servidor en microsegundos

## Descripción

```php
final public MongoDB\Driver\ServerDescription::getLastUpdateTime(): int
```php

Devuelve la hora de la última actualización del servidor en microsegundos.

> [!NOTE]
> El valor devuelto es un timestamp monotónico, que comienza en un punto arbitrario. Por lo tanto, es únicamente adecuado para ser comparado con otros valores de retorno de `MongoDB\Driver\ServerDescription::getLastUpdateTime`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la hora de la última actualización del servidor en microsegundos.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
