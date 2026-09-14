---
title: MongoDB\Driver\ClientEncryption::__construct
description: Crea un nuevo objeto ClientEncryption
source_url: https://www.php.net/manual/es/mongodb-driver-clientencryption.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/clientencryption/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 49100
---

MongoDB\Driver\ClientEncryption::\_\_construct

Crea un nuevo objeto ClientEncryption

## Descripción

```php
final public MongoDB\Driver\ClientEncryption::__construct(array $options)
```php

Construye un nuevo objeto `MongoDB\Driver\ClientEncryption` con las opciones especificadas.

## Parámetros

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
<td>keyVaultClient</td>
<td><code>MongoDB\Driver\Manager</code></td>
<td>El gestor utilizado para enrutar las consultas de claves de datos. Esta opción es obligatoria (a diferencia de <code>MongoDB\Driver\Manager::createClientEncryption</code>).</td>
</tr>
<tr>
<td>keyVaultNamespace</td>
<td><code>string</code></td>
<td>Un nombre de espacio completamente calificado (por ejemplo <code>"databaseName.collectionName"</code>) denotando la colección que contiene todas las claves de datos utilizadas para el cifrado y descifrado. Esta opción es requerida.</td>
</tr>
<tr>
<td>kmsProviders</td>
<td><code>array</code></td>
<td><p>Un documento que contiene la configuración de uno o más proveedores KMS, que se utilizan para cifrar claves de datos. Los proveedores admitidos incluyen <code>"aws"</code>, <code>"azure"</code>, <code>"gcp"</code>, <code>"kmip"</code> y <code>"local"</code>, y se debe especificar al menos uno.</p>
<p>Si se especifica un documento vacío para <code>"aws"</code>, <code>"azure"</code> o <code>"gcp"</code>, el controlador intentará configurar el proveedor utilizando <a href="https://github.com/mongodb/specifications/blob/master/source/client-side-encryption/client-side-encryption.rst#automatic-credentials">Automatic Credentials</a>.</p>
<p>El formato para <code>"aws"</code> es el siguiente:</p>
<pre role="javascript"><code>aws: {
    accessKeyId: &lt;string&gt;,
    secretAccessKey: &lt;string&gt;,
    sessionToken: &lt;optional string&gt;
}
&#10;           </code></pre>
<p>El formato para <code>"azure"</code> es el siguiente:</p>
<pre role="javascript"><code>azure: {
    tenantId: &lt;string&gt;,
    clientId: &lt;string&gt;,
    clientSecret: &lt;string&gt;,
    identityPlatformEndpoint: &lt;optional string&gt; // Defaults to &quot;login.microsoftonline.com&quot;
}
&#10;           </code></pre>
<p>El formato para <code>"gcp"</code> es el siguiente:</p>
<pre role="javascript"><code>gcp: {
    email: &lt;string&gt;,
    privateKey: &lt;base64 string&gt;|&lt;MongoDB\BSON\Binary&gt;,
    endpoint: &lt;optional string&gt; // Defaults to &quot;oauth2.googleapis.com&quot;
}
&#10;           </code></pre>
<p>El formato para <code>"kmip"</code> es el siguiente:</p>
<pre role="javascript"><code>kmip: {
    endpoint: &lt;string&gt;
}
&#10;           </code></pre>
<p>El formato para <code>"local"</code> es el siguiente:</p>
<pre role="javascript"><code>local: {
    // 96-byte master key used to encrypt/decrypt data keys
    key: &lt;base64 string&gt;|&lt;MongoDB\BSON\Binary&gt;
}
&#10;           </code></pre></td>
</tr>
<tr>
<td>tlsOptions</td>
<td><code>array</code></td>
<td><p>Un documento que contiene la configuración TLS de uno o varios proveedores KMS. Los proveedores soportados son <code>"aws"</code>, <code>"azure"</code>, <code>"gcp"</code> y <code>"kmip"</code>. Todos los proveedores soportan las siguientes opciones:</p>
<pre role="javascript"><code>&lt;provider&gt;: {
    tlsCaFile: &lt;optional string&gt;,
    tlsCertificateKeyFile: &lt;optional string&gt;,
    tlsCertificateKeyFilePassword: &lt;optional string&gt;,
    tlsDisableOCSPEndpointCheck: &lt;optional bool&gt;
}
&#10;           </code></pre></td>
</tr>
</tbody>
</table>

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza

MongoDB\Driver\Exception\RuntimeException

si la extensión fue compilada sin soporte para libmongocrypt

## Historial de cambios

<table>
<thead>
<tr>
<th>Versión</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>PECL mongodb 1.16.0</td>
<td><p>El proveedor de KMS de AWS para la cifrado lado-cliente ahora acepta una opción <code>"sessionToken"</code>, que puede usarse para autenticarse con credenciales temporales de AWS.</p>
<p>Se añadió <code>"tlsDisableOCSPEndpointCheck"</code> a la opción <code>"tlsOptions"</code>.</p>
<p>Si se especifica un documento vacío para el proveedor de KMS de <code>"azure"</code> o <code>"gcp"</code>, el controlador intentará configurar el proveedor usando <a href="https://github.com/mongodb/specifications/blob/master/source/client-side-encryption/client-side-encryption.rst#automatic-credentials">Credenciales Automáticas</a>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.15.0</td>
<td><p>Si se especifica un documento vacío para el proveedor de KMS de <code>"aws"</code>, el controlador intentará configurar el proveedor usando <a href="https://github.com/mongodb/specifications/blob/master/source/client-side-encryption/client-side-encryption.rst#automatic-credentials">Credenciales Automáticas</a>.</p></td>
</tr>
</tbody>
</table>

## Véase también

MongoDB\Driver\Manager::createClientEncryption

Cifrado Explícito (Manual) de Nivel de Campo del Lado del Cliente

en el manual de MongoDB
