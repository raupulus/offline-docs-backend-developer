---
title: MongoDB\Driver\Server::executeCommand
description: Ejecuta un comando de base de datos en este servidor
source_url: https://www.php.net/manual/es/mongodb-driver-server.executecommand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/server/executecommand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_revision: 6047c10c1
order: 50970
---

MongoDB\Driver\Server::executeCommand

Ejecuta un comando de base de datos en este servidor

## Descripción

```php
final public MongoDB\Driver\Server::executeCommand(string $db, MongoDB\Driver\Command $command, [array $options]): MongoDB\Driver\Cursor
```php

Ejecuta un comando en este servidor.

Este método no aplica ninguna lógica especial al comando. Los valores por omisión para las opciones `"readPreference"`, `"readConcern"` y `"writeConcern"` serán deducidos de una transacción activa (indicada por la opción `"session"`). Si no hay una transacción activa, se utilizará una preferencia de lectura primaria para la selección del servidor.

Los valores por omisión *no* serán deducidos de la [URI de conexión](#mongodb-driver-manager.construct-uri). Por lo tanto, se recomienda a los usuarios utilizar métodos de comando de lectura y/o escritura específicos si es posible.

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

Lanza una excepción

MongoDB\Driver\Exception\RuntimeException

si ocurre un error (i.e. comando inválido, envío de un comando de escritura a un secundario).

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | El parámetro `options` ya no acepta instancias de `MongoDB\Driver\WriteConcern`. |
| PECL mongodb 1.21.0 | Pasar un objeto `MongoDB\Driver\ReadPreference` como `options` está obsoleto y será eliminado en la versión 2.0. |
| PECL mongodb 1.4.4 | Se lanzará `MongoDB\Driver\Exception\InvalidArgumentException` si la opción `"session"` se utiliza conjuntamente con una preocupación de escritura no reconocida. |
| PECL mongodb 1.4.0 | El tercer parámetro es ahora un array de `options`. Para la compatibilidad ascendente, este parámetro siempre aceptará un objeto `MongoDB\Driver\ReadPreference`. |

## Notas

> [!NOTE]
> Es responsabilidad del llamante asegurarse de que el servidor sea capaz de ejecutar la operación de escritura. Por ejemplo, la ejecución de una operación de escritura en un secundario (excluyendo su base de datos "local") fallará.

## Véase también

MongoDB\Driver\Command

MongoDB\Driver\Cursor

MongoDB\Driver\Server::executeReadCommand

MongoDB\Driver\Server::executeReadWriteCommand

MongoDB\Driver\Server::executeWriteCommand

MongoDB\Driver\Manager::executeCommand
