---
title: ZipArchive::setCommentName
description: Establece el comentario de una entrada definido por su nombre
source_url: https://www.php.net/manual/es/ziparchive.setcommentname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setcommentname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108500
---

ZipArchive::setCommentName

Establece el comentario de una entrada definido por su nombre

## Descripción

```php
public ZipArchive::setCommentName(string $name, string $comment): bool
```php

Establece el comentario de una entrada definido por su nombre.

## Parámetros

`name`  
Nombre de la entrada.

`comment`  
Los contenidos del comentario.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Abrir un archivo y establecer un comentario para una entrada

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test.zip');
if ($res === TRUE) {
    $zip->setCommentName('entry1.txt', 'comentario de la entrada nueva');
    $zip->close();
    echo 'ok';
} else {
    echo 'falló';
}
?>

   
```php
