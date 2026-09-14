---
title: odbc_commit
description: Valida una transacción ODBC
source_url: https://www.php.net/manual/es/function.odbc-commit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-commit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98690
---

odbc_commit

Valida una transacción ODBC

## Descripción

```php
odbc_commit(Odbc\Connection $odbc): bool
```php

Valida todas las transacciones en curso en la conexión.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |
