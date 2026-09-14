---
title: mysqli_sql_exception::getSqlState
description: Devuelve el código de error SQLSTATE
source_url: https://www.php.net/manual/es/mysqli-sql-exception.getsqlstate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_sql_exception/getsqlstate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55700
---

mysqli_sql_exception::getSqlState

Devuelve el código de error SQLSTATE

## Descripción

```php
public mysqli_sql_exception::getSqlState(): string
```php

Devuelve un string que contiene el código de error SQLSTATE para el último error. El código de error está compuesto por cinco caracteres. Los valores están especificados por ANSI SQL y ODBC. Para una lista de los valores posibles, ver <http://dev.mysql.com/doc/mysql/en/error-handling.html>.

> [!NOTE]
> Cabe señalar que no todos los errores de MySQL están mapeados a SQLSTATE. El valor `HY000` (error general) se utiliza para los errores no mapeados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un string que contiene el código de error SQLSTATE para el último error. El código de error está compuesto por cinco caracteres.
