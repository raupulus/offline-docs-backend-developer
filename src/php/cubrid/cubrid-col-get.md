---
title: cubrid_col_get
description: Recupera el contenido de los elementos de un tipo de colección utilizando
  el OID
source_url: https://www.php.net/manual/es/function.cubrid-col-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-col-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8890
---

cubrid_col_get

Recupera el contenido de los elementos de un tipo de colección utilizando el OID

## Descripción

```php
cubrid_col_get(resource $conn_identifier, string $oid, string $attr_name): array
```php

La función `cubrid_col_get` se utiliza para recuperar el contenido de los atributos de los elementos de un tipo de colección (set, multiset, sequence), en forma de un `array`.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
OID de la instancia a utilizar para la lectura.

`attr_name`  
Nombre del atributo que se desea leer desde la instancia.

## Valores devueltos

Un `array` (numérico, comenzando en 0) que contiene los elementos deseados cuando la operación se ha realizado con éxito.

`false` (para distinguir los errores y el hecho de que los atributos tienen una colección vacía o nula; en caso de error, se mostrará un mensaje de alerta; en este caso, se puede recuperar el error utilizando la función `cubrid_error_code`), cuando la operación ha fallado.

## Ejemplos

Ejemplo con `cubrid_col_get`

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

$size = cubrid_col_size($conn, $oid, "b");
var_dump($size);

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
    int(3)
