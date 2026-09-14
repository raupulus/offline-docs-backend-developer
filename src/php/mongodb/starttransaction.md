---
title: MongoDB\Driver\Session::startTransaction
description: Inicia una transacción
source_url: https://www.php.net/manual/es/mongodb-driver-session.starttransaction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session/starttransaction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51390
---

MongoDB\Driver\Session::startTransaction

Inicia una transacción

## Descripción

```php
final public MongoDB\Driver\Session::startTransaction([array $options]): void
```php

Inicia una transacción multi-documento asociada a la sesión. En un momento dado, solo se puede tener una transacción abierta para una sesión. Después de iniciar una transacción, el objeto de sesión debe ser pasado a cada operación a través de la opción `"session"` (por ejemplo MongoDB\Driver\Manager::executeBulkWrite) para asociar esta operación a la transacción.

Las transacciones pueden ser confirmadas a través de MongoDB\Driver\Session::commitTransaction, y anuladas con MongoDB\Driver\Session::abortTransaction. Las transacciones también se anulan automáticamente cuando la sesión se cierra por la recolección de basura o al llamar explícitamente a MongoDB\Driver\Session::endSession.

## Parámetros

`options`  
Las opciones pueden ser pasadas como argumento a este método. Cada elemento de este array de opciones reemplaza la opción correspondiente de la opción `"defaultTransactionOptions"`, si se define al iniciar la sesión con MongoDB\Driver\Manager::startSession.

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
<td>maxCommitTimeMS</td>
<td>integer</td>
<td><p>El tiempo máximo en milisegundos para permitir que una sola comando <code>commitTransaction</code> se ejecute.</p>
<p>Si se especifica, <code>maxCommitTimeMS</code> debe ser un entero 32 bits con signo superior o igual a cero.</p></td>
</tr>
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
<td>writeConcern</td>
<td><code>MongoDB\Driver\WriteConcern</code></td>
<td><p>Una preocupación de escritura a aplicar a la operación.</p></td>
</tr>
</tbody>
</table>

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\CommandException

si la transacción no pudo ser iniciada debido a un problema en el lado del servidor (por ejemplo, un bloqueo no pudo ser obtenido).

Lanza una

MongoDB\Driver\Exception\RuntimeException

si la transacción no pudo ser iniciada (por ejemplo, una transacción ya estaba en curso).

## Historial de cambios

| Versión            | Descripción                                |
|--------------------|--------------------------------------------|
| PECL mongodb 1.6.0 | La opción `"maxCommitTimeMS"` fue añadida. |

## Véase también

MongoDB\Driver\Manager::startSession

MongoDB\Driver\Session::commitTransaction

MongoDB\Driver\Session::abortTransaction
