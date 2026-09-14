---
title: MongoDB\Driver\Manager::__construct
description: Crea un nuevo Manager MongoDB
source_url: https://www.php.net/manual/es/mongodb-driver-manager.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/manager/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: true
translation_revision: 36c32a2a9
order: 49700
---

MongoDB\Driver\Manager::\_\_construct

Crea un nuevo Manager MongoDB

## Descripción

```php
final public MongoDB\Driver\Manager::__construct([string $uri], [array $uriOptions], [array $driverOptions])
```php

Construye un nuevo objeto `MongoDB\Driver\Manager` con las opciones especificadas.

> [!NOTE]
> Con la [Especificación de descubrimiento y supervisión del servidor](https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md#single-threaded-client-construction), este constructor no realiza E/S. Las conexiones se inicializarán bajo demanda, durante la ejecución de la primera operación.

> [!NOTE]
> Cuando se especifican opciones de URI SSL o TLS a través de la cadena de conexión o el parámetro `uriOptions`, la extensión activará implícitamente TLS para sus conexiones. Para evitar esto, desactive explícitamente la opción `tls` o no especifique ninguna opción TLS.

> [!NOTE]
> En las plataformas Unix, la extensión MongoDB es sensible a los scripts que utilizan la llamada al sistema fork() sin llamar a exec(). No se deben reutilizar instancias `MongoDB\Driver\Manager` en un proceso hijo derivado de un fork.

## Parámetros

`uri`  
Una URI de conexión [mongodb://](https://www.mongodb.com/docs/manual/reference/connection-string/):

```
mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[defaultAuthDb][?options]]

      
```php

Para los detalles sobre las opciones de URI admitidas, ver [Opciones de cadena de conexión](https://www.mongodb.com/docs/manual/reference/connection-string/#connections-connection-options) en el manual MongoDB. [Opciones de pool de conexiones](https://www.mongodb.com/docs/manual/reference/connection-string/#connection-pool-options) no son admitidas, ya que la extensión no implementa pools de conexiones.

Por omisión, `"mongodb://127.0.0.1:27017"` si no se especifica.

El `uri` es una URL, por lo que todos los caracteres especiales en sus componentes deben estar codificados en URL según la [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986). Esto es particularmente relevante para el nombre de usuario y la contraseña, que pueden incluir caracteres especiales tales como `@`, `:` o `%`. Al conectarse a través de un socket de dominio Unix, la ruta del socket puede contener caracteres especiales como barras diagonales y debe estar codificada. La función `rawurlencode` puede ser utilizada para codificar las partes constitutivas de la URI.

El componente `defaultAuthDb` puede ser utilizado para especificar la base de datos asociada a las credenciales del usuario; sin embargo, la opción de URI `authSource` tendrá prioridad si se especifica. Si ni `defaultAuthDb` ni `authSource` se especifican, la base de datos `admin` será utilizada por omisión. El componente `defaultAuthDb` no tiene ningún efecto en ausencia de credenciales de usuario.

`uriOptions`  
Opciones adicionales [de cadena de conexión](https://www.mongodb.com/docs/manual/reference/connection-string/#connections-connection-options), que sobrescribirán cualquier opción con el mismo nombre en el parámetro `uri`.

<table>
<caption>uriOptions</caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>appname</td>
<td><code>string</code></td>
<td><p>MongoDB 3.4+ tiene la capacidad de anotar las conexiones con metadatos proporcionados por el cliente conectado. Estos metadatos se incluyen en los registros del servidor al establecer una conexión y también se registran en los registros de consultas lentas cuando el perfilado de la base de datos está activado.</p>
<p>Esta opción puede ser utilizada para especificar un nombre de aplicación, que será incluido en los metadatos. El valor no puede exceder 128 caracteres de longitud.</p></td>
</tr>
<tr>
<td>authMechanism</td>
<td><code>string</code></td>
<td><p>El mecanismo de autenticación que MongoDB utilizará para autenticar la conexión. Para más detalles y una lista de los valores admitidos, ver <a href="https://www.mongodb.com/docs/manual/reference/connection-string/#urioption.authMechanism">Opciones de autenticación</a> en el manual MongoDB.</p></td>
</tr>
<tr>
<td>authMechanismProperties</td>
<td><code>array</code></td>
<td><p>Las propiedades específicas del mecanismo de autenticación seleccionado. Para más detalles y una lista de las propiedades admitidas, ver la <a href="https://github.com/mongodb/specifications/blob/master/source/auth/auth.rst#auth-related-options">Especificación de autenticación del controlador</a>.</p>

&#10;</div>
<p>Cuando no se especifica en la cadena de URI, esta opción se expresa como un array de pares clave/valor. Las claves y valores de este array deben ser strings.</p>
</div></td>
</tr>
<tr>
<td>authSource</td>
<td><code>string</code></td>
<td><p>El nombre de la base de datos asociada a las credenciales del usuario. Por omisión al componente de la base de datos de la URI de conexión, o a la base de datos <code>admin</code> si ambos no se especifican.</p>
<p>Para los mecanismos de autenticación que no admiten la noción de base de datos (por ejemplo, GSSAPI), esto debería ser <code>"$external"</code>.</p></td>
</tr>
<tr>
<td>compressors</td>
<td><code>string</code></td>
<td><p>Una lista priorizada y delimitada por comas de compresores que el cliente desea utilizar. Los mensajes solo se comprimen si el cliente y el servidor comparten compresores en común, y el compresor utilizado en cada dirección dependerá de la configuración individual del servidor o del controlador. Ver la <a href="https://github.com/mongodb/specifications/blob/master/source/compression/OP_COMPRESSED.rst#compressors">Especificación de compresión del controlador</a> para más información.</p></td>
</tr>
<tr>
<td>connectTimeoutMS</td>
<td><code>int</code></td>
<td><p>El tiempo en milisegundos para intentar una conexión antes de expirar. Por omisión, 10 000 milisegundos.</p></td>
</tr>
<tr>
<td>directConnection</td>
<td><code>bool</code></td>
<td><p>Esta opción puede ser utilizada para controlar el comportamiento de descubrimiento del conjunto de réplicas cuando solo se proporciona un host en la cadena de conexión. Por omisión, proporcionar un solo miembro en la cadena de conexión establecerá una conexión directa o descubrirá miembros adicionales según si la opción de URI <code>"replicaSet"</code> está omitida o presente, respectivamente. Especifique <code>false</code> para forzar el descubrimiento a que ocurra (si <code>"replicaSet"</code> está omitido) o especifique <code>true</code> para forzar una conexión directa (si <code>"replicaSet"</code> está presente).</p></td>
</tr>
<tr>
<td>enableOverloadRetargeting</td>
<td><code>bool</code></td>
<td><p>Cuando se establece a <code>true</code>, fuerza la selección del servidor tras un <code>SystemOverloadedError</code>. Por omisión, <code>false</code>.</p></td>
</tr>
<tr>
<td>heartbeatFrequencyMS</td>
<td><code>int</code></td>
<td><p>Especifica el intervalo en milisegundos entre las verificaciones de la topología MongoDB, contado desde el final de la verificación previa hasta el inicio de la siguiente. Por omisión, 60 000 milisegundos.</p>
<p>Para la <a href="https://github.com/mongodb/specifications/blob/master/source/server-discovery-and-monitoring/server-discovery-and-monitoring.md#heartbeatfrequencyms">Especificación de descubrimiento y supervisión del servidor</a>, este valor no puede ser inferior a 500 milisegundos.</p></td>
</tr>
<tr>
<td>journal</td>
<td><code>bool</code></td>
<td><p>Corresponde a la opción <code>journal</code> del write concern por omisión. Si <code>true</code>, las escrituras requerirán un acuse de recibo de MongoDB indicando que la operación ha sido escrita en el diario. Para más detalles, ver <code>MongoDB\Driver\WriteConcern</code>.</p></td>
</tr>
<tr>
<td>loadBalanced</td>
<td><code>bool</code></td>
<td><p>Especifica si el controlador se conecta a un clúster MongoDB a través de un equilibrador de carga. Si <code>true</code>, el controlador solo puede conectarse a un solo host (especificado por la cadena de conexión o la búsqueda SRV), la opción de URI <code>"directConnection"</code> no puede ser <code>true</code>, y la opción de URI <code>"replicaSet"</code> debe ser omitida. Por omisión, <code>false</code>.</p></td>
</tr>
<tr>
<td>localThresholdMS</td>
<td><code>int</code></td>
<td><p>El tamaño en milisegundos de la ventana de latencia para la selección entre múltiples instancias MongoDB apropiadas al resolver una preferencia de lectura. Por omisión, 15 milisegundos.</p></td>
</tr>
<tr>
<td>maxAdaptiveRetries</td>
<td><code>int</code></td>
<td><p>Esta opción puede ser utilizada para cambiar el número máximo de reintentos cuando se produce un <code>SystemOverloadedError</code>. Debe ser un entero positivo; por omisión, <code>2</code>.</p></td>
</tr>
<tr>
<td>maxStalenessSeconds</td>
<td><code>int</code></td>
<td><p>Corresponde a la opción <code>maxStalenessSeconds</code> de la preferencia de lectura. Especifica, en segundos, la duración máxima de validez de una instancia secundaria antes de que el cliente deje de usarla para las operaciones de lectura. Por omisión, no hay una duración máxima de validez y los clientes no tendrán en cuenta el retraso de una instancia secundaria al elegir la dirección de una operación de lectura. Para más detalles, ver <code>MongoDB\Driver\ReadPreference</code>.</p>
<p>Si se especifica, la duración máxima de validez debe ser un entero de 32 bits firmado superior o igual a <code>MongoDB\Driver\ReadPreference::SMALLEST_MAX_STALENESS_SECONDS</code> (por ejemplo, 90 segundos).</p></td>
</tr>
<tr>
<td>password</td>
<td><code>string</code></td>
<td>La contraseña del usuario en proceso de autenticación. Esta opción es útil si la contraseña contiene caracteres especiales, que de otro modo deberían estar codificados en URL para la URI de conexión.</td>
</tr>
<tr>
<td>readConcernLevel</td>
<td><code>string</code></td>
<td>Corresponde a la opción <code>level</code> de la preferencia de lectura. Especifica el nivel de aislamiento de lectura. Para más detalles, ver <code>MongoDB\Driver\ReadConcern</code>.</td>
</tr>
<tr>
<td>readPreference</td>
<td><code>string</code></td>
<td><p>Corresponde a la opción <code>mode</code> de la preferencia de lectura. Por omisión, <code>"primary"</code>. Para más detalles, ver <code>MongoDB\Driver\ReadPreference</code>.</p></td>
</tr>
<tr>
<td>readPreferenceTags</td>
<td><code>array</code></td>
<td><p>Corresponde a la opción <code>tagSets</code> de la preferencia de lectura. Los conjuntos de etiquetas permiten dirigir las operaciones de lectura a miembros específicos de un conjunto de réplicas. Para más detalles, ver <code>MongoDB\Driver\ReadPreference</code>.</p>

&#10;</div>
<p>Cuando no se especifica en la cadena de URI, esta opción se expresa como un array conforme al formato esperado por <code>MongoDB\Driver\ReadPreference::__construct</code>.</p>
</div></td>
</tr>
<tr>
<td>replicaSet</td>
<td><code>string</code></td>
<td><p>Especifica el nombre del conjunto de réplicas.</p></td>
</tr>
<tr>
<td>retryReads</td>
<td><code>bool</code></td>
<td><p>Especifica si el controlador debe reintentar automáticamente ciertas operaciones de lectura que fallan debido a errores de red transitorios o elecciones de conjunto de réplicas. Esta funcionalidad requiere MongoDB 3.6+. Por omisión, <code>true</code>.</p>
<p>Ver la <a href="https://github.com/mongodb/specifications/blob/master/source/retryable-reads/retryable-reads.rst">Especificación de lectura reintentable</a> para más información.</p></td>
</tr>
<tr>
<td>retryWrites</td>
<td><code>bool</code></td>
<td><p>Especifica si el controlador debe reintentar automáticamente ciertas operaciones de escritura que fallan debido a errores de red transitorios o elecciones de conjunto de réplicas. Esta funcionalidad requiere MongoDB 3.6+. Por omisión, <code>true</code>.</p>
<p>Ver <a href="https://www.mongodb.com/docs/manual/core/retryable-writes/">Escrituras reintentables</a> en el manual MongoDB para más información.</p></td>
</tr>
<tr>
<td>serverSelectionTimeoutMS</td>
<td><code>int</code></td>
<td><p>Especifica cuánto tiempo en milisegundos bloquear para la selección del servidor antes de lanzar una excepción. Por omisión, 30 000 milisegundos.</p></td>
</tr>
<tr>
<td>serverSelectionTryOnce</td>
<td><code>bool</code></td>
<td><p>Cuando <code>true</code>, indica al controlador que escanee el despliegue MongoDB exactamente una vez después de un fallo de selección del servidor, luego seleccione un servidor o lance una excepción. Cuando <code>false</code>, el controlador bloquea y busca un servidor hasta el valor de <code>"serverSelectionTimeoutMS"</code>. Por omisión, <code>true</code>.</p></td>
</tr>
<tr>
<td>socketCheckIntervalMS</td>
<td><code>int</code></td>
<td><p>Si un socket no ha sido utilizado recientemente, el controlador debe verificarlo a través de un comando <code>hello</code> antes de usarlo para cualquier operación. Por omisión, 5 000 milisegundos.</p></td>
</tr>
<tr>
<td>socketTimeoutMS</td>
<td><code>int</code></td>
<td><p>El tiempo en milisegundos para intentar un envío o recepción en un socket antes de expirar. Por omisión, 300 000 milisegundos (es decir, cinco minutos).</p></td>
</tr>
<tr>
<td>srvMaxHosts</td>
<td><code>int</code></td>
<td><p>El número máximo de resultados SRV a seleccionar aleatoriamente durante la primera población de la lista de semillas o, durante la consulta SRV, la adición de nuevos hosts a la topología. Por omisión, <code>0</code> (es decir, sin máximo).</p></td>
</tr>
<tr>
<td>srvServiceName</td>
<td><code>string</code></td>
<td><p>El nombre de servicio a utilizar para la búsqueda SRV en la lista de semillas inicial y la consulta SRV. Por omisión, <code>"mongodb"</code>.</p></td>
</tr>
<tr>
<td>tls</td>
<td><code>bool</code></td>
<td><p>Inicializa la conexión con TLS/SSL si <code>true</code>. Por omisión, <code>false</code>.</p></td>
</tr>
<tr>
<td>tlsAllowInvalidCertificates</td>
<td><code>bool</code></td>
<td><p>Especifica si el controlador debe generar un error cuando el certificado TLS del servidor es inválido. Por omisión, <code>false</code>.</p>

&#10;</div>
<p>Desactivar la validación del certificado crea una vulnerabilidad.</p>
</div></td>
</tr>
<tr>
<td>tlsAllowInvalidHostnames</td>
<td><code>bool</code></td>
<td><p>Especifica si el controlador debe generar un error cuando hay un desacuerdo entre el nombre de host del servidor y el nombre de host especificado por el certificado TLS. Por omisión, <code>false</code>.</p>

&#10;</div>
<p>Desactivar la validación del certificado crea una vulnerabilidad. Permitir nombres de host inválidos puede exponer al controlador a una <a href="https://en.wikipedia.org/wiki/Man-in-the-middle_attack">ataque del hombre del medio</a>.</p>
</div></td>
</tr>
<tr>
<td>tlsCAFile</td>
<td><code>string</code></td>
<td><p>La ruta del archivo que contiene un solo certificado o un conjunto de certificados de autoridades a considerar confiables al establecer una conexión TLS. Se utilizará el almacén de certificados del sistema por omisión.</p></td>
</tr>
<tr>
<td>tlsCertificateKeyFile</td>
<td><code>string</code></td>
<td><p>La ruta del archivo de certificado del cliente o del archivo de clave privada del cliente; en el caso de que ambos sean necesarios, los archivos deben estar concatenados.</p></td>
</tr>
<tr>
<td>tlsCertificateKeyFilePassword</td>
<td><code>string</code></td>
<td><p>La contraseña para descifrar la clave privada del cliente (es decir, la opción de URI <code>"tlsCertificateKeyFile"</code>) a utilizar para las conexiones TLS.</p></td>
</tr>
<tr>
<td>tlsDisableCertificateRevocationCheck</td>
<td><code>bool</code></td>
<td><p>Si <code>true</code>, el controlador no intentará verificar el estado de revocación del certificado (por ejemplo, OCSP, CRL). Por omisión, <code>false</code>.</p></td>
</tr>
<tr>
<td>tlsDisableOCSPEndpointCheck</td>
<td><code>bool</code></td>
<td><p>Si <code>true</code>, el controlador no intentará contactar un punto de extremo de responso OCSP si es necesario (es decir, una respuesta OCSP no está grapada). Por omisión, <code>false</code>.</p></td>
</tr>
<tr>
<td>tlsInsecure</td>
<td><code>bool</code></td>
<td><p>Relaja las restricciones TLS tanto como sea posible. Especificar <code>true</code> para que esta opción tenga el mismo efecto que especificar <code>true</code> para las opciones de URI <code>"tlsAllowInvalidCertificates"</code> y <code>"tlsAllowInvalidHostnames"</code>. Por omisión, <code>false</code>.</p>

&#10;</div>
<p>Desactivar la validación del certificado crea una vulnerabilidad. Permitir nombres de host inválidos puede exponer al controlador a una <a href="https://en.wikipedia.org/wiki/Man-in-the-middle_attack">ataque del hombre del medio</a>.</p>
</div></td>
</tr>
<tr>
<td>username</td>
<td><code>string</code></td>
<td>El nombre de usuario del usuario en proceso de autenticación. Esta opción es útil si el nombre de usuario contiene caracteres especiales, que de otro modo deberían estar codificados en URL para la URI de conexión.</td>
</tr>
<tr>
<td>w</td>
<td><code>intstring</code></td>
<td><p>Corresponde a la opción <code>w</code> del write concern por omisión. Para más detalles, ver <code>MongoDB\Driver\WriteConcern</code>.</p></td>
</tr>
<tr>
<td>wTimeoutMS</td>
<td><code>intstring</code></td>
<td><p>Corresponde a la opción <code>wtimeout</code> del write concern por omisión. Especifica un límite de tiempo, en milisegundos, para el write concern. Para más detalles, ver <code>MongoDB\Driver\WriteConcern</code>.</p>
<p>Si se especifica, <code>wTimeoutMS</code> debe ser un entero de 32 bits firmado superior o igual a cero.</p></td>
</tr>
<tr>
<td>zlibCompressionLevel</td>
<td><code>int</code></td>
<td><p>Especifica el nivel de compresión a utilizar para el compresor zlib. Esta opción no tiene ningún efecto si <code>zlib</code> no está incluido en la opción de URI <code>"compressors"</code>. Ver la <a href="https://github.com/mongodb/specifications/blob/master/source/compression/OP_COMPRESSED.rst#zlibcompressionlevel">Especificación de compresión del controlador</a> para más información.</p></td>
</tr>
</tbody>
</table>

`driverOptions`  
<table>
<caption>driverOptions</caption>
<thead>
<tr>
<th>Opción</th>
<th>Tipo</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>autoEncryption</td>
<td><code>array</code></td>
<td><p>Proporciona opciones para activar el cifrado automático a nivel de campo. La lista de opciones se describe en la <a href="#mongodb-driver-manager.construct-autoencryption">tabla de abajo</a>.</p>

&#10;</div>
<p>El cifrado automático es una funcionalidad empresarial que solo se aplica a las operaciones sobre una colección. El cifrado automático no es admitido para las operaciones sobre una base de datos o una vista, y las operaciones que no son sorteadas resultarán en un error (ver <a href="https://github.com/mongodb/specifications/blob/master/source/client-side-encryption/client-side-encryption.rst#libmongocrypt-auto-encryption-allow-list">libmongocrypt: La lista de autorización de cifrado automático</a>). Para sortear el cifrado automático para todas las operaciones, establezca <code>bypassAutoEncryption</code> a <code>true</code>.</p>
<p>El cifrado automático requiere que el usuario autenticado tenga el privilegio de acción <a href="https://www.mongodb.com/docs/manual/reference/command/listCollections/#required-access">listCollections</a>.</p>
<p>El cifrado explícito y automático es una funcionalidad de la comunidad. El controlador siempre puede descifrar automáticamente cuando <code>bypassAutoEncryption</code> es <code>true</code>.</p>
</div></td>
</tr>
<tr>
<td>ca_dir</td>
<td><code>string</code></td>
<td><p>La ruta del directorio de certificados correctamente hashados. Se utilizará el almacén de certificados del sistema por omisión.</p></td>
</tr>
<tr>
<td>crl_file</td>
<td><code>string</code></td>
<td>La ruta del archivo de lista de revocación de certificados.</td>
</tr>
<tr>
<td>disableClientPersistence</td>
<td><code>bool</code></td>
<td><p>Si <code>true</code>, este Manager utilizará un nuevo cliente libmongoc, que no será persistido ni compartido con otros objetos Manager. Cuando este objeto Manager es liberado, su cliente será destruido y todas las conexiones serán cerradas. Por omisión, <code>false</code>.</p>

&#10;</div>
<p>Desactivar la persistencia del cliente no es generalmente recomendado.</p>
</div></td>
</tr>
<tr>
<td>driver</td>
<td><code>array</code></td>
<td><p>Permite a un nivel superior de biblioteca añadir sus propias metadatos al apretón de manos del servidor. Por omisión, la extensión envía su propio nombre, versión y plataforma (es decir, versión PHP) en el apretón de manos. Las cadenas pueden ser especificadas para las claves <code>"name"</code>, <code>"version"</code> y <code>"platform"</code> de este array, y serán añadidas al campo respectivo(s) del apretón de manos del servidor.</p>

&#10;</div>
<p>Las informaciones del apretón de manos están limitadas a 512 bytes. La extensión truncará los datos del apretón de manos para adaptarse a esta cadena de 512 bytes. Las bibliotecas de nivel superior están animadas a mantener sus propias metadatos concisas.</p>
</div></td>
</tr>
<tr>
<td>serverApi</td>
<td><code>MongoDB\Driver\ServerApi</code></td>
<td><p>Esta opción se utiliza para declarar una versión de API de servidor para el Manager. Si se omite, no se declara ninguna versión de API.</p></td>
</tr>
</tbody>
</table>

Las siguientes opciones son admitidas:

<table>
<caption>Opciones para el cifrado automático</caption>
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
<td>El Manager utilizado para enrutar las peticiones de claves de datos a un cluster MongoDB diferente. Por defecto, el Manager y cluster actual es utilizado.</td>
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
<tr>
<td>schemaMap</td>
<td><code>arrayobject</code></td>
<td><p>Mapea los espacios de nombres de colección a un esquema JSON local. Esto se utiliza para configurar el cifrado automático. Ver <a href="https://www.mongodb.com/docs/manual/reference/security-client-side-automatic-json-schema/">Reglas de cifrado automático</a> en el manual MongoDB para más información. Es un error especificar una colección tanto en <code>schemaMap</code> como en <code>encryptedFieldsMap</code>.</p>

&#10;</div>
<p>Proporcionar un <code>schemaMap</code> proporciona más seguridad que confiar en los esquemas JSON obtenidos del servidor. Esto protege contra un servidor malintencionado anunciando un falso esquema JSON, que podría engañar al cliente para enviar datos no cifrados que deberían estar cifrados.</p>

&#10;</div>
<p>Los esquemas proporcionados en el <code>schemaMap</code> solo se aplican a la configuración del cifrado automático para el cifrado del lado del cliente. Otras reglas de validación en el esquema JSON no serán aplicadas por el controlador y resultarán en un error.</p>
</div></td>
</tr>
<tr>
<td>bypassAutoEncryption</td>
<td><code>bool</code></td>
<td>Si <code>true</code>, <code>mongocryptd</code> no será lanzado automáticamente. Esto se utiliza para desactivar el cifrado automático. Por omisión, <code>false</code>.</td>
</tr>
<tr>
<td>bypassQueryAnalysis</td>
<td><code>bool</code></td>
<td><p>Si <code>true</code>, el análisis automático de las comandos salientes será desactivado y <code>mongocryptd</code> no será lanzado automáticamente. Esto permite el caso de uso del cifrado explícito para consultar campos indexados sin requerir la biblioteca <code>crypt_shared</code> bajo licencia empresarial o el proceso <code>mongocryptd</code>. Por omisión, <code>false</code>.</p></td>
</tr>
<tr>
<td>encryptedFieldsMap</td>
<td><code>arrayobject</code></td>
<td><p>Mapea los espacios de nombres de colección a un documento <code>encryptedFields</code>. Esto se utiliza para configurar el cifrado consultable. Ver <a href="https://www.mongodb.com/docs/manual/core/queryable-encryption/fundamentals/encrypt-and-query/">Cifrado de campo y consultabilidad</a> en el manual MongoDB para más información. Es un error especificar una colección tanto en <code>encryptedFieldsMap</code> como en <code>schemaMap</code>.</p>

&#10;</div>
<p>Proporcionar un <code>encryptedFieldsMap</code> proporciona más seguridad que confiar en los <code>encryptedFields</code> obtenidos del servidor. Esto protege contra un servidor malintencionado anunciando un falso <code>encryptedFields</code>.</p>
</div></td>
</tr>
<tr>
<td>extraOptions</td>
<td><code>array</code></td>
<td><p>El <code>extraOptions</code> se refieren al proceso <code>mongocryptd</code>. Las siguientes opciones son admitidas:</p>
<code>mongocryptdURI</code> (<code>string</code>): URI para conectarse a un proceso <code>mongocryptd</code> existente. Por omisión, <code>"mongodb://localhost:27020"</code>., <code>mongocryptdBypassSpawn</code> (<code>bool</code>): Si <code>true</code>, impide que el controlador lance <code>mongocryptd</code>. Por omisión, <code>false</code>., <code>mongocryptdSpawnPath</code> (<code>string</code>): Ruta absoluta para buscar el binario <code>mongocryptd</code>. Por omisión, una cadena vacía y consulta las rutas del sistema., <code>mongocryptdSpawnArgs</code> (<code>array</code>): Array de argumentos de cadena a pasar a <code>mongocryptd</code> al lanzarlo. Por omisión, <code>["--idleShutdownTimeoutSecs=60"]</code>., <code>cryptSharedLibPath</code> (<code>string</code>): Ruta absoluta hacia la biblioteca compartida <code>crypt_shared</code>. Por omisión, una cadena vacía y consulta las rutas del sistema., <code>cryptSharedLibRequired</code> (<code>bool</code>): Si <code>true</code>, exige que el controlador cargue <code>crypt_shared</code>. Por omisión, <code>false</code>.
<p>Ver la <a href="https://github.com/mongodb/specifications/blob/master/source/client-side-encryption/client-side-encryption.rst#extraoptions">Especificación de cifrado del lado del cliente</a> para más información.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> El cifrado automático es una funcionalidad empresarial que solo se aplica a las operaciones sobre una colección. El cifrado automático no es admitido para las operaciones sobre una base de datos o una vista, y las operaciones que no son sorteadas resultarán en un error. Para sortear el cifrado automático para todas las operaciones, establezca `bypassAutoEncryption=true` en `autoEncryption`. Para más información sobre las operaciones admitidas, ver la [Especificación de cifrado del lado del cliente](https://github.com/mongodb/specifications/blob/master/source/client-side-encryption/client-side-encryption.rst#libmongocrypt-auto-encryption-whitelist).

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

si un parámetro es de tipo incorrecto

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
<td>PECL mongodb 2.0.0</td>
<td><p>La opción de URI <code>"authMechanismProperties"</code> ha sido eliminada. Utilizar la propiedad <code>"CANONICALIZE_HOST_NAME"</code> de la opción de URI <code>"authMechanismProperties"</code> en su lugar.</p>
<p>La opción de URI <code>"authMechanism"</code> ha sido eliminada. Utilizar la propiedad <code>"SERVICE_NAME"</code> de la opción de URI <code>"authMechanismProperties"</code> en su lugar.</p>
<p>La opción de URI <code>"authSource"</code> ha sido eliminada. Utilizar las opciones de URI <code>"w"</code> y <code>"wTimeoutMS"</code> en su lugar.</p>
<p>La opción de URI <code>"ssl"</code> ha sido eliminada. Utilizar la opción de URI <code>"tls"</code> en su lugar.</p>
<p>La opción de controlador <code>"allow_invalid_hostname"</code> ha sido eliminada. Utilizar la opción de URI <code>"tlsAllowInvalidHostnames"</code> en su lugar.</p>
<p>La opción de controlador <code>"ca_file"</code> ha sido eliminada. Utilizar la opción de URI <code>"tlsCAFile"</code> en su lugar.</p>
<p>La opción de controlador <code>"context"</code> ha sido eliminada. Todas las opciones de contexto han sido deprecadas en favor de las diversas opciones de URI relacionadas con TLS.</p>
<p>La opción de controlador <code>"pem_file"</code> ha sido eliminada. Utilizar la opción de URI <code>"tlsCertificateKeyFile"</code> en su lugar.</p>
<p>La opción de controlador <code>"pem_pwd"</code> ha sido eliminada. Utilizar la opción de URI <code>"tlsCertificateKeyFilePassword"</code> en su lugar.</p>
<p>La opción de controlador <code>"weak_cert_validation"</code> ha sido eliminada. Utilizar la opción de URI <code>"tlsAllowInvalidCertificates"</code> en su lugar.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.16.0</td>
<td><p>El proveedor AWS KMS para el cifrado del lado del cliente ahora acepta una opción <code>"sessionToken"</code>, que puede ser utilizada para autenticarse con credenciales AWS temporales.</p>
<p>Añadido <code>"tlsDisableOCSPEndpointCheck"</code> al campo <code>"tlsOptions"</code> de la opción de controlador <code>"autoEncryption"</code>.</p>
<p>Si se especifica un documento vacío para el proveedor KMS <code>"azure"</code> o <code>"gcp"</code>, el controlador intentará configurar el proveedor utilizando <a href="https://github.com/mongodb/specifications/blob/master/source/client-side-encryption/client-side-encryption.rst#automatic-credentials">las credenciales automáticas</a>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.15.0</td>
<td><p>Si se especifica un documento vacío para el proveedor KMS <code>"aws"</code>, el controlador intentará configurar el proveedor utilizando <a href="https://github.com/mongodb/specifications/blob/master/source/client-side-encryption/client-side-encryption.rst#automatic-credentials">las credenciales automáticas</a>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.14.0</td>
<td><p>Añadidas las opciones de cifrado del lado del cliente <code>"bypassQueryAnalysis"</code> y <code>"encryptedFieldsMap"</code>. Opciones adicionales relacionadas con <code>crypt_shared</code> son ahora admitidas en la opción de cifrado del lado del cliente <code>"extraOptions"</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.13.0</td>
<td><p>Añadidas las opciones de URI <code>"srvMaxHosts"</code> y <code>"srvServiceName"</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.12.0</td>
<td><p>KMIP es ahora admitido como proveedor KMS para el cifrado del lado del cliente y puede ser configurado en el campo <code>"kmsProviders"</code> de la opción de controlador <code>"autoEncryption"</code>. Además, las opciones TLS para los proveedores KMS pueden ahora ser configuradas en el campo <code>"tlsOptions"</code> de la opción de controlador <code>"autoEncryption"</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.11.0</td>
<td><p>Añadida la opción de URI <code>"loadBalanced"</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.10.0</td>
<td><p>Añadida la opción de controlador <code>"disableClientPersistence"</code>.</p>
<p>Azure y GCP son ahora admitidos como proveedores KMS para el cifrado del lado del cliente y pueden ser configurados en el campo <code>"kmsProviders"</code> de la opción de controlador <code>"autoEncryption"</code>. Las cadenas codificadas en base64 son ahora aceptadas como alternativa a <code>MongoDB\BSON\Binary</code> para las opciones en <code>"kmsProviders"</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.8.0</td>
<td><p>Añadidas las opciones de URI <code>"directConnection"</code>, <code>"tlsDisableCertificateRevocationCheck"</code> y <code>"tlsDisableOCSPEndpointCheck"</code>.</p>
<p>Añadida la opción de controlador <code>"driver"</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.7.0</td>
<td><p>Añadida la opción de controlador <code>"autoEncryption"</code>.</p>
<p>Especificar cualquier opción SSL o TLS a través del parámetro <code>driverOptions</code> activará ahora implícitamente TLS, como ocurre con las opciones de URI correspondientes.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.6.0</td>
<td><p>Añadidas las opciones de URI <code>"retryReads"</code>, <code>"tls"</code>, <code>"tlsAllowInvalidCertificates"</code>, <code>"tlsAllowInvalidHostnames"</code>, <code>"tlsCAFile"</code>, <code>"tlsCertificateKeyFile"</code>, <code>"tlsCertificateKeyFilePassword"</code>, y <code>"tlsInsecure"</code>.</p>
<p>La opción de URI <code>"retryWrites"</code> está ahora a <code>true</code> por omisión.</p>
<p>Especificar una opción de URI SSL o TLS a través de la cadena de conexión o el parámetro <code>uriOptions</code> activará ahora implícitamente TLS a menos que <code>ssl</code> o <code>tls</code> sea <code>false</code>. TLS no es <em>implícitamente</em> activado para las opciones en el parámetro <code>driverOptions</code>, lo que es inalterado con respecto a las versiones anteriores.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.5.0</td>
<td><p><code>"wtimeoutMS"</code> es ahora siempre validado y aplicado al write concern. Anteriormente, la opción era ignorada si <code>"w"</code> era &lt;= 1, ya que el tiempo de espera solo se aplica a la replicación.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.4.0</td>
<td><p>Añadidas las opciones de URI <code>"compressors"</code>, <code>"retryWrites"</code>, y <code>"zlibCompressionLevel"</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.3.0</td>
<td><p>El argumento <code>uriOptions</code> ahora acepta las opciones <code>"authMechanism"</code> y <code>"authMechanismProperties"</code>. Anteriormente, estas opciones solo eran admitidas en el argumento <code>uri</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.2.0</td>
<td><p>El argumento <code>uri</code> es ahora opcional y por omisión <code>"mongodb://</code>. El puerto por omisión sigue siendo <code>27017</code>.</p>
<p>Añadida la opción de URI <code>"appname"</code>.</p>
<p>Añadidas las opciones de controlador <code>"allow_invalid_hostname"</code>, <code>"ca_file"</code>, <code>"ca_dir"</code>, <code>"clr_file"</code>, <code>"pem_file"</code>, <code>"pem_pwd"</code>, y <code>"weak_cert_validation"</code>.</p>
<p>La API de flujos PHP ya no se utiliza para la comunicación por socket. La opción <code>"connectTimeoutMS"</code> de la URI es ahora por omisión 10 segundos en lugar de <a href="#ini.default-socket-timeout">default_socket_timeout</a> en versiones anteriores. Además, la extensión ya no admite todas las <a href="#context.ssl">opciones de contexto SSL</a> a través de la opción de controlador <code>"context"</code>.</p></td>
</tr>
<tr>
<td>PECL mongodb 1.1.0</td>
<td><p>El argumento <code>uri</code> es ahora opcional y por omisión a <code>"mongodb://localhost:27017/"</code>.</p></td>
</tr>
</tbody>
</table>

## Ejemplos

Ejemplos básicos `MongoDB\Driver\Manager::__construct`

Conexión a un nodo MongoDB autónomo:

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://example.com:27017");

?>

   
```php

Conexión a un nodo MongoDB autónomo a través de un socket de dominio Unix. La ruta del socket puede incluir caracteres especiales como barras diagonales y debe ser codificada con `rawurlencode`.

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://" . rawurlencode("/tmp/mongodb-27017.sock"));

?>

   
```php

Conexión a un conjunto de réplicas:

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://rs1.example.com,rs2.example.com/?replicaSet=myReplicaSet");

?>

   
```php

Conexión a un clúster fragmentado (es decir, una o más instancias mongos):

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://mongos1.example.com,mongos2.example.com/");

?>

   
```php

Conexión a MongoDB con credenciales de autenticación para un usuario y una base de datos específicos:

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://myusername:mypassword@example.com/?authSource=databaseName");

?>

   
```php

Conexión a MongoDB con credenciales de autenticación para un usuario y una base de datos específicos, donde el nombre de usuario o la contraseña incluye caracteres especiales (por ejemplo `@`, `:`, `%`). En el ejemplo siguiente, la cadena de contraseña `myp@ss:w%rd` ha sido manualmente escapada; sin embargo, `rawurlencode` también puede ser utilizada para escapar los componentes de la URI que pueden contener caracteres especiales.

```
<?php

$manager = new MongoDB\Driver\Manager("mongodb://myusername:myp%40ss%3Aw%25rd@example.com/?authSource=databaseName");

?>

   
```php

Conexión a MongoDB con autenticación X509:

```
<?php

$manager = new MongoDB\Driver\Manager(
    "mongodb://example.com/?ssl=true&authMechanism=MONGODB-X509",
    [],
    [
        "pem_file" => "/path/to/client.pem",
    ]
);
?>

   
```php

## Véase también

Manejo de la conexión y persistencia

Formato de cadena de conexión MongoDB
