---
title: pg_field_is_null
description: Comprueba si un campo PostgreSQL es null
source_url: https://www.php.net/manual/es/function.pg-field-is-null.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-field-is-null.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_revision: 39bb8a868
order: 63140
---

pg_field_is_null

Comprueba si un campo PostgreSQL es

null

## Descripción

```php
pg_field_is_null(PgSql\Result $result, string $row, mixed $field): int
```php

```php
pg_field_is_null(PgSql\Result $result, mixed $field): int
```

`pg_field_is_null` comprueba si un campo en una instancia `PgSql\Result` es un `NULL` SQL o no.

> [!NOTE]
> Anteriormente, esta función se llamaba `pg_fieldisnull`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`row`  
Número de la fila a recuperar. Las filas están numeradas a partir de 0. Si el argumento es omitido, se recupera la fila siguiente.

`field`  
Número del campo (comenzando en 0) de tipo `int` o el nombre del campo de tipo `string`.

## Valores devueltos

Retorna `1` si el campo de la fila dada es `null`, `0` si no es `null`. `false` es retornado si la fila no está en el array o cualquier otro error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | `row` es ahora nullable. |
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_field_is_null`

```php
<?php
    $dbconn = pg_connect("dbname=publisher") or die ("Conexión imposible");
    $res = pg_query($dbconn, "select * from autores where autor = 'Orwell'");
    if ($res) {
        if (pg_field_is_null($res, 0, "año") == 1) {
            echo "El valor del campo \"año\" es null.\n";
        }
        if (pg_field_is_null($res, 0, "año") == 0) {
            echo "El valor del campo \"año\" no es null.\n";
        }
    }
?>

    
```
