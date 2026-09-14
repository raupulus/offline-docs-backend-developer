---
title: db2_special_columns
description: Devuelve un conjunto de resultados que lista los identificadores únicos
  de las filas de una tabla
source_url: https://www.php.net/manual/es/function.db2-special-columns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-special-columns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 31070
---

db2_special_columns

Devuelve un conjunto de resultados que lista los identificadores únicos de las filas de una tabla

## Descripción

```php
db2_special_columns(resource $connection, string $qualifier, string $schema, string $table_name, int $scope): resource
```php

Devuelve un conjunto de resultados que lista los identificadores únicos de las filas de una tabla.

## Parámetros

`connection`  
Una conexión válida a una base de datos IBM DB2, Cloudscape o Apache Derby.

`qualifier`  
Un calificador para las bases de datos DB2 que funcionan en servidores OS/390 o z/OS. Para otras bases de datos, se debe pasar `null` o una cadena vacía.

`schema`  
El esquema que contiene las tablas.

`table_name`  
El nombre de la tabla.

`scope`  
Un entero que representa el tiempo mínimo para el cual el identificador único de la fila es válido. Puede ser uno de los siguientes valores:

| Valor entero | Constante SQL | Descripción |
|----|----|----|
| 0 | SQL_SCOPE_CURROW | El identificador de la fila es válido solo cuando el cursor está posicionado en la fila. |
| 1 | SQL_SCOPE_TRANSACTION | El identificador de la fila es válido durante la duración de la transacción. |
| 2 | SQL_SCOPE_SESSION | El identificador de la fila es válido durante la duración de la conexión. |

## Valores devueltos

Devuelve un recurso con un conjunto de resultados que contiene filas con información única para una tabla. Las filas están compuestas por las siguientes columnas:

<table>
<thead>
<tr>
<th>Nombre de la columna</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>SCOPE</td>
<td><table>
<thead>
<tr>
<th>Valor entero</th>
<th>Constante SQL</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td>SQL_SCOPE_CURROW</td>
<td>El identificador de la fila es válido solo cuando el cursor está posicionado en la fila.</td>
</tr>
<tr>
<td>1</td>
<td>SQL_SCOPE_TRANSACTION</td>
<td>El identificador de la fila es válido durante la duración de la transacción.</td>
</tr>
<tr>
<td>2</td>
<td>SQL_SCOPE_SESSION</td>
<td>El identificador de la fila es válido durante la duración de la conexión.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>COLUMN_NAME</td>
<td>Nombre de la columna única.</td>
</tr>
<tr>
<td>DATA_TYPE</td>
<td>El tipo de datos SQL para la columna.</td>
</tr>
<tr>
<td>TYPE_NAME</td>
<td>Una cadena que representa el tipo de datos para la columna.</td>
</tr>
<tr>
<td>COLUMN_SIZE</td>
<td>Un entero que representa el tamaño de la columna.</td>
</tr>
<tr>
<td>BUFFER_LENGTH</td>
<td>Número máximo de bytes necesarios para almacenar datos de esta columna.</td>
</tr>
<tr>
<td>DECIMAL_DIGITS</td>
<td>La escala de la columna o <code>null</code> donde la escala no es aplicable.</td>
</tr>
<tr>
<td>NUM_PREC_RADIX</td>
<td>Un entero que puede ser <code>10</code> (representando un tipo de datos numérico exacto), <code>2</code> (representando un tipo de datos numéricos aproximados) o <code>null</code> (representando un tipo de datos para el cual la base no es aplicable).</td>
</tr>
<tr>
<td>PSEUDO_COLUMN</td>
<td>Siempre devuelve 1.</td>
</tr>
</tbody>
</table>

## Véase también

db2_column_privileges

db2_columns

db2_foreign_keys

db2_primary_keys

db2_procedure_columns

db2_procedures

db2_statistics

db2_table_privileges

db2_tables
