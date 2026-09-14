---
title: ZipArchive::getFromIndex
description: Devuelve el contenido de la entrada usando su índice
source_url: https://www.php.net/manual/es/ziparchive.getfromindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/getfromindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108310
---

ZipArchive::getFromIndex

Devuelve el contenido de la entrada usando su índice

## Descripción

```php
public ZipArchive::getFromIndex(int $index, [int $len], [int $flags]): string
```php

Devuelve el contenido de la entrada usando su índice.

## Parámetros

`index`  
El índice de la entrada

`len`  
La longitud que se see desde la entrada. Si es `0`, entonces toda la entrada se lee.

`flags`  
Las flags usadas para abrir el fichero. Los siguientes valores pueden combinarse con OR.

- `ZipArchive::FL_UNCHANGED`

- `ZipArchive::FL_COMPRESSED`

## Valores devueltos

Devuelve el contenido de la entrada si se ejecutó con éxito o `false` si ocurre un error.

## Ejemplos

Obtener el contenido del fichero

```
<?php
$zip = new ZipArchive;
if ($zip->open('test.zip') === TRUE) {
    echo $zip->getFromIndex(2);
    $zip->close();
} else {
    echo 'falló';
}
?>

   
```php

## Véase también

ZipArchive::getFromName
