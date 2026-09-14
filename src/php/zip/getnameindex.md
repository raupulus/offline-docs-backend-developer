---
title: ZipArchive::getNameIndex
description: Devuelve el nombre de una entrada utilizando su índice
source_url: https://www.php.net/manual/es/ziparchive.getnameindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/getnameindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108330
---

ZipArchive::getNameIndex

Devuelve el nombre de una entrada utilizando su índice

## Descripción

```php
public ZipArchive::getNameIndex(int $index, [int $flags]): string
```php

Devuelve el nombre de una entrada utilizando su índice.

## Parámetros

`index`  
El índice de la entrada.

`flags`  
Si las flags se establecen en `ZipArchive::FL_UNCHANGED`, el nombre original es devuelto sin cambios.

## Valores devueltos

Devuelve el nombre en caso de tener éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `ZipArchive::getNameIndex`

```
<?php
if ($zip->open('test.zip') == TRUE) {
 for ($i = 0; $i < $zip->numFiles; $i++) {
     $filename = $zip->getNameIndex($i);
     // ...
 }
}
?>

    
```php
