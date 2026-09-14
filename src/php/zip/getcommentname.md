---
title: ZipArchive::getCommentName
description: Devuelve el comentario de una entrada usando el nombre de la entrada
source_url: https://www.php.net/manual/es/ziparchive.getcommentname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/getcommentname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108280
---

ZipArchive::getCommentName

Devuelve el comentario de una entrada usando el nombre de la entrada

## Descripción

```php
public ZipArchive::getCommentName(string $name, [int $flags]): string
```php

Devuelve el comentario de una entrada usando el nombre de la entrada.

## Parámetros

`name`  
Nombre de la entrada

`flags`  
Si flags está defindo a `ZipArchive::FL_UNCHANGED`, se devuelve el comentario original no cambiado.

## Valores devueltos

Devuelve el comentario si se ejecutó con éxito o `false` si ocurre un error.

## Ejemplos

Vuelca el comentario de la entrada

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test1.zip');
if ($res === TRUE) {
    var_dump($zip->getCommentName('test/entry1.txt'));
} else {
    echo 'Falló, código:' . $res;
}
?>

   
```php
