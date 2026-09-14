---
title: ZipArchive::statIndex
description: Obtiene los detalles de una entrada definida por su índice
source_url: https://www.php.net/manual/es/ziparchive.statindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/statindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108600
---

ZipArchive::statIndex

Obtiene los detalles de una entrada definida por su índice

## Descripción

```php
public ZipArchive::statIndex(int $index, [int $flags]): array
```php

La función obtiene información acerca de la entrada definida por su índice.

## Parámetros

`index`  
Índice de la entrada

`flags`  
`ZipArchive::FL_UNCHANGED` podría ser puesto con otros OR lógicos en él para pedir información acerca del fichero original en el archivo, ignorando cualquiera de los cambios hechos.

## Valores devueltos

Devuelve una matríz conteniendo los detalles de la entrada, o `false` si ocurre un error.

## Ejemplos

Volcar la información estadística de una entrada

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test.zip');
if ($res === TRUE) {
    print_r($zip->statIndex(3));
    $zip->close();
} else {
    echo 'falló, código:' . $res;
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [name] => foobar/baz
        [index] => 3
        [crc] => 499465816
        [size] => 27
        [mtime] => 1123164748
        [comp_size] => 24
        [comp_method] => 8
    )
