---
title: ZipArchive::setArchiveComment
description: Establece el comentario de un archivo ZIP
source_url: https://www.php.net/manual/es/ziparchive.setarchivecomment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setarchivecomment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108470
---

ZipArchive::setArchiveComment

Establece el comentario de un archivo ZIP

## Descripción

```php
public ZipArchive::setArchiveComment(string $comment): bool
```php

Establece el comentario de un archivo ZIP.

## Parámetros

`comment`  
Los contenidos del comentario.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Crear un archivo y establecer un comentario

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test.zip', ZipArchive::CREATE);
if ($res === TRUE) {
    $zip->addFromString('test.txt', 'El contenido del fichero va aquí');
    $zip->setArchiveComment('nuevo comentario del archivo');
    $zip->close();
    echo 'ok';
} else {
    echo 'falló';
}
?>

   
```php
