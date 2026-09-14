---
title: cubrid_col_size
description: Obtener el número de elementos de la columna del tipo de colección usando
  OID
source_url: https://www.php.net/manual/es/function.cubrid-col-size.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-col-size.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 8900
---

cubrid_col_size

Obtener el número de elementos de la columna del tipo de colección usando OID

## Descripción

```php
cubrid_col_size(resource $conn_identifier, string $oid, string $attr_name): int
```php

La función `cubrid_col_size` se usa para obtener el número de elementos de un atributo de tipo de colección (conjunto, multiconjunto, secuencia).

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
El OID de la instancia con la que se quiere trabajar.

`attr_name`  
Nombre del atributo con el que se quiere trabajar.

## Valores devueltos

Número de elementos, cuando el proceso tiene éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.1 | Cambio del valor devuelto: cuando el proceso no tiene éxito devuelve false, no -1. |

## Ejemplos

Ejemplo de `cubrid_col_size`

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
