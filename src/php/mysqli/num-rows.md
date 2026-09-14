---
title: mysqli_result::$num_rows
description: Devuelve el número de filas en el conjunto de resultados
source_url: https://www.php.net/manual/es/mysqli-result.num-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/num-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 181e9c557
order: 55680
---

mysqli_result::\$num_rows

mysqli_num_rows

Devuelve el número de filas en el conjunto de resultados

## Descripción

Estilo orientado a objetos

int

string

mysqli_result-\>num_rows

Estilo procedimental

```php
mysqli_num_rows(mysqli_result $result): int
```php

Devuelve el número de filas en un conjunto de resultados.

El comportamiento de `mysqli_num_rows` depende del uso de conjuntos de resultados almacenados en búfer o no. Esta función devuelve `0` para conjuntos de resultados no almacenados en búfer, a menos que todas las filas hayan sido recuperadas del servidor.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

## Valores devueltos

Un `int` que representa el número de filas recuperadas. Devuelve `0` en modo no almacenado en búfer, a menos que todas las filas hayan sido recuperadas desde el servidor.

> [!NOTE]
> Si el número de filas es mayor que `PHP_INT_MAX`, el número será devuelto como un `string`.

## Ejemplos

Estilo orientado a objetos

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$result = $mysqli->query("SELECT Code, Name FROM Country ORDER BY Name");

/* Determina el número de filas del conjunto de resultados */
$row_cnt = $result->num_rows;

printf("El conjunto de resultados tiene %d filas.\n", $row_cnt);

   
```php

Estilo procedimental

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

$result = mysqli_query($link, "SELECT Code, Name FROM Country ORDER BY Name");

/* Determina el número de filas del conjunto de resultados */
$row_cnt = mysqli_num_rows($result);

printf("El conjunto de resultados tiene %d filas.\n", $row_cnt);
?>

   
```php

Los ejemplos anteriores mostrarán:

    El conjunto de resultados tiene 239 filas.

## Notas

> [!NOTE]
> A diferencia de la función `mysqli_stmt_num_rows`, esta función no tiene una variante de método orientado a objetos. En el estilo orientado a objetos, se debe utilizar el getter de la propiedad.

## Véase también

`mysqli_affected_rows`, `mysqli_store_result`, `mysqli_use_result`, `mysqli_query`, `mysqli_stmt_num_rows`
