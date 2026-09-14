---
title: MongoDB\Driver\Server::executeReadCommand
description: Ejecuta un comando de base de datos que lee en este servidor
source_url: https://www.php.net/manual/es/mongodb-driver-server.executereadcommand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/executereadcommand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 50990
---

MongoDB\Driver\Server::executeReadCommand

Ejecuta un comando de base de datos que lee en este servidor

## Descripción

```php
final public MongoDB\Driver\Server::executeReadCommand(string $db, MongoDB\Driver\Command $command, [array $options]): MongoDB\Driver\Cursor
```php

Ejecuta el comando en este servidor, independientemente de la opción `"readPreference"`.

Este método aplicará una lógica específica a los comandos de lectura (por ejemplo [distinct](https://www.mongodb.com/docs/manual/reference/command/distinct/)). Los valores por omisión para las opciones `"readPreference"` y `"readConcern"` serán deducidos de una transacción activa (indicada por la opción `"session"`), seguida de la [URI de conexión](#mongodb-driver-manager.construct-uri).

> [!NOTE]
> La opción `"readPreference"` no controla el servidor hacia el cual el controlador emite la operación; siempre se ejecutará en este objeto servidor. En su lugar, puede ser utilizado al emitir la operación a un secundario (desde una conexión de conjunto de réplicas, no autónoma) o el nodo Mongos para asegurarse de que el controlador defina el protocolo de fila en consecuencia o añada la preferencia de lectura a la operación, respectivamente.

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
<td>readPreference</td>
<td><code>MongoDB\Driver\ReadPreference</code></td>
<td><p>Una preferencia de lectura a utilizar para seleccionar un servidor para la operación.</p></td>
</tr>
<tr>
<td>session</td>
<td><code>MongoDB\Driver\Session</code></td>
<td><p>Una sesión a asociar a la operación.</p></td>
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

## Véase también

MongoDB\Driver\Command

MongoDB\Driver\Cursor

MongoDB\Driver\Server::executeCommand

MongoDB\Driver\Server::executeReadWriteCommand

MongoDB\Driver\Server::executeWriteCommand

MongoDB\Driver\Manager::executeReadCommand
