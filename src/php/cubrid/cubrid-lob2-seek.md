---
title: cubrid_lob2_seek
description: Desplaza el cursor de un objeto LOB
source_url: https://www.php.net/manual/es/function.cubrid-lob2-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob2-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9260
---

cubrid_lob2_seek

Desplaza el cursor de un objeto LOB

## Descripción

```php
cubrid_lob2_seek(resource $lob_identifier, int $offset, [int $origin]): bool
```php

La función `cubrid_lob2_seek` se utiliza para desplazar la posición del cursor de un objeto LOB según el argumento `offset` especificado, y en la dirección indicada por el argumento `origin`.

Para definir el argumento `origin`, puede utilizarse la constante `CUBRID_CURSOR_FIRST` para desplazar la posición del cursor `offset` unidades hacia adelante desde el inicio. En este caso, `offset` debe ser un valor positivo.

Si se utiliza la constante `CUBRID_CURSOR_CURRENT` para el parámetro `origin`, puede desplazarse hacia adelante o hacia atrás. El argumento `offset` puede ser negativo o positivo.

Si se utiliza la constante `CUBRID_CURSOR_LAST` para el parámetro `origin`, puede desplazarse hacia atrás `offset` unidades desde el final del objeto LOB; el argumento `offset` solo puede ser positivo en este caso.

## Parámetros

`lob_identifier`  
Un identificador LOB, resultado de la función `cubrid_lob2_new` o recuperado desde el conjunto de resultados.

`offset`  
Número de unidades a utilizar para desplazar el cursor.

`origin`  
Este parámetro puede tomar los siguientes valores:

CUBRID_CURSOR_FIRST: Se desplaza hacia adelante desde el inicio.

CUBRID_CURSOR_CURRENT: Se desplaza hacia adelante o hacia atrás, desde la posición actual.

CUBRID_CURSOR_LAST: Se desplaza hacia atrás desde el final del objeto LOB.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_lob2_seek`

```
<?php
// test_lob (id INT, contents CLOB)
$conn = cubrid_connect("localhost", 33000, "demodb", "dba", "");

cubrid_execute($conn,"DROP TABLE if exists test_lob");
cubrid_execute($conn,"CREATE TABLE test_lob (id INT, contents CLOB)");
$req = cubrid_prepare($conn, "INSERT INTO test_lob VALUES(2, ?)");

$lob = cubrid_lob2_new($conn, 'CLOB');
$len = cubrid_lob2_write($lob, "Hello world");

cubrid_lob2_seek($lob, 0, CUBRID_CURSOR_LAST);
cubrid_lob2_write($lob, "beautiful");

cubrid_lob2_seek($lob, 15, CUBRID_CURSOR_FIRST);
$data = cubrid_lob2_read($lob, 5);

echo $data."\n";

cubrid_lob2_bind($req, 1, $lob);
cubrid_execute($req);

cubrid_disconnect($conn);
?>

   
```php

## Véase también

cubrid_lob2_read

cubrid_lob2_write

cubrid_lob2_seek64

cubrid_lob2_tell

cubrid_lob2_tell64

cubrid_lob2_size

cubrid_lob2_size64
