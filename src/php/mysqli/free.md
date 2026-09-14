---
title: mysqli_result::free
description: Libera la memoria asociada a un resultado
source_url: https://www.php.net/manual/es/mysqli-result.free.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/free.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55650
---

mysqli_result::free

mysqli_result::close

mysqli_result::free_result

mysqli_free_result

Libera la memoria asociada a un resultado

## Descripción

Estilo orientado a objetos

```php
public mysqli_result::free(): void
```php

```php
public mysqli_result::close(): void
```

```php
public mysqli_result::free_result(): void
```php

Estilo procedimental

```php
mysqli_free_result(mysqli_result $result): void
```

Libera la memoria asociada a un resultado.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

## Valores devueltos

No se retorna ningún valor.

## Véase también

`mysqli_query`, `mysqli_stmt_get_result`, `mysqli_store_result`, `mysqli_use_result`
