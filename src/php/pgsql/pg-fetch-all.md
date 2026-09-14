---
title: pg_fetch_all
description: Lee todas las líneas de un resultado
source_url: https://www.php.net/manual/es/function.pg-fetch-all.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-fetch-all.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: cfeb14a38
order: 63080
---

pg_fetch_all

Lee todas las líneas de un resultado

## Descripción

```php
pg_fetch_all(PgSql\Result $result, [int $mode]): array
```php

`pg_fetch_all` devuelve un array que contiene todas las filas (registros) de la instancia de `PgSql\Result`.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`mode`  
Un parámetro opcional que controla cómo el `array` devuelto es indexado. `mode` es una constante que puede tomar los siguientes valores: `PGSQL_ASSOC`, `PGSQL_NUM` y `PGSQL_BOTH`. Usando `PGSQL_NUM`, la función devolverá un array con índices numéricos, usando `PGSQL_ASSOC`, devolverá solo índices asociativos mientras que `PGSQL_BOTH` devolverá ambos índices numéricos y asociativos.

## Valores devueltos

Un array `array` de todas las líneas en el conjunto de resultados. Cada línea es un array de valores de los campos indexado por el nombre de los campos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |
| 8.0.0 | `pg_fetch_all` devolverá ahora un `array` vacío en lugar de `false` para los conjuntos de resultados con cero líneas. |
| 7.1.0 | Se ha añadido el argumento `mode`. |

## Ejemplos

Ejemplo con `pg_fetch_all`

```
<?php
$conn = pg_pconnect("dbname=publisher");
if (!$conn) {
  echo "Se ha producido un error.\n";
  exit;
}

$result = pg_query($conn, "SELECT * FROM autores");
if (!$result) {
  echo "Se ha producido un error.\n";
  exit;
}

$arr = pg_fetch_all($result);

print_r($arr);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
            (
                [id] => 1
                [name] => Fred
            )

        [1] => Array
            (
                [id] => 2
                [name] => Bob
            )

    )

## Véase también

`pg_fetch_row`, `pg_fetch_array`, `pg_fetch_object`, `pg_fetch_result`
