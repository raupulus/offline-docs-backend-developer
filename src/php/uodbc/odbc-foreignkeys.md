---
title: odbc_foreignkeys
description: Lista las claves foráneas
source_url: https://www.php.net/manual/es/function.odbc-foreignkeys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-foreignkeys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98910
---

odbc_foreignkeys

Lista las claves foráneas

## Descripción

```php
odbc_foreignkeys(Odbc\Connection $odbc, string $pk_catalog, string $pk_schema, string $pk_table, string $fk_catalog, string $fk_schema, string $fk_table): Odbc\Result
```php

Devuelve una lista de claves foráneas en la tabla especificada o una lista de claves foráneas en otras tablas que hacen referencia a la clave primaria en la tabla especificada.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`fk_catalog`  
El catálogo ('qualifier' en terminología ODBC 2) de la clave primaria de la tabla.

`pk_schema`  
El esquema ('qualifier' en terminología ODBC 2) de la clave primaria de la tabla.

`pk_table`  
La tabla de clave primaria.

`pk_catalog`  
El catálogo ('qualifier' en terminología ODBC 2) de la clave foránea de la tabla.

`fk_schema`  
El esquema ('qualifier' en terminología ODBC 2) de la clave foránea de la tabla.

`fk_table`  
La tabla de clave foránea.

## Valores devueltos

Devuelve un objeto de resultado ODBC o `false` si ocurre un error.

El conjunto de resultados contiene las siguientes columnas:

- `PKTABLE_CAT`

- `PKTABLE_SCHEM`

- `PKTABLE_NAME`

- `PKCOLUMN_NAME`

- `FKTABLE_CAT`

- `FKTABLE_SCHEM`

- `FKTABLE_NAME`

- `FKCOLUMN_NAME`

- `KEY_SEQ`

- `UPDATE_RULE`

- `DELETE_RULE`

- `FK_NAME`

- `PK_NAME`

- `DEFERRABILITY`

Los controladores pueden indicar columnas adicionales.

Si las claves foráneas asociadas con una clave primaria son solicitadas, el conjunto de resultados está ordenado por `FKTABLE_CAT`, `FKTABLE_SCHEM`, `FKTABLE_NAME` y `KEY_SEQ`. Si las claves primarias asociadas con una clave foránea son solicitadas, el conjunto de resultados está ordenado por `PKTABLE_CAT`, `PKTABLE_SCHEM`, `PKTABLE_NAME` y `KEY_SEQ`.

Si `pk_table` contiene un nombre de tabla, `odbc_foreignkeys` retorna la clave primaria de la tabla `pk_table`, y todas las claves foráneas que hacen referencia a ella.

Si `fk_table` contiene un nombre de tabla, `odbc_foreignkeys` retorna la lista de claves foráneas de la tabla `fk_table`, y las claves primarias (de otras tablas) que hacen referencia a ella.

Si `pk_table` y `fk_table` contienen nombres de tablas, `odbc_foreignkeys` retorna la lista de claves foráneas de la tabla `fk_table` que utilizan la clave primaria de la tabla `pk_table`. Esta lista debería contener como máximo una clave.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Result` ; anteriormente, se devolvía un `resource`. |

## Véase también

`odbc_tables`, `odbc_primarykeys`
