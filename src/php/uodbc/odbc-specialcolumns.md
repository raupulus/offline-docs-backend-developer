---
title: odbc_specialcolumns
description: Devuelve el conjunto óptimo de columnas
source_url: https://www.php.net/manual/es/function.odbc-specialcolumns.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-specialcolumns.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 99070
---

odbc_specialcolumns

Devuelve el conjunto óptimo de columnas

## Descripción

```php
odbc_specialcolumns(Odbc\Connection $odbc, int $type, string $catalog, string $schema, string $table, int $scope, int $nullable): Odbc\Result
```php

Devuelve el conjunto óptimo de columnas que identifica de manera única una fila de una tabla, o las columnas que se actualizan automáticamente cuando alguno de los valores de la fila es modificado por una transacción.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`type`  
Cuando el tipo es `SQL_BEST_ROWID`, `odbc_specialcolumns` devuelve la o las columnas que permiten identificar de manera única cada fila de una tabla.

Cuando el tipo es `SQL_ROWVER`, `odbc_specialcolumns` devuelve la columna o las columnas de la tabla especificada, si las hay, que se actualizan automáticamente por los datos de origen cuando cada valor de la fila es modificado por cualquier transacción.

`catalog`  
El catálogo ('calificativo' en el argot ODBC 2).

`schema`  
El esquema ('propietario' en el argot ODBC 2).

`table`  
La tabla.

`scope`  
El `scope`, que ordena el conjunto de resultados. Uno de `SQL_SCOPE_CURROW`, `SQL_SCOPE_TRANSACTION` o `SQL_SCOPE_SESSION`.

`nullable`  
Determina si las columnas especiales que pueden tener un valor NULL deben ser devueltas o no. Uno de `SQL_NO_NULLS` o `SQL_NULLABLE`.

## Valores devueltos

Devuelve un objeto de resultado ODBC o `false` si ocurre un error.

El conjunto de resultados contiene las siguientes columnas:

- `SCOPE`

- `COLUMN_NAME`

- `DATA_TYPE`

- `TYPE_NAME`

- `COLUMN_SIZE`

- `BUFFER_LENGTH`

- `DECIMAL_DIGITS`

- `PSEUDO_COLUMN`

Los controladores pueden indicar columnas adicionales.

El conjunto de resultados está ordenado por `SCOPE`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Result` ; anteriormente, se devolvía un `resource`. |

## Véase también

`odbc_tables`
