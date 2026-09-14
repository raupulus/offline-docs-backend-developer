---
title: pg_fetch_row
description: Lee una fila en un array
source_url: https://www.php.net/manual/es/function.pg-fetch-row.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-fetch-row.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: cfeb14a38
order: 63130
---

pg_fetch_row

Lee una fila en un array

## Descripción

```php
pg_fetch_row(PgSql\Result $result, [int $row], [int $mode]): array
```php

`pg_fetch_row` lee una fila en el resultado asociado a la instancia `result`.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`row`  
Número de la fila a recuperar. Las filas están numeradas comenzando en 0. Si el argumento es omitido o si vale `null`, la siguiente fila es recuperada.

`mode`  
Un parámetro opcional que controla cómo el `array` devuelto es indexado. `mode` es una constante que puede tomar los siguientes valores: `PGSQL_ASSOC`, `PGSQL_NUM` y `PGSQL_BOTH`. Usando `PGSQL_NUM`, la función devolverá un array con índices numéricos, usando `PGSQL_ASSOC`, devolverá solo índices asociativos mientras que `PGSQL_BOTH` devolverá ambos índices numéricos y asociativos.

## Valores devueltos

Un `array`, indexado desde 0, con cada valor representado como un `string`. Los valores `null` de la base de datos son retornados como `null`.

`false` es retornado si `row` excede el número de filas en el conjunto de resultados, no tiene más filas disponibles o cualquier otro error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_fetch_row`

```
<?php

$conn = pg_pconnect("dbname=publisher");
if (!$conn) {
  echo "Ha ocurrido un error.\n";
  exit;
}

$result = pg_query($conn, "SELECT autor, email FROM autores");
if (!$result) {
  echo "Ha ocurrido un error.\n";
  exit;
}

while ($row = pg_fetch_row($result)) {
  echo "Autor: $row[0]  E-mail: $row[1]";
  echo "<br />\n";
}

?>

    
```php

## Véase también

`pg_query`, `pg_fetch_array`, `pg_fetch_object`, `pg_fetch_result`
