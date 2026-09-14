---
title: mysqli::real_query
description: Ejecuta una consulta SQL
source_url: https://www.php.net/manual/es/mysqli.real-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/real-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: d470f625f
order: 55290
---

mysqli::real_query

mysqli_real_query

Ejecuta una consulta SQL

## Descripción

Estilo orientado a objetos

```php
public mysqli::real_query(string $query): bool
```php

Estilo procedimental

```php
mysqli_real_query(mysqli $mysql, string $query): bool
```

Ejecuta una sola consulta en la conexión a la base de datos representada por el parámetro `link` cuyo resultado puede ser recuperado o almacenado utilizando las funciones `mysqli_store_result` o `mysqli_use_result`.

> [!WARNING]
> Si la consulta contiene alguna entrada de variable, entonces se deben usar [sentencias preparadas parametrizadas](#mysqli.quickstart.prepared-statements) en su lugar. Alternativamente, los datos deben estar correctamente formateados y todas las cadenas deben ser escapadas usando la función `mysqli_real_escape_string` .

Para determinar si una consulta dada debería haber devuelto un conjunto de resultados o no, consulte la función `mysqli_field_count`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`query`  
La consulta `string`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Véase también

`mysqli_query`, `mysqli_store_result`, `mysqli_use_result`
