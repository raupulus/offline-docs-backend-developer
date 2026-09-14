---
title: db2_tables
description: Devuelve la lista de tablas y sus metadatos
source_url: https://www.php.net/manual/es/function.db2-tables.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-tables.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 31120
---

db2_tables

Devuelve la lista de tablas y sus metadatos

## Descripción

```php
db2_tables(resource $connection, [string $qualifier], [string $schema], [string $table_name], [string $table_type]): resource
```php

Devuelve un conjunto de resultados que lista las tablas y sus metadatos asociados de una base de datos.

## Parámetros

`connection`  
Una conexión válida a una base de datos IBM DB2, Cloudscape o Apache Derby.

`qualifier`  
Un calificador para las bases de datos DB2 que funcionan en servidores OS/390 o z/OS. Para otras bases de datos, se debe pasar `null` o una cadena vacía.

`schema`  
El esquema que contiene las tablas. El argumento acepta formas que contienen `_` y `%` como comodines.

`table_name`  
El nombre de la tabla. El argumento acepta formas que contienen `_` y `%` como comodines.

`table_type`  
Una lista de identificadores de tipos de tabla delimitada por comas. Para coincidir con todos los esquemas, se debe pasar `null` o una cadena vacía. Los identificadores válidos son: ALIAS, HIERARCHY TABLE, INOPERATIVE VIEW, NICKNAME, MATERIALIZED QUERY TABLE, SYSTEM TABLE, TABLE, TYPED TABLE, TYPED VIEW y VIEW.

## Valores devueltos

Devuelve un recurso con el conjunto de resultados que contiene las filas que describen las tablas que coinciden con los argumentos especificados. Las filas están compuestas por las siguientes columnas:

| Nombre de la columna | Descripción |
|----|----|
| TABLE_CAT | Nombre del catálogo que contiene la tabla. El valor es `null` si la tabla no tiene catálogo. |
| TABLE_SCHEM | Nombre del esquema que contiene la tabla. |
| TABLE_NAME | Nombre de la tabla. |
| TABLE_TYPE | Identificador de la tabla. |
| REMARKS | Descripción de la tabla. |

## Véase también

db2_column_privileges

db2_columns

db2_foreign_keys

db2_primary_keys

db2_procedure_columns

db2_procedures

db2_special_columns

db2_statistics

db2_table_privileges
