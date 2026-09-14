---
title: odbc_gettypeinfo
description: Lista los tipos de datos soportados por un origen
source_url: https://www.php.net/manual/es/function.odbc-gettypeinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-gettypeinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98930
---

odbc_gettypeinfo

Lista los tipos de datos soportados por un origen

## Descripción

```php
odbc_gettypeinfo(Odbc\Connection $odbc, [int $data_type]): Odbc\Result
```php

Lista los tipos de datos soportados por un origen.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

`data_type`  
Puede ser utilizado para restringir la información a un solo tipo de datos.

## Valores devueltos

Devuelve un objeto de resultado ODBC o `false` si ocurre un error.

El resultado posee las columnas siguientes:

- TYPE_NAME

- DATA_TYPE

- PRECISION

- LITERAL_PREFIX

- LITERAL_SUFFIX

- CREATE_PARAMS

- NULLABLE

- CASE_SENSITIVE

- SEARCHABLE

- UNSIGNED_ATTRIBUTE

- MONEY

- AUTO_INCREMENT

- LOCAL_TYPE_NAME

- MINIMUM_SCALE

- MAXIMUM_SCALE

El resultado está ordenado por DATA_TYPE y TYPE_NAME.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Result` ; anteriormente, se devolvía un `resource`. |
