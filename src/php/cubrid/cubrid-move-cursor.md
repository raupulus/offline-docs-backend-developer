---
title: cubrid_move_cursor
description: Desplaza el cursor en el resultado
source_url: https://www.php.net/manual/es/function.cubrid-move-cursor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-move-cursor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9350
---

cubrid_move_cursor

Desplaza el cursor en el resultado

## Descripción

```php
cubrid_move_cursor(resource $req_identifier, int $offset, [int $origin]): bool
```php

La función `cubrid_move_cursor` se utiliza para desplazar el cursor actual según el parámetro `req_identifier` con el valor del parámetro `offset` y en la dirección definida por el parámetro `origin` argumento. Para definir el argumento `origin`, se puede utilizar `CUBRID_CURSOR_FIRST` para la primera parte del resultado, `CUBRID_CURSOR_CURRENT` para la posición actual del resultado, o `CUBRID_CURSOR_LAST` para la última parte del resultado. Si el argumento `origin` no es explícitamente designado, entonces la función utilizará `CUBRID_CURSOR_CURRENT` como valor por omisión.

Si el valor actual del desplazamiento del cursor está más allá de los límites válidos, entonces el cursor se desplaza a la siguiente posición después del intervalo válido del cursor. Por ejemplo, si se desplaza 20 unidades en el resultado cuyo tamaño es de 10, entonces el cursor se colocará en la 11ª posición y devolverá `CUBRID_NO_MORE_DATA`.

## Parámetros

`req_identifier`  
Identificador de la consulta.

`offset`  
Número de unidades que se desean utilizar para el desplazamiento.

`origin`  
Objetivo donde se desea desplazar el cursor, ya sea `CUBRID_CURSOR_FIRST`, `CUBRID_CURSOR_CURRENT`, `CUBRID_CURSOR_LAST`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_move_cursor`

```
<?php
$conn = cubrid_connect("127.0.0.1", 33000, "demodb", "dba");

$req = cubrid_execute($conn, "SELECT * FROM code");
cubrid_move_cursor($req, 1, CUBRID_CURSOR_LAST);

$result = cubrid_fetch_row($req);
var_dump($result);

cubrid_move_cursor($req, 1, CUBRID_CURSOR_FIRST);
$result = cubrid_fetch_row($req);
var_dump($result);

cubrid_move_cursor($req, 1, CUBRID_CURSOR_CURRENT);
$result = cubrid_fetch_row($req);
var_dump($result);

cubrid_close_request($req);
cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    array(2) {
      [0]=>
      string(1) "G"
      [1]=>
      string(4) "Gold"
    }
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

## Véase también

cubrid_execute
