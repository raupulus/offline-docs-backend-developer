---
title: pg_result_seek
description: Establece la posición de la línea en un resultado
source_url: https://www.php.net/manual/es/function.pg-result-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-result-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63620
---

pg_result_seek

Establece la posición de la línea en un resultado

## Descripción

```php
pg_result_seek(PgSql\Result $result, int $row): bool
```php

`pg_result_seek` selecciona la línea `offset` como línea actual en el resultado `result`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`row`  
Línea a la que se moverá la posición interna en la instancia de `PgSql\Result`. Las líneas están numeradas a partir de cero.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_result_seek`

```
<?php

// Conexión a la base de datos
$conn = pg_pconnect("dbname=publisher");

// Ejecución de la consulta
$result = pg_query($conn, "SELECT autor, email FROM autores");

// Desplazamiento a la tercera línea (se asume que hay 3 líneas)
pg_result_seek($result, 2);

// Obtención de la tercera línea
$row = pg_fetch_row($result);

?>

    
```php

## Véase también

`pg_fetch_row`, `pg_fetch_assoc`, `pg_fetch_array`, `pg_fetch_object`, `pg_fetch_result`
