---
title: cubrid_get
description: Obtener una columna usando OID
source_url: https://www.php.net/manual/es/function.cubrid-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 9120
---

cubrid_get

Obtener una columna usando OID

## Descripción

```php
cubrid_get(resource $conn_identifier, string $oid, [mixed $attr]): mixed
```php

La función `cubrid_get` se usa para obtener el atributo de la instancia del `oid` dado. Se puede obtener un solo atributo usando el tipo de datos de cadena para el argumento `attr`, o muchos atributos usando el tipo de datos array para el argumento `attr`.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
OID de la instancia que se quiere leer.

`attr`  
Nombre del atributo que se quiere leer.

## Valores devueltos

Contenido del atributo solicitado, cuando el proceso tiene éxito; Cuando `attr` se establece al tipo de datos de cadena, el resultado es devuelto como una cadena; cuando `attr` se establece como tipo de datos array (númerico basado en 0), el resultado es devuelto como un array asociativo. Cuanso se omite `attr`, entonces todos los atributos se reciben como array.

`false` cuando el proceso no tiene éxito o el resultado es NULL (Si ocurre un error para diferenciar una cadena vacía de NULL, se imprime un mensaje de advertencia. Se puede comprobar el error usando `cubrid_error_code`)

## Ejemplos

Ejemplo de `cubrid_get`

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

cubrid_put
