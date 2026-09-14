---
title: MongoDB\Driver\ClientEncryption::encrypt
description: Cifra un valor
source_url: https://www.php.net/manual/es/mongodb-driver-clientencryption.encrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/clientencryption/encrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49140
---

MongoDB\Driver\ClientEncryption::encrypt

Cifra un valor

## Descripción

```php
final public MongoDB\Driver\ClientEncryption::encrypt(mixed $value, [array $options]): MongoDB\BSON\Binary
```php

Cifra el valor.

## Parámetros

`value`  
El valor a cifrar. Cualquier valor que pueda insertarse en MongoDB puede cifrarse utilizando este método.

`options`  
<table>
<caption>Opciones de cifrado</caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>algorithm</td>
<td><code>string</code></td>
<td><p>El algoritmo de cifrado a utilizar. Esta opción es requerida. Especifique una de las siguientes constantes de <a href="#mongodb-driver-clientencryption.constants">ClientEncryption</a>:</p>
<code>MongoDB\Driver\ClientEncryption::AEAD_AES_256_CBC_HMAC_SHA_512_DETERMINISTIC</code>, <code>MongoDB\Driver\ClientEncryption::AEAD_AES_256_CBC_HMAC_SHA_512_RANDOM</code>, <code>MongoDB\Driver\ClientEncryption::ALGORITHM_INDEXED</code>, <code>MongoDB\Driver\ClientEncryption::ALGORITHM_UNINDEXED</code>, <code>MongoDB\Driver\ClientEncryption::ALGORITHM_RANGE</code></td>
</tr>
<tr>
<td>contentionFactor</td>
<td><code>int</code></td>
<td><p>El factor de contención para evaluar las consultas con cargas útiles cifradas indexadas.</p>
<p>Esta opción se aplica únicamente y solo puede ser especificada cuando <code>algorithm</code> es <code>MongoDB\Driver\ClientEncryption::ALGORITHM_INDEXED</code> o <code>MongoDB\Driver\ClientEncryption::ALGORITHM_RANGE</code>.</p></td>
</tr>
<tr>
<td>keyAltName</td>
<td><code>string</code></td>
<td><p>Identifica un documento de colección de cofre de claves por <code>keyAltName</code>. Esta opción es mutuamente exclusiva con <code>keyId</code> y una de las dos es requerida.</p></td>
</tr>
<tr>
<td>keyId</td>
<td><code>MongoDB\BSON\Binary</code></td>
<td><p>Identifica una clave de datos por <code>_id</code>. El valor es un UUID (subtipo binario 4). Esta opción es mutuamente exclusiva con <code>keyAltName</code> y una de las dos es requerida.</p></td>
</tr>
<tr>
<td>queryType</td>
<td><code>string</code></td>
<td><p>El tipo de consulta para evaluar las consultas con cargas útiles cifradas indexadas. Especifique una de las siguientes constantes de <a href="#mongodb-driver-clientencryption.constants">ClientEncryption</a>:</p>
<code>MongoDB\Driver\ClientEncryption::QUERY_TYPE_EQUALITY</code>, <code>MongoDB\Driver\ClientEncryption::QUERY_TYPE_RANGE</code>
<p>Esta opción se aplica únicamente y solo puede ser especificada cuando <code>algorithm</code> es <code>MongoDB\Driver\ClientEncryption::ALGORITHM_INDEXED</code> o <code>MongoDB\Driver\ClientEncryption::ALGORITHM_RANGE</code>.</p></td>
</tr>
<tr>
<td>rangeOpts</td>
<td><code>array</code></td>
<td><p>Opciones de índice para un campo de cifrado interrogeable que soporta consultas "range". Las opciones a continuación deben coincidir con los valores definidos en <code>encryptedFields</code> de la colección objetivo. Para los tipos de campo BSON double y decimal128, <code>min</code>, <code>max</code> y <code>precision</code> deben ser todos definidos o todos no definidos.</p>
<table>
<caption>Opciones de índice de rango</caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>min</td>
<td><code>mixed</code></td>
<td>Requisito si <code>precision</code> está definido. El valor BSON mínimo del rango.</td>
</tr>
<tr>
<td>max</td>
<td><code>mixed</code></td>
<td>Requisito si <code>precision</code> está definido. El valor BSON máximo del rango.</td>
</tr>
<tr>
<td>sparsity</td>
<td><code>int</code></td>
<td>Opcional. Entero positivo de 64 bits.</td>
</tr>
<tr>
<td>precision</td>
<td><code>int</code></td>
<td>Opcional. Entero positivo de 32 bits que especifica la precisión a utilizar para el cifrado explícito. Solo puede ser definido para los tipos de campo BSON double o decimal128.</td>
</tr>
<tr>
<td>trimFactor</td>
<td><code>int</code></td>
<td>Opcional. Entero positivo de 32 bits.</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

## Valores devueltos

Devuelve el valor cifrado como objeto `MongoDB\BSON\Binary` con subtipo 6.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza

MongoDB\Driver\Exception\EncryptionException

si ocurre un error durante el cifrado del valor

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.20.0 | Se añadió la opción de rango `"trimFactor"`. La opción de rango `"sparsity"` ahora es opcional. |
| PECL mongodb 1.16.0 | Se añadió la opción `"rangeOpts"`. |
| PECL mongodb 1.14.0 | Se añadieron las opciones `"contentionFactor"` y `"queryType"`. |

## Véase también

MongoDB\Driver\ClientEncryption::decrypt

MongoDB\Driver\ClientEncryption::encryptExpression
