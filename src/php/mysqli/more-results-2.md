---
title: mysqli_stmt::more_results
description: Comprueba si hay más resultados desde una consulta múltiple
source_url: https://www.php.net/manual/es/mysqli-stmt.more-results.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/more-results.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 035c126c0
order: 55900
---

mysqli_stmt::more_results

mysqli_stmt_more_results

Comprueba si hay más resultados desde una consulta múltiple

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::more_results(): bool
```php

Estilo procedimental:

```php
mysqli_stmt_more_results(mysql_stmt $statement): bool
```

Comprueba si hay más resultados desde una consulta múltiple.

> [!NOTE]
> Disponible solo con [mysqlnd](#book.mysqlnd).

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Devuelve `true` si hay más resultados, `false` en caso contrario.

## Véase también

mysqli_stmt::next_result, mysqli::multi_query
