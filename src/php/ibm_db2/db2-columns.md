---
title: db2_columns
description: Devuelve un conjunto de resultados que lista las columnas y sus metadatos
  de una tabla
source_url: https://www.php.net/manual/es/function.db2-columns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-columns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30670
---

db2_columns

Devuelve un conjunto de resultados que lista las columnas y sus metadatos de una tabla

## Descripción

```php
db2_columns(resource $connection, [string $qualifier], [string $schema], [string $table_name], [string $column_name]): resource
```php

Devuelve un conjunto de resultados que lista las columnas y sus metadatos de una tabla.

## Parámetros

`connection`  
Una conexión válida a una base de datos IBM DB2, Cloudscape o Apache Derby.

`qualifier`  
Un calificador para las bases de datos DB2 que funcionan en los servidores OS/390 o z/OS. Para otras bases de datos, se debe pasar `null` o una cadena vacía.

`schema`  
El esquema que contiene las tablas. Para coincidir con todos los esquemas, se debe pasar `'%'`.

`table_name`  
El nombre de la tabla. Para obtener todas las tablas en la base de datos, se debe pasar `null` o una cadena vacía.

`column_name`  
El nombre de la columna. Para obtener todas las columnas de la tabla, se debe pasar `null` o una cadena vacía.

## Valores devueltos

Devuelve un recurso con el conjunto de resultados que contiene las filas que describen los privilegios de las columnas que coinciden con los parámetros especificados. Las filas están compuestas por las siguientes columnas:

| Nombre de la columna | Descripción |
|----|----|
| TABLE_CAT | Nombre del catálogo. El valor es `null` si la tabla no posee catálogo. |
| TABLE_SCHEM | Nombre del esquema. |
| TABLE_NAME | Nombre de la tabla. |
| COLUMN_NAME | Nombre de la columna. |
| DATA_TYPE | El tipo de datos SQL para la columna, representado como un integer. |
| TYPE_NAME | Una cadena que representa el tipo de datos para la columna. |
| COLUMN_SIZE | Un integer que representa el tamaño de la columna. |
| BUFFER_LENGTH | Número máximo de bytes necesarios para almacenar datos de esta columna. |
| DECIMAL_DIGITS | La escala de la columna o `null` donde la escala no es aplicable. |
| NUM_PREC_RADIX | Un integer que puede ser `10` (que representa un tipo de datos numérico exacto), `2` (que representa un tipo de datos numéricos aproximado) o `null` (que representa un tipo de datos para el cual la base no es aplicable). |
| NULLABLE | Un integer que representa si la columna puede ser nula o no. |
| REMARKS | Descripción de la columna. |
| COLUMN_DEF | Valor por defecto de la columna. |
| SQL_DATA_TYPE | Un integer que representa el tamaño de la columna. |
| SQL_DATETIME_SUB | Devuelve un integer que representa un código de subtipo `datetime` o `null` si los tipos de datos SQL no aplican. |
| CHAR_OCTET_LENGTH | Tamaño máximo en bytes para los tipos de datos de carácter de la columna, que coincide con COLUMN_SIZE para un solo byte de datos o `null` para un tipo de datos que no son caracteres. |
| ORDINAL_POSITION | La posición de la columna comenzando desde 1 en la tabla. |
| IS_NULLABLE | Una cadena cuyo valor es 'YES' significa que la columna es nula y 'NO' significa que la columna no puede ser nula. |

## Véase también

db2_column_privileges

db2_foreign_keys

db2_primary_keys

db2_procedure_columns

db2_procedures

db2_special_columns

db2_statistics

db2_table_privileges

db2_tables
