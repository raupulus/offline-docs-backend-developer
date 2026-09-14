---
title: mysqli::reap_async_query
description: Lee un resultado para una consulta asíncrona
source_url: https://www.php.net/manual/es/mysqli.reap-async-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/reap-async-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 63b99082e
order: 55300
---

mysqli::reap_async_query

mysqli_reap_async_query

Lee un resultado para una consulta asíncrona

## Descripción

Estilo orientado a objetos

```php
public mysqli::reap_async_query(): mysqli_result
```php

Estilo procedimental

```php
mysqli_reap_async_query(mysqli $mysql): mysqli_result
```

Lee el resultado para una consulta asíncrona.

> [!NOTE]
> Disponible solo con [mysqlnd](#book.mysqlnd).

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Devuelve `false` en caso de error. Para consultas exitosas que producen un conjunto de resultados como `SELECT, SHOW, DESCRIBE` o `EXPLAIN`, `mysqli_reap_async_query` devolverá un objeto `mysqli_result`. Para otros tipos de consultas exitosas, `mysqli_reap_async_query` devolverá `true`.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Véase también

`mysqli_poll`
