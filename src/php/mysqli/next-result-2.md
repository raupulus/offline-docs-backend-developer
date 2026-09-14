---
title: mysqli_stmt::next_result
description: Lee el resultado siguiente desde una consulta múltiple
source_url: https://www.php.net/manual/es/mysqli-stmt.next-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/next-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 63b99082e
order: 55910
---

mysqli_stmt::next_result

mysqli_stmt_next_result

Lee el resultado siguiente desde una consulta múltiple

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::next_result(): bool
```php

Estilo procedimental:

```php
mysqli_stmt_next_result(mysql_stmt $statement): bool
```

Lee el resultado siguiente desde una consulta múltiple.

> [!NOTE]
> Anterior a PHP 8.1.0, disponible únicamente con [mysqlnd](#book.mysqlnd).

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Historial de cambios

| Versión | Descripción                                             |
|---------|---------------------------------------------------------|
| 8.1.0   | Ahora también disponible al enlazar con libmysqlclient. |

## Véase también

mysqli_stmt::more_results, mysqli::multi_query
