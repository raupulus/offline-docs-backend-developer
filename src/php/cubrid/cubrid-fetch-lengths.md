---
title: cubrid_fetch_lengths
description: Devuelve una matriz con las longitudes de los valores de cada campo de
  la fila actual
source_url: https://www.php.net/manual/es/function.cubrid-fetch-lengths.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-fetch-lengths.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8690
---

cubrid_fetch_lengths

Devuelve una matriz con las longitudes de los valores de cada campo de la fila actual

## Descripción

```php
cubrid_fetch_lengths(resource $result): array
```php

Esta función devuelve una matriz numérica con las longitudes de los valores de cada campo de la fila actual del conjunto de resultados o FALSE en caso de fallo.

> [!NOTE]
> Si el tipo de información del campo es BLOB/CLOB, se debería tomar su longitud usando `cubrid_lob_size`.

## Parámetros

`result`  
`result` proviene de una llamada a la función `cubrid_execute`

## Valores devueltos

Una matriz numérica, cuando el proceso tuvo éxito.

`false` en caso de error.

## Ejemplos

Ejemplo de `cubrid_fetch_lengths`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");
$result = cubrid_execute($conn, "SELECT * FROM game WHERE host_year=2004 AND nation_code='AUS' AND medal='G'");

$row = cubrid_fetch_row($result);
print_r($row);

$lens = cubrid_fetch_lengths($result);
print_r($lens);

cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => 2004
        [1] => 20085
        [2] => 15118
        [3] => 30134
        [4] => AUS
        [5] => G
        [6] => 2004-8-20
    )
    Array
    (
        [0] => 4
        [1] => 5
        [2] => 5
        [3] => 5
        [4] => 3
        [5] => 1
        [6] => 10
    )
