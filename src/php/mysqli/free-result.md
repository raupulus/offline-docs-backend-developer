---
title: mysqli_stmt::free_result
description: Libera el resultado MySQL de la memoria
source_url: https://www.php.net/manual/es/mysqli-stmt.free-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/free-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55860
---

mysqli_stmt::free_result

mysqli_stmt_free_result

Libera el resultado MySQL de la memoria

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::free_result(): void
```php

Estilo procedimental

```php
mysqli_stmt_free_result(mysqli_stmt $statement): void
```

Libera el resultado `stmt` de la memoria. `stmt` ha sido obtenido de la función `mysqli_stmt_store_result`.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

No se retorna ningún valor.

## Véase también

`mysqli_stmt_store_result`
