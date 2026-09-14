---
title: MongoDB\Driver\Manager::startSession
description: Inicia una nueva sesión de cliente para ser utilizada con este cliente
source_url: https://www.php.net/manual/es/mongodb-driver-manager.startsession.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/startsession.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 49860
---

MongoDB\Driver\Manager::startSession

Inicia una nueva sesión de cliente para ser utilizada con este cliente

## Descripción

```php
final public MongoDB\Driver\Manager::startSession([array $options]): MongoDB\Driver\Session
```php

Crear una `MongoDB\Driver\Session` para las opciones dadas. La sesión puede luego ser especificada durante la ejecución de comandos, consultas y operaciones de escritura.

> [!NOTE]
> Una `MongoDB\Driver\Session` solo puede ser utilizada con el `MongoDB\Driver\Manager` desde el cual fue creada.

## Parámetros

`options`  
<table>
<caption>options</caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
<th>Por defecto</th>
</tr>
</thead>
<tbody>
<tr>
<td>causalConsistency</td>
<td><code>bool</code></td>
<td><p>Configura la coherencia causal en una sesión. Si <code>true</code>, cada operación en la sesión será ordenada de manera causal después de la operación de lectura o escritura previa. Definir a <code>false</code> para desactivar la coherencia causal.</p>
<p>Ver <a href="https://www.mongodb.com/docs/manual/core/read-isolation-consistency-recency/#causal-consistency">Consistencia causal</a> en el manual de MongoDB para más información.</p></td>
<td><code>true</code></td>
</tr>
<tr>
<td>defaultTransactionOptions</td>
<td><code>array</code></td>
<td><p>Las opciones por defecto a aplicar a las transacciones recién creadas. Estas opciones se utilizan a menos que sean reemplazadas cuando una transacción es iniciada con un valor diferente para cada opción.</p>
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
<p>Esta opción está disponible en MongoDB 4.0+.</p></td>
<td><code>[]</code></td>
</tr>
<tr>
<td>snapshot</td>
<td><code>bool</code></td>
<td><p>Configura las lecturas instantáneas en una sesión. Si <code>true</code>, un timestamp será obtenido de la primera operación de lectura soportada en la sesión (es decir, <code>find</code>, <code>aggregate</code>, o <code>distinct</code> no fragmentado). Las operaciones de lectura posteriores en la sesión utilizarán luego un nivel de coherencia de lectura <code>"snapshot"</code> para leer datos mayoritariamente comprometidos desde ese timestamp. Definir a <code>false</code> para desactivar las lecturas instantáneas.</p>
<p>Las lecturas instantáneas requieren MongoDB 5.0+ y no pueden ser utilizadas con la coherencia causal, transacciones o operaciones de escritura. Si <code>"snapshot"</code> es <code>true</code>, <code>"causalConsistency"</code> será por defecto <code>false</code>.</p>
<p>Ver <a href="https://www.mongodb.com/docs/manual/reference/read-concern-snapshot/#read-concern-and-atclustertime">Read Concern "instantáneas"</a> en el manual de MongoDB para más información.</p></td>
<td><code>false</code></td>
</tr>
</tbody>
</table>

## Valores devueltos

Devuelve una `MongoDB\Driver\Session`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una

MongoDB\Driver\Exception\InvalidArgumentException

si las opciones

"causalConsistency"

y

"snapshot"

son ambas

true

.

Lanza una

MongoDB\Driver\Exception\RuntimeException

si la sesión no puede ser creada (por ejemplo, libmongoc no soporta el cifrado).

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.11.0 | La opción `"snapshot"` fue añadida. |
| PECL mongodb 1.6.0 | La opción `"maxCommitTimeMS"` fue añadida a `"defaultTransactionOptions"`. |
| PECL mongodb 1.5.0 | La opción `"defaultTransactionOptions"` fue añadida. |

## Véase también

MongoDB\Driver\Session

Consistencia causal

en el manual de MongoDB
