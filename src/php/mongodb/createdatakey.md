---
title: MongoDB\Driver\ClientEncryption::createDataKey
description: Crea un documento de clave
source_url: https://www.php.net/manual/es/mongodb-driver-clientencryption.createdatakey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/clientencryption/createdatakey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49110
---

MongoDB\Driver\ClientEncryption::createDataKey

Crea un documento de clave

## Descripción

```php
final public MongoDB\Driver\ClientEncryption::createDataKey(string $kmsProvider, [array $options]): MongoDB\BSON\Binary
```php

Crea un nuevo documento de clave e inserta en la colección de almacén de claves.

## Parámetros

`kmsProvider`  
El proveedor KMS (por ejemplo `"local"`, `"aws"`) que se utilizará para cifrar la nueva clave de datos.

`options`  
<table>
<caption>Opciones de clave de datos</caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>masterKey</td>
<td><code>array</code></td>
<td><p>El documento masterKey identifica una clave específica del KMS utilizada para cifrar la nueva clave de datos. Esta opción es obligatoria a menos que <code>kmsProvider</code> sea <code>"local"</code>.</p>
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
<tr>
<td>keyAltNames</td>
<td><code>array</code></td>
<td><p>Una lista opcional de nombres alternativos de tipo string utilizados para referenciar una clave. Si se crea una clave con nombres alternativos, entonces el cifrado puede referirse a la clave mediante el nombre alternativo único en lugar de por <code>_id</code>.</p></td>
</tr>
<tr>
<td>keyMaterial</td>
<td><code>MongoDB\BSON\Binary</code></td>
<td><p>Un valor opcional de 96 bytes para usar como material de clave personalizado para la clave de datos que se está creando. Si se proporciona keyMaterial, el material de clave personalizado se utiliza para cifrar y descifrar datos. De lo contrario, el material de la nueva clave de datos se genera a partir de un dispositivo criptográficamente seguro aleatorio.</p></td>
</tr>
</tbody>
</table>

## Valores devueltos

Devuelve el identificador de la nueva clave como un objeto `MongoDB\BSON\Binary` con subtipo 4 (UUID).

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

MongoDB\Driver\Exception\RuntimeException

en caso de otros errores.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.20.0 | Añadido `"delegated"` a las opciones de masterKey del proveedor KMIP. |
| PECL mongodb 1.15.0 | Añadida la opción `"keyMaterial"`. |
| PECL mongodb 1.10.0 | Azure y GCP ahora son compatibles como proveedores KMS para cifrado lado-cliente. |
