---
title: db2_server_info
description: Devuelve un objeto con propiedades que describen el servidor de base
  de datos DB2
source_url: https://www.php.net/manual/es/function.db2-server-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-server-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 31050
---

db2_server_info

Devuelve un objeto con propiedades que describen el servidor de base de datos DB2

## Descripción

```php
db2_server_info(resource $connection): stdClass
```php

Esta función devuelve un objeto con propiedades de solo lectura que proporcionan información sobre el servidor de base de datos IBM DB2, Cloudscape o Apache Derby. La tabla siguiente lista las propiedades del servidor de base de datos:

<table>
<caption>Propiedades del servidor de base de datos</caption>
<thead>
<tr>
<th>Nombre de la propiedad</th>
<th>Tipo de retorno</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>DBMS_NAME</td>
<td><code>string</code></td>
<td>El nombre del servidor de base de datos al que se está conectado. Para servidores DB2, es una combinación de <code>DB2</code> seguido del sistema operativo en el que funciona el servidor de base de datos.</td>
</tr>
<tr>
<td>DBMS_VER</td>
<td><code>string</code></td>
<td>La versión del servidor de base de datos, en formato de <code>string</code> <code>"MM.mm.uuuu"</code> donde <code>MM</code> es la versión mayor, <code>mm</code> es la versión menor y <code>uuuu</code> es la actualización. Por ejemplo, <code>"08.02.0001"</code> representa la versión mayor 8, la versión menor 2, la actualización 1.</td>
</tr>
<tr>
<td>DB_CODEPAGE</td>
<td><code>int</code></td>
<td>La página de código de la base de datos a la que se está conectado.</td>
</tr>
<tr>
<td>DB_NAME</td>
<td><code>string</code></td>
<td>El nombre de la base de datos a la que se está conectado.</td>
</tr>
<tr>
<td>DFT_ISOLATION</td>
<td><code>string</code></td>
<td><p>El nivel predeterminado de aislamiento de transacción soportado por el servidor:</p>
<dl>
<dt>UR</dt>
<dd>
<p>Lectura no confirmada (<code>Uncommitted read</code>): los cambios son inmediatamente visibles para todas las transacciones concurrentes.</p>
</dd>
<dt>CS</dt>
<dd>
<p>Estabilidad del cursor (<code>Cursor stability</code>): una fila leída por una transacción puede ser modificada y confirmada por una segunda transacción concurrente.</p>
</dd>
<dt>RS</dt>
<dd>
<p>Estabilidad de lectura (<code>Read stability</code>): una transacción puede agregar o eliminar filas que coincidan con una condición de búsqueda o una transacción pendiente.</p>
</dd>
<dt>RR</dt>
<dd>
<p>Lectura repetible (<code>Repeatable read</code>): los datos afectados por las transacciones pendientes no están disponibles para otras transacciones.</p>
</dd>
<dt>NC</dt>
<dd>
<p>Sin confirmación (<code>No commit</code>): todo cambio es visible al final de una operación exitosa. Las confirmaciones explícitas y los retrocesos no están permitidos.</p>
</dd>
</dl></td>
</tr>
<tr>
<td>IDENTIFIER_QUOTE_CHAR</td>
<td><code>string</code></td>
<td>El carácter utilizado para delimitar un identificador.</td>
</tr>
<tr>
<td>INST_NAME</td>
<td><code>string</code></td>
<td>La instancia en el servidor de base de datos que contiene la base de datos.</td>
</tr>
<tr>
<td>ISOLATION_OPTION</td>
<td><code>array</code></td>
<td>Un array de opciones de aislamiento soportadas por el servidor de base de datos. Las opciones de aislamiento se describen en la propiedad DFT_ISOLATION.</td>
</tr>
<tr>
<td>KEYWORDS</td>
<td><code>array</code></td>
<td>Un array de palabras clave reservadas por el servidor de base de datos.</td>
</tr>
<tr>
<td>LIKE_ESCAPE_CLAUSE</td>
<td><code>bool</code></td>
<td><code>true</code> si el servidor de base de datos soporta el uso de los caracteres comodín <code>%</code> y <code>_</code>. <code>false</code> si el servidor de base de datos no soporta estos caracteres comodín.</td>
</tr>
<tr>
<td>MAX_COL_NAME_LEN</td>
<td><code>int</code></td>
<td>Tamaño máximo de un nombre de columna soportado por el servidor de base de datos, expresado en bytes.</td>
</tr>
<tr>
<td>MAX_IDENTIFIER_LEN</td>
<td><code>int</code></td>
<td>Tamaño máximo de un identificador SQL soportado por los servidores de base de datos, expresado en caracteres.</td>
</tr>
<tr>
<td>MAX_INDEX_SIZE</td>
<td><code>int</code></td>
<td>Tamaño máximo de las columnas combinadas en un índice soportado por el servidor de base de datos, expresado en bytes.</td>
</tr>
<tr>
<td>MAX_PROC_NAME_LEN</td>
<td><code>int</code></td>
<td>Tamaño máximo de un nombre de procedimiento soportado por el servidor de base de datos, expresado en bytes.</td>
</tr>
<tr>
<td>MAX_ROW_SIZE</td>
<td><code>int</code></td>
<td>Tamaño máximo de una fila en la tabla de base soportada por el servidor de base de datos, expresado en bytes.</td>
</tr>
<tr>
<td>MAX_SCHEMA_NAME_LEN</td>
<td><code>int</code></td>
<td>Tamaño máximo de un nombre de esquema soportado por el servidor de base de datos, expresado en bytes.</td>
</tr>
<tr>
<td>MAX_STATEMENT_LEN</td>
<td><code>int</code></td>
<td>Tamaño máximo de una consulta SQL soportada por el servidor de base de datos, expresado en bytes.</td>
</tr>
<tr>
<td>MAX_TABLE_NAME_LEN</td>
<td><code>int</code></td>
<td>Tamaño máximo de un nombre de tabla soportado por el servidor de base de datos, expresado en bytes.</td>
</tr>
<tr>
<td>NON_NULLABLE_COLUMNS</td>
<td><code>bool</code></td>
<td><code>true</code> si el servidor de base de datos soporta las columnas que pueden ser definidas como NOT NULL, <code>false</code> si el servidor de base de datos no soporta las columnas definidas como NOT NULL.</td>
</tr>
<tr>
<td>PROCEDURES</td>
<td><code>bool</code></td>
<td><code>true</code> si el servidor de base de datos soporta el uso de la consulta CALL para llamar a los procedimientos almacenados, <code>false</code> si el servidor de base de datos no soporta la consulta CALL.</td>
</tr>
<tr>
<td>SPECIAL_CHARS</td>
<td><code>string</code></td>
<td>Un <code>string</code> que contiene todos los caracteres distintos de las letras (mayúsculas y minúsculas), los dígitos y el carácter de subrayado que pueden ser utilizados como nombre de identificador.</td>
</tr>
<tr>
<td>SQL_CONFORMANCE</td>
<td><code>string</code></td>
<td><p>El nivel de conformidad con la especificación ANSI/ISO SQL-92 ofrecido por el servidor de base de datos:</p>
<dl>
<dt>ENTRY</dt>
<dd>
<p>Nivel de conformidad SQL-92.</p>
</dd>
<dt>FIPS127</dt>
<dd>
<p>Conformidad tradicional FIPS-127-2.</p>
</dd>
<dt>FULL</dt>
<dd>
<p>Nivel completo de conformidad SQL-92.</p>
</dd>
<dt>INTERMEDIATE</dt>
<dd>
<p>Nivel intermedio de conformidad SQL-92.</p>
</dd>
</dl></td>
</tr>
</tbody>
</table>

