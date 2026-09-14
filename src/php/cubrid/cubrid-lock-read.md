---
title: cubrid_lock_read
description: Coloca un bloqueo de lectura sobre el OID proporcionado
source_url: https://www.php.net/manual/es/function.cubrid-lock-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lock-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9330
---

cubrid_lock_read

Coloca un bloqueo de lectura sobre el OID proporcionado

## Descripción

```php
cubrid_lock_read(resource $conn_identifier, string $oid): bool
```php

La función `cubrid_lock_read` se utiliza para colocar un bloqueo de lectura sobre la instancia apuntada por el `oid` proporcionado.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
OID de la instancia cuya lectura se desea bloquear.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_lock_read`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb", "dba");

@cubrid_execute($conn, "DROP TABLE foo");
cubrid_execute($conn, "CREATE TABLE foo(a int AUTO_INCREMENT, b set(int), c list(int), d char(10))");
cubrid_execute($conn, "INSERT INTO foo(a, b, c, d) VALUES(1, {1,2,3}, {11,22,33,333}, 'a')");
cubrid_execute($conn, "INSERT INTO foo(a, b, c, d) VALUES(2, {4,5,7}, {44,55,66,666}, 'b')");

$req = cubrid_execute($conn, "SELECT * FROM foo", CUBRID_INCLUDE_OID);

cubrid_move_cursor($req, 1, CUBRID_CURSOR_FIRST);
$oid = cubrid_current_oid($req);

cubrid_lock_read($conn, $oid);

$attr = cubrid_get($conn, $oid, "b");
var_dump($attr);

$attr = cubrid_get($conn, $oid);
var_dump($attr);

cubrid_close_request($req);
cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    string(9) "{1, 2, 3}"
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

## Véase también

cubrid_lock_write
