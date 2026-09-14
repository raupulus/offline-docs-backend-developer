---
title: pg_fetch_assoc
description: Lee una fila de resultado PostgreSQL como un array asociativo
source_url: https://www.php.net/manual/es/function.pg-fetch-assoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-fetch-assoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: false
translation_revision: c2eca73ef
order: 63100
---

pg_fetch_assoc

Lee una fila de resultado PostgreSQL como un array asociativo

## Descripción

```php
pg_fetch_assoc(PgSql\Result $result, [int $row]): array
```php

`pg_fetch_assoc` devuelve un array asociativo que contiene la fila actual en el resultado `result`.

`pg_fetch_assoc` es equivalente a llamar `pg_fetch_row` con `PGSQL_ASSOC` como tercer argumento (que es opcional). Esto devolverá solo un array asociativo. Si se necesitan índices numéricos, se debe utilizar `pg_fetch_row`.

> [!NOTE]
> Esta función define los campos NULL al valor PHP `null`.

`pg_fetch_assoc` no es significativamente más lenta que `pg_fetch_row` y aporta una comodidad de uso apreciable.

## Parámetros

`result`  
Una instancia `PgSql\Result`, devuelta por `pg_query`, `pg_query_params`, o `pg_execute` (entre otros).

`row`  
Número de la fila a recuperar. Las filas están numeradas comenzando desde 0. Si el argumento es omitido o si es `null`, la siguiente fila es recuperada.

## Valores devueltos

Un `array` con índice asociativo (por nombre de campo). Cada valor en el `array` es representado como un `string`. Los valores `null` de la base de datos son devueltos `null`.

`false` es devuelto si `row` excede el número de filas en el conjunto de resultados, no hay más filas disponibles o cualquier otro error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `result` ahora espera una instancia de `PgSql\Result` ; anteriormente, se esperaba un `resource`. |

## Ejemplos

Ejemplo con `pg_fetch_assoc`

```
<?php
$conn = pg_pconnect ("dbname=publisher");
if (!$conn) {
  echo "Ha ocurrido un error.\n";
  exit;
}

$result = pg_query ($conn, "SELECT id, autor, email FROM autores");
if (!$result) {
  echo "Ha ocurrido un error.\n";
  exit;
}

while ($row = pg_fetch_assoc($result)) {
  echo $row['id'];
  echo $row['autor'];
  echo $row['email'];
}
?>

    
```php

## Véase también

`pg_fetch_row`, `pg_fetch_array`, `pg_fetch_object`, `pg_fetch_result`
