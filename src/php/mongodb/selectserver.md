---
title: MongoDB\Driver\Manager::selectServer
description: Selecciona un servidor correspondiente a una preferencia de lectura
source_url: https://www.php.net/manual/es/mongodb-driver-manager.selectserver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/selectserver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49850
---

MongoDB\Driver\Manager::selectServer

Selecciona un servidor correspondiente a una preferencia de lectura

## Descripción

```php
final public MongoDB\Driver\Manager::selectServer([MongoDB\Driver\ReadPreference $readPreference]): MongoDB\Driver\Server
```php

Selecciona un `MongoDB\Driver\Server` correspondiente a `readPreference`. Si `readPreference` es `null` o se omite, el servidor primario será seleccionado por omisión. Esto puede ser utilizado para preseleccionar un servidor a fin de realizar una verificación de versión antes de ejecutar una operación.

> [!NOTE]
> A diferencia de `MongoDB\Driver\Manager::getServers`, este método inicializará las conexiones de base de datos y realizará el descubrimiento de servidores si es necesario. Ver la [Especificación de selección de servidor](https://github.com/mongodb/specifications/blob/master/source/server-selection/server-selection.md#single-threaded-server-selection) para más información.

## Parámetros

`readPreference` (`MongoDB\Driver\ReadPreference`)  
Las preferencias de lectura a utilizar para seleccionar un servidor. Si `null` o se omite, el servidor primario será seleccionado por omisión.

## Valores devueltos

Devuelve un `MongoDB\Driver\Server` correspondiente a la preferencia de lectura.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\ConnectionException

si la conexión al servidor falla por una razón distinta a un problema de identificación

Lanza una excepción

MongoDB\Driver\Exception\AuthenticationException

si se requiere una identificación pero falla

Lanza una

MongoDB\Driver\Exception\RuntimeException

si un servidor correspondiente a la preferencia de lectura no ha podido ser encontrado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.11.0 | El `readPreference` es ahora opcional. Si `null` o se omite, el servidor primario será seleccionado por omisión. |

## Véase también

MongoDB\Driver\Server

MongoDB\Driver\Manager::getServers

Especificación de selección de servidor
