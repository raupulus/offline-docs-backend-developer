---
title: db2_foreign_keys
description: Devuelve un conjunto de resultados que lista las claves externas de una
  tabla
source_url: https://www.php.net/manual/es/function.db2-foreign-keys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-foreign-keys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30880
---

db2_foreign_keys

Devuelve un conjunto de resultados que lista las claves externas de una tabla

## Descripción

```php
db2_foreign_keys(resource $connection, string $qualifier, string $schema, string $table_name): resource
```php

Devuelve un conjunto de resultados que lista las claves externas de una tabla.

## Parámetros

`connection`  
Una conexión válida a una base de datos IBM DB2, Cloudscape o Apache Derby.

`qualifier`  
Un calificador para las bases de datos DB2 que funcionan en los servidores OS/390 o z/OS. Para otras bases de datos, pase `null` o una cadena vacía.

`schema`  
El esquema que contiene las tablas. Si `schema` es `null`, `db2_foreign_keys` hace coincidir el esquema para la conexión actual.

`table_name`  
El nombre de la tabla.

## Valores devueltos

Devuelve un recurso con el conjunto de resultados que contiene filas que describen las claves externas de la tabla especificada. El conjunto de resultados está compuesto por las siguientes columnas:

| Nombre de la columna | Descripción |
|----|----|
| PKTABLE_CAT | Nombre del catálogo de la tabla que contiene la clave primaria. El valor es `null` si la tabla no tiene catálogo. |
| PKTABLE_SCHEM | Nombre del esquema de la tabla que contiene la clave primaria. |
| PKTABLE_NAME | Nombre de la tabla que contiene la clave primaria. |
| PKCOLUMN_NAME | Nombre de la columna que contiene la clave primaria. |
| FKTABLE_CAT | Nombre del catálogo de la tabla que contiene la clave externa. El valor es `null` si la tabla no tiene catálogo. |
| FKTABLE_SCHEM | Nombre del esquema de la tabla que contiene la clave externa. |
| FKTABLE_NAME | Nombre de la tabla que contiene la clave externa. |
| FKCOLUMN_NAME | Nombre de la columna que contiene la clave externa. |
| KEY_SEQ | Posición, comenzando en 1, de la columna en la clave. |
| UPDATE_RULE | Entero que representa la acción aplicada a la clave externa cuando una operación es de tipo UPDATE. |
| DELETE_RULE | Entero que representa la acción aplicada a la clave externa cuando una operación es de tipo DELETE. |
| FK_NAME | Nombre de la clave externa. |
| PK_NAME | Nombre de la clave primaria. |
| DEFERRABILITY | Un entero que representa si el modo diferido de la clave externa es SQL_INITIALLY_DEFERRED, SQL_INITIALLY_IMMEDIATE o SQL_NOT_DEFERRABLE. |

## Véase también

db2_column_privileges

db2_columns

db2_primary_keys

db2_procedure_columns

db2_procedures

db2_special_columns

db2_statistics

db2_table_privileges

db2_tables
