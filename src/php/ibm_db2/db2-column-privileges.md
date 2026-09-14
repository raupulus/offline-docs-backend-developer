---
title: db2_column_privileges
description: Devuelve un conjunto de resultados que lista las columnas y sus privilegios
  de una tabla
source_url: https://www.php.net/manual/es/function.db2-column-privileges.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-column-privileges.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30660
---

db2_column_privileges

Devuelve un conjunto de resultados que lista las columnas y sus privilegios de una tabla

## Descripción

```php
db2_column_privileges(resource $connection, [string $qualifier], [string $schema], [string $table_name], [string $column_name]): resource
```php

Devuelve un conjunto de resultados que lista las columnas y sus privilegios de una tabla.

## Parámetros

`connection`  
Una conexión válida a una base de datos IBM DB2, Cloudscape o Apache Derby.

`qualifier`  
Un calificador para las bases de datos DB2 que funcionan en los servidores OS/390 o z/OS. Para otras bases de datos, pase `null` o una cadena vacía.

`schema`  
El esquema que contiene las tablas. Para coincidir con todos los esquemas, pase `null` o una cadena vacía.

`table_name`  
El nombre de la tabla. Para obtener todas las tablas en la base de datos, pase `null` o una cadena vacía.

`column_name`  
El nombre de la columna. Para obtener todas las columnas de la tabla, pase `null` o una cadena vacía.

## Valores devueltos

Devuelve un recurso con el conjunto de resultados que contiene las filas que describen los privilegios de las columnas que coinciden con los parámetros especificados. Las filas están compuestas por las siguientes columnas:

| Nombre de la columna | Descripción |
|----|----|
| TABLE_CAT | Nombre del catálogo. El valor es `null` si la tabla no posee catálogo. |
| TABLE_SCHEM | Nombre del esquema. |
| TABLE_NAME | Nombre de la tabla. |
| COLUMN_NAME | Nombre de la columna. |
| GRANTOR | ID de autorización del usuario que concedió el privilegio. |
| GRANTEE | ID de autorización del usuario al que se le concedió el privilegio. |
| PRIVILEGE | El privilegio para la columna. |
| IS_GRANTABLE | Si GRANTEE está permitido para conceder este privilegio a otros usuarios. |

## Véase también

db2_columns

db2_foreign_keys

db2_primary_keys

db2_procedure_columns

db2_procedures

db2_special_columns

db2_statistics

db2_table_privileges

db2_tables
