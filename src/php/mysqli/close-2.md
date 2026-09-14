---
title: mysqli_stmt::close
description: Termina una consulta preparada
source_url: https://www.php.net/manual/es/mysqli-stmt.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: f78180344
order: 55770
---

mysqli_stmt::close

mysqli_stmt_close

Termina una consulta preparada

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::close(): true
```php

Estilo procedimental

```php
mysqli_stmt_close(mysqli_stmt $statement): true
```

Cierra una consulta preparada. `mysqli_stmt_close` libera el puntero utilizado por `stmt`. Si la consulta está pendiente o los resultados no han sido leídos aún, esta función los cancelará y, por lo tanto, la siguiente consulta podrá ser ejecutada.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ahora siempre devuelve `true`. Anteriormente, devolvía `false` en caso de fallo. |

## Véase también

`mysqli_prepare`
