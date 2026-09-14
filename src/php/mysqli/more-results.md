---
title: mysqli::more_results
description: Comprueba si hay más conjuntos de resultados MySQL disponibles
source_url: https://www.php.net/manual/es/mysqli.more-results.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/more-results.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55190
---

mysqli::more_results

mysqli_more_results

Comprueba si hay más conjuntos de resultados MySQL disponibles

## Descripción

Estilo orientado a objetos

```php
public mysqli::more_results(): bool
```php

Estilo procedimental

```php
mysqli_more_results(mysqli $mysql): bool
```

Indica si uno o más conjuntos de resultados están disponibles, generados por una llamada anterior a `mysqli_multi_query`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Devuelve `true` si uno o más conjuntos de resultados (incluyendo errores) están disponibles a partir de una llamada previa a la función `mysqli_multi_query`, `false` en caso contrario.

## Ejemplos

Ver `mysqli_multi_query`.

## Véase también

`mysqli_multi_query`, `mysqli_next_result`, `mysqli_store_result`, `mysqli_use_result`
