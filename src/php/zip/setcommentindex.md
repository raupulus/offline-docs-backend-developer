---
title: ZipArchive::setCommentIndex
description: Establece el comentario de una entrada definido por su índice
source_url: https://www.php.net/manual/es/ziparchive.setcommentindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setcommentindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108490
---

ZipArchive::setCommentIndex

Establece el comentario de una entrada definido por su índice

## Descripción

```php
public ZipArchive::setCommentIndex(int $index, string $comment): bool
```php

Establece el comentario de una entrada definido por su índice.

## Parámetros

`index`  
Índice de la entrada.

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
    $zip->setCommentIndex(2, 'comentario de la entrada nueva');
    $zip->close();
    echo 'ok';
} else {
    echo 'falló';
}
?>

   
```php
