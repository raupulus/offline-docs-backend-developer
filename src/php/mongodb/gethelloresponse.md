---
title: MongoDB\Driver\ServerDescription::getHelloResponse
description: Devuelve la respuesta "hello" más reciente del servidor
source_url: https://www.php.net/manual/es/mongodb-driver-serverdescription.gethelloresponse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/serverdescription/gethelloresponse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51180
---

MongoDB\Driver\ServerDescription::getHelloResponse

Devuelve la respuesta "hello" más reciente del servidor

## Descripción

```php
final public MongoDB\Driver\ServerDescription::getHelloResponse(): array
```php

Devuelve un array de información que describe el servidor. Este array se deriva de la respuesta [hello](https://www.mongodb.com/docs/manual/reference/command/hello/) más reciente (en el momento en que la `MongoDB\Driver\ServerDescription` fue construida) obtenida a través de [la supervisión del servidor](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md).

> [!NOTE]
> Cuando el controlador está conectado a un balanceador de carga, este método devolverá un array vacío porque los balanceadores de carga no son supervisados. Esto contrasta con `MongoDB\Driver\Server::getInfo`, que devolvería la respuesta del [hello](https://www.mongodb.com/docs/manual/reference/command/hello/) de la comando de apretón de manos de conexión inicial del servidor base.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array de información que describe este servidor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Véase también

MongoDB\Driver\Server::getInfo

hello

comando en el manual de MongoDB

Descubrimiento y supervisión de servidores
