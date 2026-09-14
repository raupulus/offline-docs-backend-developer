---
title: db2_statistics
description: Devuelve un conjunto de resultados que enumera los índices y estadísticas
  de una tabla
source_url: https://www.php.net/manual/es/function.db2-statistics.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-statistics.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 31080
---

db2_statistics

Devuelve un conjunto de resultados que enumera los índices y estadísticas de una tabla

## Descripción

```php
db2_statistics(resource $connection, string $qualifier, string $schema, string $table_name, bool $unique): resource
```php

Devuelve un conjunto de resultados que enumera los índices y estadísticas de una tabla.

## Parámetros

`connection`  
Una conexión válida a una base de datos IBM DB2, Cloudscape o Apache Derby.

`qualifier`  
Un calificador para las bases de datos DB2 que funcionan en servidores OS/390 o z/OS. Para otras bases de datos, se debe pasar `null` o una string vacía.

`schema`  
El esquema que contiene las tablas objetivo. Si el argumento es `null`, se devuelven las estadísticas y los índices para el esquema del usuario actual.

`table_name`  
El nombre de la tabla.

`unique`  
Cuando `unique` es `true`, se devuelve la información relativa a todos los índices de la tabla. De lo contrario, solo se devuelve la información relativa a los índices únicos de la tabla.

## Valores devueltos

Devuelve un recurso de sentencia con un conjunto de resultados que contiene filas que describen las estadísticas e índices para las tablas base que coinciden con los parámetros especificados. Las filas están compuestas por las columnas siguientes:

<table>
<thead>
<tr>
<th>Nombre de la columna</th>
<th>Descripción</th>
</tr>
</thead>
<tbody>
<tr>
<td>TABLE_CAT</td>
<td>Nombre del catálogo que contiene la tabla. El valor es <code>null</code> si la tabla no tiene catálogo.</td>
</tr>
<tr>
<td>TABLE_SCHEM</td>
<td>Nombre del esquema que contiene la tabla.</td>
</tr>
<tr>
<td>TABLE_NAME</td>
<td>Nombre de la tabla.</td>
</tr>
<tr>
<td>NON_UNIQUE</td>
<td><p>Un integer que representa si el índice prohíbe valores únicos o si la fila contiene estadísticas sobre la tabla misma:</p>
<table>
<thead>
<tr>
<th>Valor de retorno</th>
<th>Tipo de argumento</th>
</tr>
</thead>
<tbody>
<tr>
<td>0 (SQL_FALSE)</td>
<td>El índice permite valores duplicados.</td>
</tr>
<tr>
<td>1 (SQL_TRUE)</td>
<td>Los valores del índice deben ser únicos.</td>
</tr>
<tr>
<td><code>null</code></td>
<td>La fila contiene información estadística sobre la tabla.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>INDEX_QUALIFIER</td>
<td>Una string que representa un calificador que debería haber sido previamente fijado a INDEX_NAME para calificar completamente el índice.</td>
</tr>
<tr>
<td>INDEX_NAME</td>
<td>Una string que representa el nombre del índice.</td>
</tr>
<tr>
<td>TYPE</td>
<td><p>Un integer que representa el tipo de información contenida en esta fila del conjunto de resultados:</p>
<table>
<thead>
<tr>
<th>Valor de retorno</th>
<th>Tipo de argumento</th>
</tr>
</thead>
<tbody>
<tr>
<td>0 (SQL_TABLE_STAT)</td>
<td>La fila contiene información estadística sobre la tabla.</td>
</tr>
<tr>
<td>1 (SQL_INDEX_CLUSTERED)</td>
<td>La fila contiene información sobre un índice agrupado.</td>
</tr>
<tr>
<td>2 (SQL_INDEX_HASH)</td>
<td>La fila contiene información sobre un índice hash.</td>
</tr>
<tr>
<td>3 (SQL_INDEX_OTHER)</td>
<td>La fila contiene información sobre un tipo de índice que no es agrupado ni hash.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>ORDINAL_POSITION</td>
<td>Un array que comienza en el índice 1 indicando la columna en el índice. <code>null</code> si la fila contiene información estadística sobre la tabla.</td>
</tr>
<tr>
<td>COLUMN_NAME</td>
<td>El nombre de la columna en el índice. <code>null</code> si la fila contiene información estadística sobre la tabla.</td>
</tr>
<tr>
<td>ASC_OR_DESC</td>
<td><code>A</code> si la columna está ordenada en orden alfabético, <code>D</code> si la columna está ordenada en orden alfabético inverso, <code>null</code> si la fila contiene información estadística sobre la tabla.</td>
</tr>
<tr>
<td>CARDINALITY</td>
<td><p>Si la fila contiene información sobre un índice, esta columna contendrá un integer que representa el número de valores únicos en el índice.</p>
<p>Si la fila contiene información sobre la tabla, esta columna contendrá un integer que representa el número de filas en la tabla.</p></td>
</tr>
<tr>
<td>PAGES</td>
<td><p>Si la fila contiene información sobre un índice, esta columna contendrá un integer que representa el número de páginas utilizadas para registrar el índice.</p>
<p>Si la fila contiene información sobre la tabla, esta columna contendrá un integer que representa el número de páginas utilizadas para registrar la tabla.</p></td>
</tr>
<tr>
<td>FILTER_CONDITION</td>
<td>Siempre devuelve <code>null</code>.</td>
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

db2_special_columns

db2_table_privileges

db2_tables
