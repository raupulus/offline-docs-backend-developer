---
title: pg_fetch_array
description: Lee una línea de resultado PostgreSQL en un array
source_url: https://www.php.net/manual/es/function.pg-fetch-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-fetch-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: cfeb14a38
order: 63090
---

pg_fetch_array

Lee una línea de resultado PostgreSQL en un array

## Descripción

```php
pg_fetch_array(PgSql\Result $result, [int $row], [int $mode]): array
```php

`pg_fetch_array` devuelve un array que contiene la línea solicitada.

`pg_fetch_array` es una versión mejorada de `pg_fetch_row`. Además de proporcionar un array con índice numérico, también puede almacenar los datos en un array asociativo, utilizando los nombres de los campos como claves. Estas dos funciones utilizan el array asociativo por omisión.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

`pg_fetch_array` no es significativamente más lenta que `pg_fetch_row` y aporta una comodidad de uso apreciable.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`row`  
Número de la línea a recuperar. Las líneas están numeradas comenzando por 0. Si el argumento es omitido o si vale `null`, se recupera la línea siguiente.

`mode`  
Un parámetro opcional que controla cómo el `array` devuelto es indexado. `mode` es una constante que puede tomar los siguientes valores: `PGSQL_ASSOC`, `PGSQL_NUM` y `PGSQL_BOTH`. Usando `PGSQL_NUM`, la función devolverá un array con índices numéricos, usando `PGSQL_ASSOC`, devolverá solo índices asociativos mientras que `PGSQL_BOTH` devolverá ambos índices numéricos y asociativos.

## Valores devueltos

Un `array` con índice numérico (comenzando por 0), asociativo (indexado con el nombre de los campos) o ambos. Cada valor en el `array` está representado como un `string`. Los valores `null` de la base de datos son devueltos como `null`.

`false` es devuelto si `row` excede el número de líneas en el conjunto de resultados, no hay más líneas disponibles o cualquier otro error. Intentar recuperar el resultado de una consulta que no sea SELECT también devolverá `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_fetch_array`

```
<?php

$conn = pg_pconnect ("dbname=publisher");
if (!$conn) {
  echo "Error de conexión.\n";
  exit;
}

$result = pg_query ($conn, "SELECT autor, email FROM autores");
if (!$result) {
  echo "Error durante la consulta.\n";
  exit;
}

$arr = pg_fetch_array ($result, 0, PGSQL_NUM);
echo $arr[0] . " <- Línea 1 Autor\n";
echo $arr[1] . " <- Línea 1 Correo electrónico\n";

// El parámetro row es opcional; NULL puede ser pasado en su lugar,
// para pasar un modo. Las llamadas sucesivas a pg_fetch_array
// devolverán la línea siguiente.
$arr = pg_fetch_array($result, NULL, PGSQL_ASSOC);
echo $arr["autor"] . " <- Línea 2 Autor\n";
echo $arr["email"] . " <- Línea 2 Correo electrónico\n";

$arr = pg_fetch_array($result);
echo $arr["autor"] . " <- Línea 3 Autor\n";
echo $arr[1] . " <- Línea 3 Correo electrónico\n";

?>

    
```php

## Véase también

`pg_fetch_row`, `pg_fetch_object`, `pg_fetch_result`
