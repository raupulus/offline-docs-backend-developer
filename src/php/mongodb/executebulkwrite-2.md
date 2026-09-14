---
title: MongoDB\Driver\Server::executeBulkWrite
description: Ejecuta una o varias operaciones de escritura en este servidor
source_url: https://www.php.net/manual/es/mongodb-driver-server.executebulkwrite.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/executebulkwrite.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 50950
---

MongoDB\Driver\Server::executeBulkWrite

Ejecuta una o varias operaciones de escritura en este servidor

## Descripción

```php
final public MongoDB\Driver\Server::executeBulkWrite(string $namespace, MongoDB\Driver\BulkWrite $bulk, [array $options]): MongoDB\Driver\WriteResult
```php

Ejecuta una o varias operaciones de escritura en este servidor.

Un objeto `MongoDB\Driver\BulkWrite` puede ser construido con una o varias operaciones de diferentes tipos (i.e. actualización, eliminación, e inserción). El driver intentará enviar las operaciones del mismo tipo al servidor en un mínimo de solicitudes posibles para optimizar los viajes de ida y vuelta.

El valor por omisión para la opción `"writeConcern"` será deducido de una transacción activa (indicada por la opción `"session"`), luego por el [URI de conexión](#mongodb-driver-manager.construct-uri).

## Parámetros

`namespace` (`string`)  
Un espacio de nombres completamente calificado (ej. `"databaseName.collectionName"`)

`bulk` (`MongoDB\Driver\BulkWrite`)  
Escritura(s) a ejecutar.

`options`  
| Opción | Tipo | Descripción |
|----|----|----|
| session | `MongoDB\Driver\Session` | Una sesión a asociar a la operación. |
| writeConcern | `MongoDB\Driver\WriteConcern` | Una preocupación de escritura a aplicar a la operación. |

options

## Valores devueltos

Retorna un `MongoDB\Driver\WriteResult` en caso de éxito.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si

bulk

no contiene ninguna operación de escritura.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si

bulk

ya ha sido ejecutado. Los objetos

MongoDB\Driver\BulkWrite

no pueden ser ejecutados varias veces.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si la opción

"session"

se utiliza junto con una preocupación de escritura no reconocida.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\ConnectionException

si la conexión al servidor falla por una razón distinta a un problema de identificación

Lanza una excepción

MongoDB\Driver\Exception\AuthenticationException

si se requiere una identificación pero falla

Lanza una excepción

MongoDB\Driver\Exception\BulkWriteException

en caso de error de una operación de escritura (un error WriteError y WriteConcern)

Lanza una excepción

MongoDB\Driver\Exception\RuntimeException

si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | El parámetro `options` ya no acepta instancias `MongoDB\Driver\WriteConcern`. |
| PECL mongodb 1.21.0 | Pasar un objeto `MongoDB\Driver\WriteConcern` como `options` está obsoleto y será eliminado en la 2.0. |
| PECL mongodb 1.4.4 | `MongoDB\Driver\Exception\InvalidArgumentException` será lanzado si la opción `"session"` es utilizada conjuntamente con una preocupación de escritura no reconocida. |
| PECL mongodb 1.4.0 | El tercer parámetro es ahora un array de `options`. Para la compatibilidad ascendente, este parámetro siempre aceptará un objeto `MongoDB\Driver\WriteConcern`. |
| PECL mongodb 1.3.0 | `MongoDBDriverExceptionInvalidArgumentException` es ahora lanzado si `Bulk` no contiene operaciones de escritura. Anteriormente, una `MongoDB\Driver\Exception\BulkWriteException` era lanzada. |

## Notas

> [!NOTE]
> Es responsabilidad del llamante asegurarse de que el servidor sea capaz de ejecutar la operación de escritura. Por ejemplo, la ejecución de una operación de escritura en un secundario (excluyendo su base de datos "local") fallará.

## Véase también

MongoDB\Driver\BulkWrite

MongoDB\Driver\WriteResult

MongoDB\Driver\WriteConcern

MongoDB\Driver\Manager::executeBulkWrite
