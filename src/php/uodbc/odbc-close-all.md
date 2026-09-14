---
title: odbc_close_all
description: Cierra todas las conexiones ODBC
source_url: https://www.php.net/manual/es/function.odbc-close-all.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-close-all.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: 96c9d88ba
order: 98650
---

odbc_close_all

Cierra todas las conexiones ODBC

## Descripción

```php
odbc_close_all(): void
```php

`odbc_close_all` cierra todas las conexiones ODBC a fuentes de datos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Notas

> [!NOTE]
> `odbc_close_all` fallará si hay transacciones en curso en esta conexión. En este caso, la conexión permanecerá abierta.
