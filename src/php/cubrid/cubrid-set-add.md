---
title: cubrid_set_add
description: Inserta un único elemento para definir el tipo de una columna
source_url: https://www.php.net/manual/es/function.cubrid-set-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-set-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9480
---

cubrid_set_add

Inserta un único elemento para definir el tipo de una columna

## Descripción

```php
cubrid_set_add(resource $conn_identifier, string $oid, string $attr_name, string $set_element): bool
```php

La función `cubrid_set_add` se utiliza para insertar un único elemento en un conjunto de tipos de atributos.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
OID de la instancia a utilizar.

`attr_name`  
Nombre del atributo en el cual el nuevo elemento será insertado.

`set_element`  
Contenido del elemento a insertar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_set_add`

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

cubrid_set_add($conn, $oid, "b", "4");

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
    array(4) {
      [0]=>
      string(1) "1"
      [1]=>
      string(1) "2"
      [2]=>
      string(1) "3"
      [3]=>
      string(1) "4"
    }

## Véase también

cubrid_seq_drop
