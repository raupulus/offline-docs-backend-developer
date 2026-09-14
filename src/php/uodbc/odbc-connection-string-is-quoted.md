---
title: odbc_connection_string_is_quoted
description: Determina si un valor de string de conexión ODBC está entre comillas
source_url: https://www.php.net/manual/es/function.odbc-connection-string-is-quoted.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-connection-string-is-quoted.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: d80850163
order: 98710
---

odbc_connection_string_is_quoted

Determina si un valor de string de conexión ODBC está entre comillas

## Descripción

```php
odbc_connection_string_is_quoted(string $str): bool
```php

Determina si un string está correctamente entre comillas para un string de conexión ODBC. La colocación entre comillas de strings de conexión ODBC se realiza utilizando llaves, y las llaves de cierre en un string deben ser escapadas repitiéndolas dos veces, similar a la colocación entre comillas SQL.

## Parámetros

`str`  
El string a verificar para la colocación entre comillas.

## Valores devueltos

`true` si el string está correctamente entre comillas, `false` en caso contrario.

## Véase también

`odbc_connection_string_quote`, `odbc_connection_string_should_quote`
