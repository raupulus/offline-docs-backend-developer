---
title: MongoDB\Driver\Server::isPrimary
description: Verifica si este servidor es un miembro principal de un conjunto de réplicas
source_url: https://www.php.net/manual/es/mongodb-driver-server.isprimary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/isprimary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51120
---

MongoDB\Driver\Server::isPrimary

Verifica si este servidor es un miembro principal de un conjunto de réplicas

## Descripción

```php
final public MongoDB\Driver\Server::isPrimary(): bool
```php

Devuelve si este servidor es un [miembro principal](https://www.mongodb.com/docs/manual/reference/glossary/#term-primary) de un conjunto de réplicas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si este servidor es un miembro principal de un conjunto de réplicas, y `false` en caso contrario.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Server::getInfo
