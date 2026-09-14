---
title: MongoDB\Driver\Server::__construct
description: Crear un nuevo servidor (no utilizado)
source_url: https://www.php.net/manual/es/mongodb-driver-server.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50940
---

MongoDB\Driver\Server::\_\_construct

Crear un nuevo servidor (no utilizado)

## Descripción

```php
final private MongoDB\Driver\Server::__construct()
```php

Los objetos `MongoDB\Driver\Server` son creados internamente por `MongoDB\Driver\Manager` cuando se establece una conexión de base de datos y pueden ser devueltos por `MongoDB\Driver\Manager::getServers` y `MongoDB\Driver\Manager::selectServer`.

## Parámetros

Esta función no contiene ningún parámetro.

## Véase también

MongoDB\Driver\Manager::getServers

MongoDB\Driver\Manager::selectServer
