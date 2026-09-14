---
title: MongoDB\Driver\Server::executeReadWriteCommand
description: Ejecuta un comando de base de datos que lee y escribe en este servidor
source_url: https://www.php.net/manual/es/mongodb-driver-server.executereadwritecommand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/executereadwritecommand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51000
---

MongoDB\Driver\Server::executeReadWriteCommand

Ejecuta un comando de base de datos que lee y escribe en este servidor

## Descripción

```php
final public MongoDB\Driver\Server::executeReadWriteCommand(string $db, MongoDB\Driver\Command $command, [array $options]): MongoDB\Driver\Cursor
```php

Ejecuta el comando en este servidor.

Este método aplicará una lógica específica a los comandos de lectura y escritura (por ejemplo [aggregate](https://www.mongodb.com/docs/manual/reference/command/aggregate/)). Los valores por omisión para las opciones `"readConcern"` y `"writeConcern"` serán deducidos de una transacción activa (indicada por la opción `"session"`), seguida de la [URI de conexión](#mongodb-driver-manager.construct-uri).

## Parámetros

`db` (`string`)  
El nombre de la base de datos sobre la cual se ejecutará el comando.

`command` (`MongoDB\Driver\Command`)  
El comando a ejecutar.

`options`  
<table>
<caption>options</caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>readConcern</td>
<td><code>MongoDB\Driver\ReadConcern</code></td>
<td><p>Una preocupación de lectura a aplicar a la operación.</p>
<p>Esta opción está disponible en MongoDB 3.2+ y se traducirá en una excepción en el momento de la ejecución si se especifica para una versión más antigua del servidor.</p></td>
</tr>
<tr>
<td>session</td>
<td><code>MongoDB\Driver\Session</code></td>
<td><p>Una sesión a asociar a la operación.</p></td>
</tr>
<tr>
<td>writeConcern</td>
<td><code>MongoDB\Driver\WriteConcern</code></td>
<td><p>Una preocupación de escritura a aplicar a la operación.</p></td>
</tr>
</tbody>
</table>

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

MongoDB\Driver\Server::executeWriteCommand

MongoDB\Driver\Manager::executeReadWriteCommand
