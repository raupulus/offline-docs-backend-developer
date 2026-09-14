---
title: cubrid_seq_insert
description: Inserta un elemento en una secuencia
source_url: https://www.php.net/manual/es/function.cubrid-seq-insert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-seq-insert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 184764a63
order: 9460
---

cubrid_seq_insert

Inserta un elemento en una secuencia

## Descripción

```php
cubrid_seq_insert(resource $conn_identifier, string $oid, string $attr_name, int $index, string $seq_element): bool
```php

La función `cubrid_seq_insert` se utiliza para insertar un elemento en una secuencia de tipos de atributos.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
OID de la instancia a utilizar.

`attr_name`  
Nombre del atributo a insertar.

`index`  
Posición del elemento para su inserción (comenzando en 1).

`seq_element`  
Contenido del elemento a insertar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_seq_insert`

```
<?php
$conn = cubrid_connect("localhost", 33000, "demodb", "dba");

@cubrid_execute($conn, "DROP TABLE foo");
cubrid_execute($conn, "CREATE TABLE foo(a int AUTO_INCREMENT, b set(int), c sequence(int), d char(10))");
cubrid_execute($conn, "INSERT INTO foo(a, b, c, d) VALUES(1, {1,2,3}, {11,22,33,333}, 'a')");

$req = cubrid_execute($conn, "SELECT * FROM foo", CUBRID_INCLUDE_OID);

cubrid_move_cursor($req, 1, CUBRID_CURSOR_FIRST);
$oid = cubrid_current_oid($req);

$attr = cubrid_col_get($conn, $oid, "c");
var_dump($attr);

cubrid_seq_insert($conn, $oid, "c", 5, "44");

$attr = cubrid_col_get($conn, $oid, "c");
var_dump($attr);

cubrid_close_request($req);
cubrid_disconnect($conn);
?>

   
```php

El ejemplo anterior mostrará:

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
    array(5) {
      [0]=>
      string(2) "11"
      [1]=>
      string(2) "22"
      [2]=>
      string(2) "33"
      [3]=>
      string(3) "333"
      [4]=>
      string(2) "44"
    }

## Véase también

cubrid_seq_drop

cubrid_seq_put
