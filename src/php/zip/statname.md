---
title: ZipArchive::statName
description: Obtener los detalles de una entrada definida por su nombre
source_url: https://www.php.net/manual/es/ziparchive.statname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/statname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108610
---

ZipArchive::statName

Obtener los detalles de una entrada definida por su nombre

## Descripción

```php
public ZipArchive::statName(string $name, [int $flags]): array
```php

La función obtiene información acerca de la entrada definida por su nombre.

## Parámetros

`name`  
Nombre de la entrada

`flags`  
El argumento flags especifica cómo la búsqueda del nombre debería se hecho. También, `ZipArchive::FL_UNCHANGED` podría ser puesta con otros OR en él para solicitar la información acerca del fichero original en el archivo, ignorando cualquier cambio realizado.

- `ZipArchive::FL_NOCASE`

- `ZipArchive::FL_NODIR`

- `ZipArchive::FL_UNCHANGED`

## Valores devueltos

Devuelve una matríz que contenie detalles de la entrada o `false` si ocurre un error.

## Ejemplos

Volcar la información estadística de una entrada

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test.zip');
if ($res === TRUE) {
    print_r($zip->statName('foobar/baz'));
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
