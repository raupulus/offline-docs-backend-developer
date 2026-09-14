---
title: db2_client_info
description: Devuelve un objeto con propiedades que describen el cliente de base de
  datos DB2
source_url: https://www.php.net/manual/es/function.db2-client-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-client-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30640
---

db2_client_info

Devuelve un objeto con propiedades que describen el cliente de base de datos DB2

## Descripción

```php
db2_client_info(resource $connection): stdClass
```php

Esta función devuelve un objeto con propiedades en solo lectura que proporcionan información sobre el cliente de base de datos DB2. La tabla siguiente lista las propiedades del cliente DB2:

<table>
<caption>Propiedades del cliente DB2</caption>
<thead>
<tr>
<th>Nombre Propiedad</th>
<th>Tipo de retorno</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>APPL_CODEPAGE</td>
<td><code>int</code></td>
<td>La aplicación es un código de página.</td>
</tr>
<tr>
<td>CONN_CODEPAGE</td>
<td><code>int</code></td>
<td>El código de página para la conexión actual.</td>
</tr>
<tr>
<td>DATA_SOURCE_NAME</td>
<td><code>string</code></td>
<td>El nombre de la fuente de datos (DSN) utilizado para crear la conexión actual a la base de datos.</td>
</tr>
<tr>
<td>DRIVER_NAME</td>
<td><code>string</code></td>
<td>El nombre de la biblioteca que implementa la especificación <code>DB2 Call Level Interface</code> (CLI).</td>
</tr>
<tr>
<td>DRIVER_ODBC_VER</td>
<td><code>string</code></td>
<td>La versión de ODBC que el cliente DB2 soporta. Esto devuelve una <code>string</code> <code>"MM.mm"</code> donde <code>MM</code> es la versión mayor y <code>mm</code> es la versión menor. El cliente DB2 siempre devuelve <code>"03.51"</code>.</td>
</tr>
<tr>
<td>DRIVER_VER</td>
<td><code>string</code></td>
<td>La versión del cliente, en la forma de una <code>string</code> <code>"MM.mm.uuuu"</code> donde <code>MM</code> es la versión mayor, <code>mm</code> es la versión menor y <code>uuuu</code> es la actualización. Por ejemplo, <code>"08.02.0001"</code> representa la versión mayor 8, la versión menor 2, y la actualización 1.</td>
</tr>
<tr>
<td>ODBC_SQL_CONFORMANCE</td>
<td><code>string</code></td>
<td><p>El nivel de sintaxis soportado por el cliente:</p>
<dl>
<dt>MINIMUM</dt>
<dd>
<p>Soporta el mínimo de sintaxis SQL de ODBC.</p>
</dd>
<dt>CORE</dt>
<dd>
<p>Soporta el núcleo de sintaxis SQL de ODBC.</p>
</dd>
<dt>EXTENDED</dt>
<dd>
<p>Soporta la sintaxis extendida SQL de ODBC.</p>
</dd>
</dl></td>
</tr>
<tr>
<td>ODBC_VER</td>
<td><code>string</code></td>
<td>La versión de ODBC que el administrador de controladores ODBC soporta. Esto devuelve una <code>string</code> <code>"MM.mm.rrrr"</code> donde <code>MM</code> es la versión mayor, <code>mm</code> es la versión menor y <code>rrrr</code> es la actualización. El cliente DB2 siempre devuelve <code>"03.01.0000"</code>.</td>
</tr>
</tbody>
</table>

## Parámetros

`connection`  
Especifica la conexión cliente DB2 activa.

## Valores devueltos

Devuelve un objeto si la llamada es exitosa, o `false` si ocurre un error

## Ejemplos

Ejemplo con `db2_client_info`

Para obtener información sobre el cliente, se debe pasar un recurso de conexión de base de datos válido a la función `db2_client_info`.

```
<?php
$conn = db2_connect( 'SAMPLE', 'db2inst1', 'ibmdb2' );
$client = db2_client_info( $conn );

if ($client) {
    echo "DRIVER_NAME: ";   var_dump( $client->DRIVER_NAME );
    echo "DRIVER_VER: ";   var_dump( $client->DRIVER_VER );
    echo "DATA_SOURCE_NAME: ";   var_dump( $client->DATA_SOURCE_NAME );
    echo "DRIVER_ODBC_VER: ";   var_dump( $client->DRIVER_ODBC_VER );
    echo "ODBC_VER: ";    var_dump( $client->ODBC_VER );
    echo "ODBC_SQL_CONFORMANCE: ";  var_dump( $client->ODBC_SQL_CONFORMANCE );
    echo "APPL_CODEPAGE: ";   var_dump( $client->APPL_CODEPAGE );
    echo "CONN_CODEPAGE: ";   var_dump( $client->CONN_CODEPAGE );
}
else {
    echo "Error al obtener la información del cliente.
     Quizás su conexión a la base de datos era inválida.";
}
db2_close($conn);

?>
   
```php

El ejemplo anterior mostrará:

    DRIVER_NAME: string(8) "libdb2.a"
    DRIVER_VER: string(10) "08.02.0001"
    DATA_SOURCE_NAME: string(6) "SAMPLE"
    DRIVER_ODBC_VER: string(5) "03.51"
    ODBC_VER: string(10) "03.01.0000"
    ODBC_SQL_CONFORMANCE: string(8) "EXTENDED"
    APPL_CODEPAGE: int(819)
    CONN_CODEPAGE: int(819)

## Véase también

db2_server_info
