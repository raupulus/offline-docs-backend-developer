---
title: ZipArchive::renameIndex
description: Renombra una entrada definida por su índice
source_url: https://www.php.net/manual/es/ziparchive.renameindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/renameindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108440
---

ZipArchive::renameIndex

Renombra una entrada definida por su índice

## Descripción

```php
public ZipArchive::renameIndex(int $index, string $new_name): bool
```php

Renombra una entrada definida por su índice.

## Parámetros

`index`  
Índice de la entrada a renombrar.

`new_name`  
Nombre nuevo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Renombra una entrada

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test.zip');
if ($res === TRUE) {
    $zip->renameIndex(2,'newname.txt');
    $zip->close();
} else {
    echo 'falló, código:' . $res;
}
?>

   
```php
