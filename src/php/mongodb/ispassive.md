---
title: MongoDB\Driver\Server::isPassive
description: Verifica si el servidor es un miembro pasivo del conjunto de réplicas
source_url: https://www.php.net/manual/es/mongodb-driver-server.ispassive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/ispassive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51110
---

MongoDB\Driver\Server::isPassive

Verifica si el servidor es un miembro pasivo del conjunto de réplicas

## Descripción

```php
final public MongoDB\Driver\Server::isPassive(): bool
```php

Devuelve si el servidor es un [miembro pasivo](https://www.mongodb.com/docs/manual/reference/glossary/#term-passive-member) de un conjunto de réplicas (i.e. su prioridad es `0`).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el servidor es un miembro pasivo de un conjunto de réplicas, y `false` en caso contrario.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Server::getInfo
