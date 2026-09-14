---
title: MongoDB\Driver\Server::isSecondary
description: Verifica si este servidor es un miembro secundario de un conjunto de
  réplicas
source_url: https://www.php.net/manual/es/mongodb-driver-server.issecondary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/issecondary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51130
---

MongoDB\Driver\Server::isSecondary

Verifica si este servidor es un miembro secundario de un conjunto de réplicas

## Descripción

```php
final public MongoDB\Driver\Server::isSecondary(): bool
```php

Devuelve si este servidor es un [miembro secundario](https://www.mongodb.com/docs/manual/reference/glossary/#term-secondary) de un conjunto de réplicas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si este servidor es un miembro secundario de un conjunto de réplicas, y `false` en caso contrario.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Server::getInfo
