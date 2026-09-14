---
title: mysqli_stmt::reset
description: Anula una consulta preparada
source_url: https://www.php.net/manual/es/mysqli-stmt.reset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/reset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55950
---

mysqli_stmt::reset

mysqli_stmt_reset

Anula una consulta preparada

## Descripción

Estilo orientado a objetos

```php
public mysqli_stmt::reset(): bool
```php

Estilo procedimental

```php
mysqli_stmt_reset(mysqli_stmt $statement): bool
```

Anula una consulta preparada en el cliente y en el servidor después de haber sido preparada.

Esta función anula la consulta en el servidor, anula los datos enviados utilizando la función `mysqli_stmt_send_long_data`, anula los conjuntos de resultados no almacenados en buffer, así como los errores actuales. Sin embargo, los conjuntos de resultados almacenados o vinculados no se anulan. Los conjuntos de resultados almacenados se borran al ejecutar la consulta preparada (o al cerrarlos).

Para preparar nuevamente una consulta, se debe utilizar la función `mysqli_stmt_prepare`.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`mysqli_prepare`
