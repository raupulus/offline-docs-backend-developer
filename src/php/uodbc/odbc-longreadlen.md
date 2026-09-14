---
title: odbc_longreadlen
description: Gestión de columnas de tipo LONG
source_url: https://www.php.net/manual/es/function.odbc-longreadlen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-longreadlen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98940
---

odbc_longreadlen

Gestión de columnas de tipo LONG

## Descripción

```php
odbc_longreadlen(Odbc\Result $statement, int $length): true
```php

Activa la gestión de columnas de tipo `LONG`, `LONGVARCHAR` y `LONGVARBINARY`. La longitud por defecto puede ser definida utilizando la directiva `php.ini` [uodbc.defaultlrl](#ini.uodbc.defaultlrl).

## Parámetros

`statement`  
The ODBC result object.

`length`  
El número de bytes retornado a PHP. Si se define como `0`, los datos de las columnas de tipo LONG son pasados al cliente (es decir, impresos) cuando son recuperados con la función `odbc_result`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |

## Notas

> [!NOTE]
> La gestión de tipos `LONGVARBINARY` también es afectada por `odbc_binmode`.
