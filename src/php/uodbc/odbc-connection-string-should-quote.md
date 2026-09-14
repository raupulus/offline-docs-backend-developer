---
title: odbc_connection_string_should_quote
description: Determina si un valor de string de conexión ODBC debe ser puesto entre
  comillas
source_url: https://www.php.net/manual/es/function.odbc-connection-string-should-quote.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-connection-string-should-quote.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: d80850163
order: 98730
---

odbc_connection_string_should_quote

Determina si un valor de string de conexión ODBC debe ser puesto entre comillas

## Descripción

```php
odbc_connection_string_should_quote(string $str): bool
```php

Determina si un string debe ser puesto entre comillas para una conexión ODBC. Es decir, si contiene caracteres especiales.

Tenga en cuenta que esta función no verifica si el string ya está entre comillas; un string ya entre comillas contendrá caracteres que harán que esta función devuelva verdadero. Se debería llamar a `odbc_connection_string_is_quoted` para verificar.

## Parámetros

`str`  
El string a verificar.

## Valores devueltos

`true` si el string debe estar entre comillas, de lo contrario `false`.

## Véase también

`odbc_connection_string_quote`, `odbc_connection_string_is_quoted`
