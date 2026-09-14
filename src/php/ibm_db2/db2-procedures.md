---
title: db2_procedures
description: Devuelve un conjunto de resultados que lista las proceduras de registro
  almacenadas en la base de datos
source_url: https://www.php.net/manual/es/function.db2-procedures.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-procedures.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 31020
---

db2_procedures

Devuelve un conjunto de resultados que lista las proceduras de registro almacenadas en la base de datos

## Descripción

```php
db2_procedures(resource $connection, string $qualifier, string $schema, string $procedure): resource
```php

Devuelve un conjunto de resultados que lista las proceduras de registro almacenadas en la base de datos.

## Parámetros

`connection`  
Una conexión válida a una base de datos IBM DB2, Cloudscape o Apache Derby.

`qualifier`  
Un calificador para las bases de datos DB2 que funcionan en los servidores OS/390 o z/OS. Para otras bases de datos, pase `null` o una cadena vacía.

`schema`  
El esquema que contiene las tablas. El parámetro acepta las formas que contienen `_` y `%` como palabras clave.

`procedure`  
El nombre de la procedura. El parámetro acepta las formas que contienen `_` y `%` como palabras clave.

## Valores devueltos

Devuelve un recurso con el conjunto de resultados que contiene las filas que describen las proceduras de registro que coinciden con los parámetros especificados. Las filas están compuestas por las siguientes columnas:

| Nombre de la columna | Descripción |
|----|----|
| PROCEDURE_CAT | Nombre del catálogo que contiene la tabla. El valor es `null` si la tabla no tiene catálogo. |
| PROCEDURE_SCHEM | Nombre del esquema que contiene la procedura de registro. |
| PROCEDURE_NAME | Nombre de la procedura. |
| NUM_INPUT_PARAMS | Número de parámetros de entrada (IN) para la procedura de registro. |
| NUM_OUTPUT_PARAMS | Número de parámetros de salida (OUT) para la procedura de registro. |
| NUM_RESULT_SETS | Número de conjuntos de resultados devueltos por la procedura de registro. |
| REMARKS | Comentarios sobre la procedura de registro. |
| PROCEDURE_TYPE | Siempre devuelve `1`, indicando que la procedura de registro no devuelve ningún valor de retorno. |

## Véase también

db2_column_privileges

db2_columns

db2_foreign_keys

db2_primary_keys

db2_procedure_columns

db2_special_columns

db2_statistics

db2_table_privileges

db2_tables
