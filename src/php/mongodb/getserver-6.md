---
title: MongoDB\Driver\Session::getServer
description: Devuelve el servidor al que esta sesión está fijada
source_url: https://www.php.net/manual/es/mongodb-driver-session.getserver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/getserver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51340
---

MongoDB\Driver\Session::getServer

Devuelve el servidor al que esta sesión está fijada

## Descripción

```php
final public MongoDB\Driver\Session::getServer(): MongoDB\Driver\Server
```php

Devuelve el `MongoDB\Driver\Server` al que esta sesión está fijada. Si la sesión no está fijada a un servidor, `null` será devuelto.

La fijación de la sesión se utiliza principalmente para las transacciones distribuidas, ya que todas las órdenes en una transacción distribuida deben ser enviadas a la misma instancia mongos. Este método está destinado a ser utilizado por bibliotecas construidas sobre la extensión para permitir el uso de un servidor fijado en lugar de invocar la selección del servidor.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el `MongoDB\Driver\Server` al que esta sesión está fijada, o `null` si la sesión no está fijada a un servidor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.
