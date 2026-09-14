---
title: db2_procedure_columns
description: Devuelve un conjunto de resultados que lista los argumentos de procedimiento
  de registro
source_url: https://www.php.net/manual/es/function.db2-procedure-columns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-procedure-columns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 31010
---

db2_procedure_columns

Devuelve un conjunto de resultados que lista los argumentos de procedimiento de registro

## Descripción

```php
db2_procedure_columns(resource $connection, string $qualifier, string $schema, string $procedure, string $parameter): resource
```php

Devuelve un conjunto de resultados que lista los argumentos para uno o varios procedimientos de registro.

## Parámetros

`connection`  
Una conexión válida a una base de datos IBM DB2, Cloudscape o Apache Derby.

`qualifier`  
Un calificador para las bases de datos DB2 que funcionan en los servidores OS/390 o z/OS. Para otras bases de datos, pase `null` o una cadena vacía.

`schema`  
El esquema que contiene las tablas. El argumento acepta formas que contienen `_` y `%` como comodín.

`procedure`  
El nombre del procedimiento. El argumento acepta formas que contienen `_` y `%` como comodín.

`parameter`  
El nombre del argumento. Este argumento acepta un argumento de búsqueda que contiene `_` y `%` como comodín. Si este argumento es `null`, se devuelven todos los argumentos para el procedimiento de registro especificado.

## Valores devueltos

Devuelve un recurso con el conjunto de resultados que contiene las filas que describen los argumentos para los procedimientos de registro que coinciden con los argumentos especificados. Las filas están compuestas por las siguientes columnas:

<table>
<thead>
<tr>
<th>Nombre de la columna</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>PROCEDURE_CAT</td>
<td>Nombre del catálogo que contiene la tabla. El valor es <code>null</code> si la tabla no tiene catálogo.</td>
</tr>
<tr>
<td>PROCEDURE_SCHEM</td>
<td>Nombre del esquema que contiene el procedimiento de registro.</td>
</tr>
<tr>
<td>PROCEDURE_NAME</td>
<td>Nombre del procedimiento.</td>
</tr>
<tr>
<td>COLUMN_NAME</td>
<td>Nombre del argumento.</td>
</tr>
<tr>
<td>COLUMN_TYPE</td>
<td><p>Un integer que representa el tipo del argumento:</p>
<table>
<thead>
<tr>
<th>Valor de retorno</th>
<th>Tipo de argumento</th>
</tr>
</thead>
<tbody>
<tr>
<td>1 (SQL_PARAM_INPUT)</td>
<td>Argumento de entrada (IN).</td>
</tr>
<tr>
<td>2 (SQL_PARAM_INPUT_OUTPUT)</td>
<td>Argumento de entrada/salida (INOUT).</td>
</tr>
<tr>
<td>3 (SQL_PARAM_OUTPUT)</td>
<td>Argumento de salida (OUT).</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>DATA_TYPE</td>
<td>El tipo de datos SQL para el argumento representado como integer.</td>
</tr>
<tr>
<td>TYPE_NAME</td>
<td>Una string que representa el tipo de datos para el argumento.</td>
</tr>
<tr>
<td>COLUMN_SIZE</td>
<td>Un integer que representa el tamaño del argumento.</td>
</tr>
<tr>
<td>BUFFER_LENGTH</td>
<td>Número máximo de bytes necesarios para almacenar datos de este argumento.</td>
</tr>
<tr>
<td>DECIMAL_DIGITS</td>
<td>La escala del argumento o <code>null</code> donde la escala no es aplicable.</td>
</tr>
<tr>
<td>NUM_PREC_RADIX</td>
<td>Un integer que puede ser <code>10</code> (que representa un tipo de datos numérico exacto), <code>2</code> (que representa una aproximación de tipo de datos numéricos) o <code>null</code> (que representa un tipo de datos para el cual la base no es aplicable).</td>
</tr>
<tr>
<td>NULLABLE</td>
<td>Un integer que representa si el argumento puede ser nulo o no.</td>
</tr>
<tr>
<td>REMARKS</td>
<td>Descripción del argumento.</td>
</tr>
<tr>
<td>COLUMN_DEF</td>
<td>Valor por defecto del argumento.</td>
</tr>
<tr>
<td>SQL_DATA_TYPE</td>
<td>Un integer que representa el tamaño del argumento.</td>
</tr>
<tr>
<td>SQL_DATETIME_SUB</td>
<td>Devuelve un integer que representa un código de subtipo <code>datetime</code> o <code>null</code> si los tipos de datos SQL no aplican.</td>
</tr>
<tr>
<td>CHAR_OCTET_LENGTH</td>
<td>Tamaño máximo en bytes para los tipos de datos de carácter del argumento, que coincide con COLUMN_SIZE para un solo byte de datos o <code>null</code> para un tipo de datos que no es de caracteres.</td>
</tr>
<tr>
<td>ORDINAL_POSITION</td>
<td>La posición del argumento comenzando en 1 en la consulta <code>CALL</code>.</td>
</tr>
<tr>
<td>IS_NULLABLE</td>
<td>Una string cuyo valor es <code>YES</code> significa que el argumento acepta o devuelve valores <code>null</code> y <code>NO</code> significa que el argumento no acepta ni devuelve valores <code>null</code>.</td>
</tr>
</tbody>
</table>

## Véase también

db2_column_privileges

db2_columns

db2_foreign_keys

db2_primary_keys

db2_procedures

db2_special_columns

db2_statistics

db2_table_privileges

db2_tables
