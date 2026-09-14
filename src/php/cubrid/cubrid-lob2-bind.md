---
title: cubrid_lob2_bind
description: Asocia un objeto LOB o una cadena de caracteres a un objeto LOB como
  argumento de una consulta preparada
source_url: https://www.php.net/manual/es/function.cubrid-lob2-bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob2-bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9200
---

cubrid_lob2_bind

Asocia un objeto LOB o una cadena de caracteres a un objeto LOB como argumento de una consulta preparada

## Descripción

```php
cubrid_lob2_bind(resource $req_identifier, int $bind_index, mixed $bind_value, [string $bind_value_type]): bool
```php

La función `cubrid_lob2_bind` se utiliza para asociar datos BLOB/CLOB a un marcador correspondiente en una consulta SQL pasada a la función `cubrid_prepare`. Si el argumento `bind_value_type` no se proporciona, la cadena será por omisión "BLOB". Pero si se utiliza primero la función `cubrid_lob2_new`, el argumento `bind_value_type` será consistente con el argumento `type` en la función `cubrid_lob2_new`.

## Parámetros

`req_identifier`  
Identificador de la petición, resultado de la función `cubrid_prepare`.

`bind_index`  
Posición de los argumentos asociados. Comienza en 1.

`bind_value`  
Valor actual para la asociación.

`bind_value_type`  
Debe ser "BLOB" o "CLOB" y no es sensible a mayúsculas/minúsculas. Si no se proporciona, el valor por omisión será "BLOB".

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_lob2_bind`

```
<?php
// Tabla : test_lob (id INT, contents CLOB)

$conn = cubrid_connect("localhost", 33000, "demodb", "dba", "");

cubrid_execute($conn,"DROP TABLE if exists test_lob");
cubrid_execute($conn,"CREATE TABLE test_lob (id INT, contents CLOB)");

$req = cubrid_prepare($conn, "INSERT INTO test_lob VALUES (?, ?)");

cubrid_bind($req,1, 3);

$lob = cubrid_lob2_new($conn, 'CLOB');
cubrid_lob2_bind($req, 2, $lob);

cubrid_execute($req);

cubrid_bind($req, 1, 4);

cubrid_lob2_bind($req, 2, 'CUBRID LOB2 TEST', 'CLOB');

cubrid_execute($req);

cubrid_disconnect($conn);
?>

   
```php

## Véase también

cubrid_lob2_new

cubrid_lob2_close
