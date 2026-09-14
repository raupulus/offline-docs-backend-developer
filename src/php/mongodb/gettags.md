---
title: MongoDB\Driver\Server::getTags
description: Devuelve un array de tags que describen este servidor en un conjunto
  de réplicas
source_url: https://www.php.net/manual/es/mongodb-driver-server.gettags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/gettags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51070
---

MongoDB\Driver\Server::getTags

Devuelve un array de tags que describen este servidor en un conjunto de réplicas

## Descripción

```php
final public MongoDB\Driver\Server::getTags(): array
```php

Devuelve un `array` de [tags](https://www.mongodb.com/docs/manual/reference/glossary/#term-tag) utilizados para describir este servidor en un conjunto de réplicas. El array contendrá cero o más pares clave y valor de tipo `string`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `array` de tags utilizados para describir este servidor en un conjunto de réplicas.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Server::getInfo
