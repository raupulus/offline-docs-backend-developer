---
title: La clase MongoDB\BSON\ObjectId
source_url: https://www.php.net/manual/es/class.mongodb-bson-objectid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/objectid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48060
---

## Introducción

Tipo BSON para un [ObjectId](https://www.mongodb.com/docs/manual/reference/bson-types/#objectid). El valor se compone de 12 bytes, donde los primeros cuatro bytes son un timestamp que refleja la creación del ObjectId. Más precisamente, el valor se compone de :

- un valor de 4 bytes representando los segundos desde la época UNIX,

- un número aleatorio de 5 bytes único a una máquina y un proceso, y

- un contador de 3 bytes, comenzando por un valor aleatorio.

En MongoDB, cada documento almacenado en una colección requiere un campo `_id` único que actúa como clave primaria. Si un documento insertado omite el campo `_id`, la extensión genera automáticamente un ObjectId para el campo `_id`.

El uso de ObjectId para el campo `_id` proporciona las siguientes ventajas adicionales:

- La hora de creación del ObjectId puede ser accedida utilizando el método MongoDB\BSON\ObjectId::getTimestamp.

- La ordenación en un campo `_id` que almacena valores ObjectId equivale aproximadamente a la ordenación por fecha de creación.

## Sinopsis de la clase

MongoDB\BSON\ObjectId

final

MongoDB\BSON\ObjectId

MongoDB\BSON\ObjectIdInterface

MongoDB\BSON\Type

JsonSerializable

Stringable

Métodos

## Historial de cambios

<table role="class">
<thead>
<tr>
<th>Versión</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>PECL mongodb 2.0.0</td>
<td><p>Esta clase ya no implementa la interfaz Serializable.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.12.0</td>
<td>Implementa Stringable para PHP 8.0+.</td>
</tr>
<tr>
<td>PECL mongodb 1.3.0</td>
<td><p>Renombrado de <code>MongoDB\BSON\ObjectID</code> a <code>MongoDB\BSON\ObjectId</code>.</p>
<p>Implementa MongoDB\BSON\ObjectIdInterface.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.2.0</td>
<td>Implementa Serializable y JsonSerializable.</td>
</tr>
</tbody>
</table>