## Parámetros

`connection`  
Especifica la conexión cliente DB2 activa.

## Valores devueltos

Devuelve un objeto si la llamada es exitosa, o `false` si ocurre un error

## Ejemplos

Ejemplo con `db2_server_info`

Para recuperar información sobre el servidor, se debe pasar un recurso de conexión de base de datos válido a la función `db2_server_info`.

```
<?php

$conn = db2_connect('sample', 'db2inst1', 'ibmdb2');

$server = db2_server_info( $conn );

if ($server) {
    echo "DBMS_NAME: ";                 var_dump( $server->DBMS_NAME );
    echo "DBMS_VER: ";                  var_dump( $server->DBMS_VER );
    echo "DB_CODEPAGE: ";               var_dump( $server->DB_CODEPAGE );
    echo "DB_NAME: ";                   var_dump( $server->DB_NAME );
    echo "INST_NAME: ";                 var_dump( $server->INST_NAME );
    echo "SPECIAL_CHARS: ";             var_dump( $server->SPECIAL_CHARS );
    echo "KEYWORDS: ";                  var_dump( sizeof($server->KEYWORDS) );
    echo "DFT_ISOLATION: ";             var_dump( $server->DFT_ISOLATION );
    echo "ISOLATION_OPTION: ";
    $il = '';
    foreach( $server->ISOLATION_OPTION as $opt )
    {
       $il .= $opt." ";
    }
    var_dump( $il );
    echo "SQL_CONFORMANCE: ";           var_dump( $server->SQL_CONFORMANCE );
    echo "PROCEDURES: ";                var_dump( $server->PROCEDURES );
    echo "IDENTIFIER_QUOTE_CHAR: ";     var_dump( $server->IDENTIFIER_QUOTE_CHAR );
    echo "LIKE_ESCAPE_CLAUSE: ";        var_dump( $server->LIKE_ESCAPE_CLAUSE );
    echo "MAX_COL_NAME_LEN: ";          var_dump( $server->MAX_COL_NAME_LEN );
    echo "MAX_ROW_SIZE: ";              var_dump( $server->MAX_ROW_SIZE );
    echo "MAX_IDENTIFIER_LEN: ";        var_dump( $server->MAX_IDENTIFIER_LEN );
    echo "MAX_INDEX_SIZE: ";            var_dump( $server->MAX_INDEX_SIZE );
    echo "MAX_PROC_NAME_LEN: ";         var_dump( $server->MAX_PROC_NAME_LEN );
    echo "MAX_SCHEMA_NAME_LEN: ";       var_dump( $server->MAX_SCHEMA_NAME_LEN );
    echo "MAX_STATEMENT_LEN: ";         var_dump( $server->MAX_STATEMENT_LEN );
    echo "MAX_TABLE_NAME_LEN: ";        var_dump( $server->MAX_TABLE_NAME_LEN );
    echo "NON_NULLABLE_COLUMNS: ";      var_dump( $server->NON_NULLABLE_COLUMNS );

    db2_close($conn);
}
?>
```php

