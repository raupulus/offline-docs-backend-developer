---
title: MongoDB\Driver\ClientEncryption::rewrapManyDataKey
description: Reenvuelve claves de datos
source_url: https://www.php.net/manual/es/mongodb-driver-clientencryption.rewrapmanydatakey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/clientencryption/rewrapmanydatakey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49200
---

MongoDB\Driver\ClientEncryption::rewrapManyDataKey

Reenvuelve claves de datos

## Descripción

```php
final public MongoDB\Driver\ClientEncryption::rewrapManyDataKey(array $filter, [array $options]): object
```php

Reenvuelve (es decir, descifra y vuelve a cifrar) cero o más claves de datos en la colección de claves maestras que coincidan con el `filter` proporcionado.

Si no se especifica la opción `"provider"`, las claves de datos coincidentes se reenvuelven con su proveedor KMS actual. De lo contrario, las claves de datos coincidentes se volverán a cifrar según las opciones `"provider"` y `"masterKey"` especificadas.

## Parámetros

`filter` (`arrayobject`)  
El [atributo de la consulta](https://www.mongodb.com/docs/manual/tutorial/query-documents/). Un atributo vacío hará coincidir todos los documentos de la colección.

> [!NOTE]
> Al evaluar los criterios de consulta, MongoDB compara los tipos y los valores según sus propias [reglas de comparación para los tipos BSON](https://www.mongodb.com/docs/manual/reference/bson-type-comparison-order/), que difieren de las reglas de [comparación](#types.comparisons) y de [manipulación de tipos](#language.types.type-juggling) de PHP. Al hacer coincidir un tipo BSON especial, los criterios de consulta deben utilizar la [clase BSON](#mongodb.bson) (ej.: utilizar `MongoDB\BSON\ObjectId` para hacer coincidir un [ObjectId](https://www.mongodb.com/docs/manual/reference/bson-types/#objectid)).

`options`  
<table>
<caption>Opciones de RewrapManyDataKey</caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>provider</td>
<td><code>string</code></td>
<td><p>El proveedor KMS (por ejemplo, <code>"local"</code>, <code>"aws"</code>) que se utilizará para volver a cifrar las claves de datos coincidentes.</p>
<p>Si no se especifica un proveedor KMS, las claves de datos coincidentes se volverán a cifrar con su proveedor KMS actual.</p></td>
</tr>
<tr>
<td>masterKey</td>
<td><code>array</code></td>
<td><p>La clave maestra identifica una clave específica del KMS utilizada para cifrar la nueva clave de datos. Esta opción no debe especificarse sin la opción <code>"provider"</code>. Esta opción es obligatoria si se especifica <code>"provider"</code> y no es <code>"local"</code>.</p>
<table>
<caption>Opciones del proveedor <code>"aws"</code></caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>region</td>
<td>string</td>
<td>Requis.</td>
</tr>
<tr>
<td>key</td>
<td>string</td>
<td>Requis. El nombre de recurso Amazon (ARN) de la clave maestra del cliente AWS (CMK).</td>
</tr>
<tr>
<td>endpoint</td>
<td>string</td>
<td>Opcional. Un identificador de host alternativo para enviar las solicitudes KMS. Puede incluir el número de puerto.</td>
</tr>
</tbody>
</table>
<table>
<caption>Opciones del proveedor <code>"azure"</code></caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>keyVaultEndpoint</td>
<td>string</td>
<td>Requis. Host con puerto opcional (por ejemplo, "example.vault.azure.net").</td>
</tr>
<tr>
<td>keyName</td>
<td>string</td>
<td>Requis.</td>
</tr>
<tr>
<td>keyVersion</td>
<td>string</td>
<td>Opcional. Una versión específica de la clave nombrada. De forma predeterminada, se utiliza la versión primaria de la clave.</td>
</tr>
</tbody>
</table>
<table>
<caption>Opciones del proveedor <code>"gcp"</code></caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>projectId</td>
<td>string</td>
<td>Requis.</td>
</tr>
<tr>
<td>location</td>
<td>string</td>
<td>Requis.</td>
</tr>
<tr>
<td>keyRing</td>
<td>string</td>
<td>Requis.</td>
</tr>
<tr>
<td>keyName</td>
<td>string</td>
<td>Requis.</td>
</tr>
<tr>
<td>keyVersion</td>
<td>string</td>
<td>Opcional. Una versión específica de la clave nombrada. De forma predeterminada, se utiliza la versión primaria de la clave.</td>
</tr>
<tr>
<td>endpoint</td>
<td>string</td>
<td>Opcional. Host con puerto opcional. El valor predeterminado es "cloudkms.googleapis.com".</td>
</tr>
</tbody>
</table>
<table>
<caption>Opciones del proveedor <code>"kmip"</code></caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>keyId</td>
<td>string</td>
<td>Opcional. Identificador único de un objeto gestionado de 96 bytes de datos secretos KMIP. Si no se especifica, el controlador crea un objeto gestionado aleatorio de 96 bytes de datos secretos KMIP.</td>
</tr>
<tr>
<td>endpoint</td>
<td>string</td>
<td>Opcional. Host con puerto opcional.</td>
</tr>
<tr>
<td>delegated</td>
<td>bool</td>
<td>Opcional. Si es true, esta clave debe ser descifrada por el servidor KMIP.</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

## Valores devueltos

Devuelve un objeto que tendrá una propiedad opcional `bulkWriteResult` que contiene el resultado de la operación interna `bulkWrite` como un objeto. Si ninguna clave de datos coincidió con el filtro o la escritura no fue reconocida, la propiedad `bulkWriteResult` será `null`.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\ConnectionException

si la conexión al servidor falla por una razón distinta a un problema de identificación

Lanza una excepción

MongoDB\Driver\Exception\AuthenticationException

si se requiere una identificación pero falla

Lanza

MongoDB\Driver\Exception\EncryptionException

si ocurre un error al descifrar o volver a cifrar una clave de datos.

Lanza

MongoDB\Driver\Exception\RuntimeException

en otros errores.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.20.0 | Se añadió `"delegated"` a las opciones de clave maestra del proveedor KMIP. |
