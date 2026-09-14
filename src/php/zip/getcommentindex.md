---
title: ZipArchive::getCommentIndex
description: Devuelve el comentario de una entrada usando la entrada díndice
source_url: https://www.php.net/manual/es/ziparchive.getcommentindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/getcommentindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108270
---

ZipArchive::getCommentIndex

Devuelve el comentario de una entrada usando la entrada díndice

## Descripción

```php
public ZipArchive::getCommentIndex(int $index, [int $flags]): string
```php

Devuelve el comentario de una entrada usando la entrada índice.

## Parámetros

`index`  
Índice de la entrada

`flags`  
Si flags `ZipArchive::FL_UNCHANGED`, se devolverá el comentario original no cambiado.

## Valores devueltos

Con éxito devuelve el comentario o `false` si ocurre un error.

## Ejemplos

Vuelca el comentario de la entrada

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test1.zip');
if ($res === TRUE) {
    var_dump($zip->getCommentIndex(1));
} else {
    echo 'falló, código:' . $res;
}
?>

   
```php
