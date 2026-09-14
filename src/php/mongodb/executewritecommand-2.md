---
title: MongoDB\Driver\Server::executeWriteCommand
description: Ejecuta un comando de base de datos que escribe en este servidor
source_url: https://www.php.net/manual/es/mongodb-driver-server.executewritecommand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/executewritecommand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51010
---

MongoDB\Driver\Server::executeWriteCommand

Ejecuta un comando de base de datos que escribe en este servidor

## Descripción

```php
final public MongoDB\Driver\Server::executeWriteCommand(string $db, MongoDB\Driver\Command $command, [array $options]): MongoDB\Driver\Cursor
```php

Ejecuta el comando en este servidor.

Este método aplicará una lógica específica a los comandos que escriben (por ejemplo [drop](https://www.mongodb.com/docs/manual/reference/command/drop/)). El valor por omisión para la opción `"writeConcern"` será deducido de una transacción activa (indicada por la opción `"session"`), seguida de la [URI de conexión](#mongodb-driver-manager.construct-uri).

> [!NOTE]
> Este método no está destinado a ser utilizado para ejecutar [insert](https://www.mongodb.com/docs/manual/reference/command/insert/), [update](https://www.mongodb.com/docs/manual/reference/command/update/), o [delete](https://www.mongodb.com/docs/manual/reference/command/delete/) comandos. Se recomienda a los usuarios utilizar `MongoDB\Driver\Server::executeBulkWrite` para estas operaciones.

## Parámetros

`db` (`string`)  
El nombre de la base de datos sobre la cual se ejecutará el comando.

`command` (`MongoDB\Driver\Command`)  
El comando a ejecutar.

`options`  
| Opción | Tipo | Descripción |
|----|----|----|
| session | `MongoDB\Driver\Session` | Una sesión a asociar a la operación. |
| writeConcern | `MongoDB\Driver\WriteConcern` | Una preocupación de escritura a aplicar a la operación. |

options

> [!WARNING]
> Si se utiliza una `"session"` que tiene una transacción en curso, no se puede especificar la opción `"readConcern"` o `"writeConcern"`. Intentar hacer esto lanzará una excepción `MongoDB\Driver\Exception\InvalidArgumentException` . En su lugar, debe definir estas opciones cuando se crea la transacción con MongoDB\Driver\Session::startTransaction.

## Valores devueltos

Retorna un `MongoDB\Driver\Cursor` en caso de éxito.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si la opción

"session"

se utiliza con una transacción asociada en combinación con una opción

"readConcern"

o

"writeConcern"

.

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

Lanza una

MongoDB\Driver\Exception\RuntimeException

en caso de otros errores (por ejemplo: comando inválido).

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.4.4 | Una `MongoDB\Driver\Exception\InvalidArgumentException` será lanzada si la opción `"session"` es utilizada en combinación con un writeConcern no reconocido. |

## Notas

> [!NOTE]
> Es responsabilidad del llamante asegurarse de que el servidor sea capaz de ejecutar la operación de escritura. Por ejemplo, la ejecución de una operación de escritura en un secundario (excluyendo su base de datos "local") fallará.

## Véase también

MongoDB\Driver\Command

MongoDB\Driver\Cursor

MongoDB\Driver\Server::executeCommand

MongoDB\Driver\Server::executeReadCommand

MongoDB\Driver\Server::executeReadWriteCommand

MongoDB\Driver\Manager::executeWriteCommand
