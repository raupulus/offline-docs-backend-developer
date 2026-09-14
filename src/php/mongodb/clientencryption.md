---
title: La clase MongoDB\Driver\ClientEncryption
source_url: https://www.php.net/manual/es/class.mongodb-driver-clientencryption.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/clientencryption.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49210
---

## Introducción

La clase `MongoDB\Driver\ClientEncryption` gestiona la creación de claves de datos para la cifrado lado-cliente, así como el cifrado y descifrado manual de valores.

## Sinopsis de la clase

MongoDB\Driver\ClientEncryption

final

MongoDB\Driver\ClientEncryption

Constantes

const

string

MongoDB\Driver\ClientEncryption::AEAD_AES_256_CBC_HMAC_SHA_512_DETERMINISTIC

AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic

const

string

MongoDB\Driver\ClientEncryption::AEAD_AES_256_CBC_HMAC_SHA_512_RANDOM

AEAD_AES_256_CBC_HMAC_SHA_512-Random

const

string

MongoDB\Driver\ClientEncryption::ALGORITHM_INDEXED

Indexed

const

string

MongoDB\Driver\ClientEncryption::ALGORITHM_UNINDEXED

Unindexed

const

string

MongoDB\Driver\ClientEncryption::ALGORITHM_RANGE

Range

const

string

MongoDB\Driver\ClientEncryption::QUERY_TYPE_EQUALITY

equality

const

string

MongoDB\Driver\ClientEncryption::QUERY_TYPE_RANGE

range

Métodos

## Constantes predefinidas

`MongoDB\Driver\ClientEncryption::AEAD_AES_256_CBC_HMAC_SHA_512_DETERMINISTIC`  
Especifica un algoritmo para el [cifrado determinista](https://www.mongodb.com/docs/manual/core/csfle/fundamentals/encryption-algorithms/#deterministic-encryption), que es adecuado para consultas.

`MongoDB\Driver\ClientEncryption::AEAD_AES_256_CBC_HMAC_SHA_512_RANDOM`  
Especifica un algoritmo para el [cifrado aleatorio](https://www.mongodb.com/docs/manual/core/csfle/fundamentals/encryption-algorithms/#randomized-encryption)

`MongoDB\Driver\ClientEncryption::ALGORITHM_INDEXED`  
Especifica un algoritmo para un contenido cifrado indexado, que puede usarse con cifrado consultable.

Para insertar o consultar con un contenido cifrado indexado, el `MongoDB\Driver\Manager` debe configurarse con la opción de controlador `"autoEncryption"`. La opción de auto-cifrado `"bypassQueryAnalysis"` puede ser `true`. La opción de auto-cifrado `"bypassAutoEncryption"` debe ser `false`.

`MongoDB\Driver\ClientEncryption::ALGORITHM_UNINDEXED`  
Especifica un algoritmo para un contenido cifrado no indexado.

`MongoDB\Driver\ClientEncryption::ALGORITHM_RANGE`  
Especifica un algoritmo para un contenido cifrado de rango, que puede usarse con cifrado consultable.

Para consultar con un contenido cifrado de rango, el `MongoDB\Driver\Manager` debe configurarse con la opción de controlador `"autoEncryption"`. La opción de auto-cifrado `"bypassQueryAnalysis"` puede ser `true`. La opción de auto-cifrado `"bypassAutoEncryption"` debe ser `false`.

> [!NOTE]
> La extensión aún no admite consultas de rango para tipos de campo BSON Decimal128.

`MongoDB\Driver\ClientEncryption::QUERY_TYPE_EQUALITY`  
Especifica un tipo de consulta de igualdad, que se usa en conjunto con `MongoDB\Driver\ClientEncryption::ALGORITHM_INDEXED`.

`MongoDB\Driver\ClientEncryption::QUERY_TYPE_RANGE`  
Especifica un tipo de consulta de rango, que se usa en conjunto con `MongoDB\Driver\ClientEncryption::ALGORITHM_RANGE`.

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
<td><p>Se eliminó <code>MongoDB\Driver\ClientEncryption::ALGORITHM_RANGE_PREVIEW</code> y <code>MongoDB\Driver\ClientEncryption::QUERY_TYPE_RANGE_PREVIEW</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.20.0</td>
<td><p>Se añadió <code>MongoDB\Driver\ClientEncryption::ALGORITHM_RANGE</code> y <code>MongoDB\Driver\ClientEncryption::QUERY_TYPE_RANGE</code>.</p>
<p>Se declaró obsoleto <code>MongoDB\Driver\ClientEncryption::ALGORITHM_RANGE_PREVIEW</code> y <code>MongoDB\Driver\ClientEncryption::QUERY_TYPE_RANGE_PREVIEW</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.16.0</td>
<td>Se añadió <code>MongoDB\Driver\ClientEncryption::ALGORITHM_RANGE_PREVIEW</code> y <code>MongoDB\Driver\ClientEncryption::QUERY_TYPE_RANGE_PREVIEW</code>.</td>
</tr>
<tr>
<td>PECL mongodb 1.14.0</td>
<td>Se añadió <code>MongoDB\Driver\ClientEncryption::ALGORITHM_INDEXED</code>, <code>MongoDB\Driver\ClientEncryption::ALGORITHM_UNINDEXED</code>, y <code>MongoDB\Driver\ClientEncryption::QUERY_TYPE_EQUALITY</code>.</td>
</tr>
</tbody>
</table>

## Véase también

MongoDB\Driver\Manager::createClientEncryption
