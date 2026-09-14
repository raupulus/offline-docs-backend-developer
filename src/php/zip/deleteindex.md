---
title: ZipArchive::deleteIndex
description: Elimina una entrada en el archivo usando su índice
source_url: https://www.php.net/manual/es/ziparchive.deleteindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/deleteindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108220
---

ZipArchive::deleteIndex

Elimina una entrada en el archivo usando su índice

## Descripción

```php
public ZipArchive::deleteIndex(int $index): bool
```php

Elimina una entrada en su archivo usando su índice.

## Parámetros

`index`  
Índice de la entrada a eliminar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Elimina el fichero desde el archivo usando su índice

```
<?php
$zip = new ZipArchive;
if ($zip->open('test.zip') === TRUE) {
    $zip->deleteIndex(2);
    $zip->close();
    echo 'ok';
} else {
    echo 'falló';
}
?>

   
```php
