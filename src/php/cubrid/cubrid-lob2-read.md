---
title: cubrid_lob2_read
description: Lee datos BLOB/CLOB
source_url: https://www.php.net/manual/es/function.cubrid-lob2-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-lob2-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9250
---

cubrid_lob2_read

Lee datos BLOB/CLOB

## Descripción

```php
cubrid_lob2_read(resource $lob_identifier, int $len): string
```php

La función `cubrid_lob2_read` lee `len` bytes desde los datos LOB, y devuelve los bytes leídos.

## Parámetros

`lob_identifier`  
Un identificador LOB, resultado de la función `cubrid_lob2_new` o recuperado desde el conjunto de resultados.

`len`  
Cantidad de datos a leer desde los datos LOB.

## Valores devueltos

Devuelve el contenido como `string`, `false` cuando no hay más datos, o `null` si ocurre un error.

## Ejemplos

Ejemplo 1 con `cubrid_lob2_read`

```
<?php
// test_lob (id INT, contents CLOB)

$conn = cubrid_connect("localhost", 33000, "demodb", "public", "");

$req = cubrid_execute($conn, "select * from test_lob");

$row = cubrid_fetch_row($req, CUBRID_LOB);

print "position now is " . cubrid_lob2_tell($row[1]) . "\n";

cubrid_lob2_seek($row[1], 10, CUBRID_CURSOR_FIRST);

print "\nPosición después del desplazamiento: " . cubrid_lob2_tell($row[1]) . "\n";

$data = cubrid_lob2_read($row[1], 12);

print "\nPosición después de la lectura: " . cubrid_lob2_tell($row[1]) . "\n";

print $data . "\n";

cubrid_lob2_seek($row[1], 5, CUBRID_CURSOR_CURRENT);

print "\nPosición después de un nuevo desplazamiento: " . cubrid_lob2_tell($row[1]) . "\n";

$data = cubrid_lob2_read($row[1], 20);
print $data . "\n";

cubrid_disconnect($conn);
?>

   
```php

Ejemplo 2 con `cubrid_lob2_read`

```
<?php
// test_lob (id INT, contents CLOB)

$conn = cubrid_connect("localhost", 33000, "demodb", "dba", "");

$req = cubrid_execute($conn, "select * from test_lob");

$row = cubrid_fetch_row($req, CUBRID_LOB);

while (true) {
    if ($data = cubrid_lob2_read($row[1], 1024)) {
        print $data . "\n";
    }
    elseif ($data === false) {
        print "No hay más datos\n";
        break;
    }
    else {
        print "Ha ocurrido un error\n";
        break;
    }
}

cubrid_disconnect($conn);
?>

   
```php

## Véase también

cubrid_lob2_write

cubrid_lob2_seek

cubrid_lob2_seek64

cubrid_lob2_tell

cubrid_lob2_tell64

cubrid_lob2_size

cubrid_lob2_size64
