---
title: cubrid_drop
description: Borrar una instancia usando OID
source_url: https://www.php.net/manual/es/function.cubrid-drop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-drop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8980
---

cubrid_drop

Borrar una instancia usando OID

## Descripción

```php
cubrid_drop(resource $conn_identifier, string $oid): bool
```php

La función `cubrid_drop` se usa para borrar una instancia de la base de datos usando el `oid` de la instancia.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
Oid de la instancia que se quiere borrar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `cubrid_drop`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb");

@cubrid_execute($conn, "DROP TABLE foo");
cubrid_execute($conn, "CREATE TABLE foo(a int AUTO_INCREMENT, b set(int), c list(int), d char(10))");
cubrid_execute($conn, "INSERT INTO foo(a, b, c, d) VALUES(1, {1,2,3}, {11,22,33,333}, 'a')");
cubrid_execute($conn, "INSERT INTO foo(a, b, c, d) VALUES(2, {4,5,7}, {44,55,66,666}, 'b')");

$req = cubrid_execute($conn, "SELECT * FROM foo", CUBRID_INCLUDE_OID);

cubrid_move_cursor($req, 1, CUBRID_CURSOR_FIRST);
$oid = cubrid_current_oid($req);

printf("--- Antes de Drop: ---\n");
$attr = cubrid_get($conn, $oid);
var_dump($attr);

if (cubrid_drop($conn, $oid)) {
    cubrid_commit($conn);
} else {
    cubrid_rollback($conn);
}

cubrid_close_request($req);

$req = cubrid_execute($conn, "SELECT * FROM foo", CUBRID_INCLUDE_OID);

cubrid_move_cursor($req, 1, CUBRID_CURSOR_FIRST);
$oid = cubrid_current_oid($req);

printf("\n--- Después de Drop: ---\n");
$attr = cubrid_get($conn, $oid);
var_dump($attr);

cubrid_close_request($req);
cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    --- Antes de Drop: ---
    array(4) {
      ["a"]=>
      string(1) "1"
      ["b"]=>
      array(3) {
        [0]=>
        string(1) "1"
        [1]=>
        string(1) "2"
        [2]=>
        string(1) "3"
      }
      ["c"]=>
      array(4) {
        [0]=>
        string(2) "11"
        [1]=>
        string(2) "22"
        [2]=>
        string(2) "33"
        [3]=>
        string(3) "333"
      }
      ["d"]=>
      string(10) "a         "
    }

    --- Después de Drop: ---
    array(4) {
      ["a"]=>
      string(1) "2"
      ["b"]=>
      array(3) {
        [0]=>
        string(1) "4"
        [1]=>
        string(1) "5"
        [2]=>
        string(1) "7"
      }
      ["c"]=>
      array(4) {
        [0]=>
        string(2) "44"
        [1]=>
        string(2) "55"
        [2]=>
        string(2) "66"
        [3]=>
        string(3) "666"
      }
      ["d"]=>
      string(10) "b         "
    }

## Véase también

cubrid_is_instance
