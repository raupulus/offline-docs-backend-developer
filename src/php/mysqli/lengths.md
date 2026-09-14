---
title: mysqli_result::$lengths
description: Devuelve la longitud de las columnas de la fila actual del conjunto de
  resultados
source_url: https://www.php.net/manual/es/mysqli-result.lengths.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/lengths.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 473b5ab2c
order: 55670
---

mysqli_result::\$lengths

mysqli_fetch_lengths

Devuelve la longitud de las columnas de la fila actual del conjunto de resultados

## Descripción

Estilo orientado a objetos

array

null

mysqli_result-\>lengths

Estilo procedimental

```php
mysqli_fetch_lengths(mysqli_result $result): array
```php

La función `mysqli_fetch_lengths` devuelve un array que contiene la longitud de cada columna de la fila actual del conjunto de resultados representado por el argumento `result`.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

## Valores devueltos

Un array de integers que representan el tamaño de cada columna (sin incluir ningún carácter null de final). Devuelve `false` si ocurre un error.

`mysqli_fetch_lengths` solo es válido para la fila actual del conjunto de resultados. Devuelve `false` si se llama antes de las funciones `mysqli_fetch_row`, `mysqli_fetch_array`, `mysqli_fetch_object` o después de haber recuperado todas las filas del resultado.

## Ejemplos

Estilo orientado a objetos

```
<?php
$mysqli = new mysqli("localhost", "mon_user", "mon_mot_de_passe", "la_base");

/* Verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$query = "SELECT * from Country ORDER BY Code LIMIT 1";

if ($result = $mysqli->query($query)) {

    $row = $result->fetch_row();

    /* Visualización de la longitud de las columnas */
    foreach ($result->lengths as $i => $val) {
        printf("El campo n°%2d tiene una longitud de %2d\n", $i+1, $val);
    }
    $result->close();
}

/* Cierra la conexión */
$mysqli->close();
?>

   
```php

Estilo procedimental

```
<?php
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$query = "SELECT * from Country ORDER BY Code LIMIT 1";

if ($result = mysqli_query($link, $query)) {

    $row = mysqli_fetch_row($result);

    /* Visualización de la longitud de las columnas */
    foreach (mysqli_fetch_lengths($result) as $i => $val) {
        printf("El campo n°%2d tiene una longitud de %2d\n", $i+1, $val);
    }
    mysqli_free_result($result);
}

/* Cierra la conexión */
mysqli_close($link);
?>

   
```php

Los ejemplos anteriores mostrarán:

    El campo n° 1 tiene una longitud de  3
    El campo n° 2 tiene una longitud de  5
    El campo n° 3 tiene una longitud de 13
    El campo n° 4 tiene una longitud de  9
    El campo n° 5 tiene una longitud de  6
    El campo n° 6 tiene una longitud de  1
    El campo n° 7 tiene una longitud de  6
    El campo n° 8 tiene una longitud de  4
    El campo n° 9 tiene una longitud de  6
    El campo n°10 tiene una longitud de  6
    El campo n°11 tiene una longitud de  5
    El campo n°12 tiene una longitud de 44
    El campo n°13 tiene una longitud de  7
    El campo n°14 tiene una longitud de  3
    El campo n°15 tiene una longitud de  2
