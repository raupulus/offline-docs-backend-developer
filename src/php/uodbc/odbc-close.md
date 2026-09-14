---
title: odbc_close
description: Cierra una conexión ODBC
source_url: https://www.php.net/manual/es/function.odbc-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98660
---

odbc_close

Cierra una conexión ODBC

## Descripción

```php
odbc_close(Odbc\Connection $odbc): void
```php

Cierra la conexión con la base de datos del servidor.

## Parámetros

`odbc`  
El objeto de conexión ODBC, ver la documentación de la función `odbc_connect` para más detalles.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `odbc` ahora espera una instancia de `Odbc\Connection` ; anteriormente, se esperaba un `resource`. |

## Notas

> [!NOTE]
> `odbc_close` fallará si hay transacciones en curso en esta conexión. En este caso, la conexión permanecerá abierta.