El ejemplo anterior mostrará:

    DBMS_NAME: string(9) "DB2/LINUX"
    DBMS_VER: string(10) "08.02.0000"
    DB_CODEPAGE: int(1208)
    DB_NAME: string(6) "SAMPLE"
    INST_NAME: string(8) "db2inst1"
    SPECIAL_CHARS: string(2) "@#"
    KEYWORDS: int(179)
    DFT_ISOLATION: string(2) "CS"
    ISOLATION_OPTION: string(12) "UR CS RS RR "
    SQL_CONFORMANCE: string(7) "FIPS127"
    PROCEDURES: bool(true)
    IDENTIFIER_QUOTE_CHAR: string(1) """
    LIKE_ESCAPE_CLAUSE: bool(true)
    MAX_COL_NAME_LEN: int(30)
    MAX_ROW_SIZE: int(32677)
    MAX_IDENTIFIER_LEN: int(18)
    MAX_INDEX_SIZE: int(1024)
    MAX_PROC_NAME_LEN: int(128)
    MAX_SCHEMA_NAME_LEN: int(30)
    MAX_STATEMENT_LEN: int(2097152)
    MAX_TABLE_NAME_LEN: int(128)
    NON_NULLABLE_COLUMNS: bool(true)

## Véase también

db2_client_info
