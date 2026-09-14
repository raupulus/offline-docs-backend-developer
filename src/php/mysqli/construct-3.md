---
title: mysqli_stmt::__construct
description: Construye un nuevo objeto mysqli_stmt
source_url: https://www.php.net/manual/es/mysqli-stmt.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 63b99082e
order: 55780
---

mysqli_stmt::\_\_construct

Construye un nuevo objeto

mysqli_stmt

## Descripción

```php
public mysqli_stmt::__construct(mysqli $mysql, [string $query])
```php

Este método construye un nuevo objeto `mysqli_stmt`.

## Parámetros

`link`  
Un objeto `mysqli` válido.

`query`  
La consulta, en forma de string. Si este argumento es `null`, entonces el constructor se comportará como la función `mysqli_stmt_init`; de lo contrario, se comportará como la función `mysqli_prepare`.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Historial de cambios

| Versión | Descripción                |
|---------|----------------------------|
| 8.0.0   | `query` ahora es nullable. |

## Véase también

`mysqli_prepare`, `mysqli_stmt_init`
