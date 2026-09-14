---
title: mysqli_result::__construct
description: Construye un objeto mysqli_result
source_url: https://www.php.net/manual/es/mysqli-result.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 63b99082e
order: 55510
---

mysqli_result::\_\_construct

Construye un objeto

mysqli_result

## Descripción

```php
public mysqli_result::__construct(mysqli $mysql, [int $result_mode])
```php

Este método construye un nuevo objeto `mysqli_result`.

Esto puede ser utilizado para crear el objeto `mysqli_result` después de haber llamado a las funciones `mysqli_real_query` o `mysqli_multi_query`. Construir el objeto manualmente es equivalente a llamar a las funciones `mysqli_store_result` o `mysqli_use_result`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`result_mode`  
El modo de resultado puede ser una de las 2 constantes que indican cómo el resultado será devuelto por el servidor MySQL.

`MYSQLI_STORE_RESULT` (por omisión) - crea un objeto `mysqli_result` con un juego de resultados almacenado en búfer.

`MYSQLI_USE_RESULT` - crea un objeto `mysqli_result` con un juego de resultados no almacenado en búfer. Mientras queden registros pendientes de ser recuperados, la línea de conexión estará ocupada y todas las llamadas siguientes devolverán el error `Commands out of sync`. Para evitar el error, todos los registros deben ser recuperados del servidor o el juego de resultados debe ser descartado llamando a `mysqli_free_result`. La conexión debe permanecer abierta para que las líneas sean recuperadas.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Creación de un objeto `mysqli_result`

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Consulta SELECT que devuelve un juego de resultados */
$mysqli->real_query("SELECT Name FROM City LIMIT 10");

$result = new mysqli_result($mysqli);
printf("Select devolvió %d filas.\n", $result->num_rows);

   
```php

Los ejemplos anteriores mostrarán algo similar a:

    Select devolvió 10 filas.

## Véase también

`mysqli_multi_query`, `mysqli_real_query`, `mysqli_store_result`, `mysqli_use_result`
