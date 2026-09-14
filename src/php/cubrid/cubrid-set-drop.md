---
title: cubrid_set_drop
description: Elimina un elemento
source_url: https://www.php.net/manual/es/function.cubrid-set-drop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-set-drop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9510
---

cubrid_set_drop

Elimina un elemento

## Descripción

```php
cubrid_set_drop(resource $conn_identifier, string $oid, string $attr_name, string $set_element): bool
```php

La función `cubrid_set_drop` se utiliza para eliminar un elemento de un atributo dado de la base de datos.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
OID de la instancia a utilizar.

`attr_name`  
Nombre del atributo desde el cual se eliminará el elemento.

`set_element`  
Contenido del elemento a eliminar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_set_drop`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb", "dba");

@cubrid_execute($conn, "DROP TABLE foo");
cubrid_execute($conn, "CREATE TABLE foo(a int AUTO_INCREMENT, b set(int), c list(int), d char(10))");
cubrid_execute($conn, "INSERT INTO foo(a, b, c, d) VALUES(1, {1,2,3}, {11,22,33,333}, 'a')");

$req = cubrid_execute($conn, "SELECT * FROM foo", CUBRID_INCLUDE_OID);

cubrid_move_cursor($req, 1, CUBRID_CURSOR_FIRST);
$oid = cubrid_current_oid($req);

$attr = cubrid_col_get($conn, $oid, "b");
var_dump($attr);

cubrid_set_drop($conn, $oid, "b", "1");

$attr = cubrid_col_get($conn, $oid, "b");
var_dump($attr);

cubrid_close_request($req);
cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

    array(3) {
      [0]=>
      string(1) "1"
      [1]=>
      string(1) "2"
      [2]=>
      string(1) "3"
    }
    array(2) {
      [0]=>
      string(1) "2"
      [1]=>
      string(1) "3"
    }

## Véase también

cubrid_set_add
