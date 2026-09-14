---
title: pg_set_chunked_rows_size
description: Establece los resultados de la consulta a recuperar en modo chunk
source_url: https://www.php.net/manual/es/function.pg-set-chunked-rows-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/functions/pg-set-chunked-rows-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_reviewed: true
translation_revision: 3c6c95fcf
order: 63690
---

pg_set_chunked_rows_size

Establece los resultados de la consulta a recuperar en modo chunk

## Descripción

```php
pg_set_chunked_rows_size(PgSql\Connection $connection, int $size): bool
```php

Establece los resultados de la consulta a recuperar en modo chunk. La consulta devuelta posteriormente se dividirá en varios fragmentos, cada uno conteniendo hasta `size` filas. Esta función debe ser llamada antes de recuperar los resultados con `pg_get_result`. Esta función solo está disponible cuando libpq está en versión 17 o superior.

## Parámetros

`connection`  
Una instancia `PgSql\Connection`.

`size`  
El número de filas a recuperar en cada fragmento.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si `size` es inferior a `1`, se lanzará un `ValueError`.

## Ejemplos

Ejemplo de `pg_result_memory_size`

```
<?php

$conn = pg_connect($conn_str);

for ($i = 0; $i < 10; $i ++) {
  pg_query($conn, "INSERT INTO users DEFAULT VALUES");
}

pg_send_query($conn, "SELECT * FROM users");
pg_set_chunked_rows_size($conn, 1);

$result = pg_get_result($conn);
var_dump(pg_num_rows($result));

:: Sin efecto después de que el resultado sea recuperado
var_dump(pg_set_chunked_rows_size($conn, 10));

   
```php

El ejemplo anterior mostrará:

    int(1)
    bool(false)

## Véase también

pg_get_result

pg_result_status
