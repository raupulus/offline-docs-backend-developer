---
title: cubrid_data_seek
description: Mueve el puntero interno de la fila del resultado CUBRID
source_url: https://www.php.net/manual/es/function.cubrid-data-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-data-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8620
---

cubrid_data_seek

Mueve el puntero interno de la fila del resultado CUBRID

## Descripción

```php
cubrid_data_seek(resource $result, int $row_number): bool
```php

Esta función desplaza el puntero interno de las filas del resultado CUBRID (asociado con el identificador especificado) para apuntar al número de fila especificada. Hay funciones, como `cubrid_fetch_assoc`, que utiliza el valor actualmente almacenado del número de fila.

## Parámetros

`result`  
El resultado.

`row_number`  
Éste es el número de fila deseado del puntero del nuevo resultado.

## Valores devueltos

Devuelve `true` en caso de éxito o `false` en caso de error.

## Ejemplos

Ejemplo de `cubrid_data_seek`

```
<?php
$conn = cubrid_connect("127.0.0.1", 33000, "demodb");

$req = cubrid_execute($conn, "SELECT * FROM code");
cubrid_data_seek($req, 0);

$result = cubrid_fetch_row($req);
var_dump($result);

cubrid_data_seek($req, 2);
$result = cubrid_fetch_row($req);
var_dump($result);

cubrid_data_seek($req, 4);
$result = cubrid_fetch_row($req);
var_dump($result);

cubrid_close_request($req);
cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    array(2) {
      [0]=>
      string(1) "X"
      [1]=>
      string(5) "Mixed"
    }
    array(2) {
      [0]=>
      string(1) "M"
      [1]=>
      string(3) "Man"
    }
    array(2) {
      [0]=>
      string(1) "S"
      [1]=>
      string(6) "Silver"
    }
