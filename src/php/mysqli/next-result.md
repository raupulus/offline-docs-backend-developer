---
title: mysqli::next_result
description: Prepara el siguiente resultado de una consulta múltiple
source_url: https://www.php.net/manual/es/mysqli.next-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/next-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 63b99082e
order: 55210
---

mysqli::next_result

mysqli_next_result

Prepara el siguiente resultado de una consulta múltiple

## Descripción

Estilo orientado a objetos

```php
public mysqli::next_result(): bool
```php

Estilo procedimental

```php
mysqli_next_result(mysqli $mysql): bool
```

Prepara el siguiente conjunto de resultados, inicializado por una llamada anterior a `mysqli_multi_query`, y que puede ser leído por `mysqli_store_result` o `mysqli_use_result`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Asimismo, devuelve `false` si la siguiente sentencia resulta en un error, a diferencia de mysqli_more_results.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Véase `mysqli_multi_query`.

## Véase también

`mysqli_multi_query`, `mysqli_more_results`, `mysqli_store_result`, `mysqli_use_result`
