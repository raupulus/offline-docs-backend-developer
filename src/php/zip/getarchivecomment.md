---
title: ZipArchive::getArchiveComment
description: Devuelve el comentario del archivo ZIP
source_url: https://www.php.net/manual/es/ziparchive.getarchivecomment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/getarchivecomment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108250
---

ZipArchive::getArchiveComment

Devuelve el comentario del archivo ZIP

## Descripción

```php
public ZipArchive::getArchiveComment([int $flags]): string
```php

Devuelve el comentario del archivo ZIP.

## Parámetros

`flags`  
Si las flags se establecen en `ZipArchive::FL_UNCHANGED`, el comentario original se devuelve sin cambios.

## Valores devueltos

Devuelve el comentario del archivo Zip o `false` si ocurre un error.

## Ejemplos

Vuelca el comentario del archivo

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test_with_comment.zip');
if ($res === TRUE) {
    var_dump($zip->getArchiveComment());
    /* O usando la propiedad del archivo */
    var_dump($zip->comment);
} else {
    echo 'falló, código:' . $res;
}
?>

   
```php
