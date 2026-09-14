---
title: odbc_free_result
description: Libera los objetos asociados a un resultado
source_url: https://www.php.net/manual/es/function.odbc-free-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-free-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: ed1aff136
order: 98920
---

odbc_free_result

Libera los objetos asociados a un resultado

## Descripción

```php
odbc_free_result(Odbc\Result $statement): true
```php

Libera los objetos asociados a un resultado.

`odbc_free_result` solo es necesario si se teme utilizar demasiada memoria durante la ejecución del script. Todos los resultados en memoria se liberarán al final del script.

## Parámetros

`statement`  
The ODBC result object.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `statement` ahora espera una instancia de `Odbc\Result` ; anteriormente, se esperaba un `resource`. |

## Notas

> [!NOTE]
> Si la autovalidación está desactivada (ver `odbc_autocommit`) y se llama a `odbc_free_result` antes de validar las consultas, todas las transacciones preparadas se cancelarán.
