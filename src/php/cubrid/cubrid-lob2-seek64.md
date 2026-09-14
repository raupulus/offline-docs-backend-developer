---
title: cubrid_lob2_seek64
description: Desplaza el cursor de un objeto LOB
source_url: https://www.php.net/manual/es/function.cubrid-lob2-seek64.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob2-seek64.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9270
---

cubrid_lob2_seek64

Desplaza el cursor de un objeto LOB

## Descripción

```php
cubrid_lob2_seek64(resource $lob_identifier, string $offset, [int $origin]): bool
```php

La función `cubrid_lob2_seek64` se utiliza para desplazar la posición del cursor en un objeto LOB de un valor proporcionado por el argumento `offset`, en la dirección proporcionada por el argumento `origin`. Si la posición `offset` es mayor que la capacidad de almacenamiento de un entero, puede utilizarse esta función.

Para definir el argumento `origin`, puede utilizarse la constante `CUBRID_CURSOR_FIRST` para definir la posición del cursor a la que se añaden `offset` unidades desde el principio. En este caso, `offset` debe ser un valor positivo.

Si se utiliza `CUBRID_CURSOR_CURRENT` para el argumento `origin`, puede desplazarse hacia atrás, así como hacia adelante. Y el argumento `offset` podrá ser positivo o negativo.

Si se utiliza la constante `CUBRID_CURSOR_LAST` para el argumento `origin`, puede desplazarse hacia atrás de `offset` unidades desde el final del objeto LOB y el argumento `offset` solo podrá ser positivo.

> [!NOTE]
> Si se utiliza esta función para desplazar la posición del cursor de un objeto LOB, debe pasarse el argumento `offset` en forma de string.

## Parámetros

`lob_identifier`  
Un identificador LOB, recuperado desde la función `cubrid_lob2_new` o desde el conjunto de resultados.

`offset`  
Número de unidades de desplazamiento del cursor.

`origin`  
Este argumento puede tomar los siguientes valores:

CUBRID_CURSOR_FIRST: desplaza el cursor hacia adelante partiendo del principio.

CUBRID_CURSOR_CURRENT: desplaza el cursor hacia atrás y hacia adelante desde la posición actual.

CUBRID_CURSOR_LAST: desplaza el cursor hacia atrás desde el final del objeto LOB.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `cubrid_lob2_seek64`

```
<?php
// test_lob (id INT, contents CLOB)
// La longitud de los datos de doc_1.txt debe ser superior a 20101029056306120215.

$conn = cubrid_connect("localhost", 33000, "demodb", "dba", "");

cubrid_execute($conn,"DROP TABLE if exists test_lob");
cubrid_execute($conn,"CREATE TABLE test_lob (id INT, contents CLOB)");

$req = cubrid_prepare($conn, "INSERT INTO test_lob VALUES (?, ?)");
cubrid_bind($req, 1, 1);

$lob = cubrid_lob2_new($conn, "clob");
cubrid_lob2_import($lob, "doc_1.txt");
cubrid_lob2_bind($req, 2, $lob, 'CLOB'); // o cubrid_lob2_bind($req, 2, $lob);

cubrid_execute($req);

cubrid_lob2_close($lob);

$req = cubrid_execute($conn, "select * from test_lob");
$row = cubrid_fetch_row($req, CUBRID_LOB);
$lob = $row[1];

cubrid_lob2_seek64($lob, "20101029056306120215", CUBRID_CURSOR_FIRST);
$data = cubrid_lob2_read($lob, 20);
echo $data."\n";
cubrid_disconnect($conn);
?>

   
```php

## Véase también

cubrid_lob2_read

cubrid_lob2_write

cubrid_lob2_seek

cubrid_lob2_tell

cubrid_lob2_tell64

cubrid_lob2_size

cubrid_lob2_size64
