---
title: ZipArchive::setCompressionIndex
description: Establecer el método de compresión de una entrada definida por su índice
source_url: https://www.php.net/manual/es/ziparchive.setcompressionindex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setcompressionindex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108510
---

ZipArchive::setCompressionIndex

Establecer el método de compresión de una entrada definida por su índice

## Descripción

```php
public ZipArchive::setCompressionIndex(int $index, int $method, [int $compflags]): bool
```php

Establecer el método de compresión de una entrada definida por su índice.

## Parámetros

`index`  
El índice de la entrada.

`method`  
El método de compresión, una de las constantes `ZipArchive::CM_*`.

`compflags`  
Nivel de compresión.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Añadir ficheros con diferentes métodos de compresión a un archivo

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test.zip', ZipArchive::CREATE);
if ($res === TRUE) {
    $zip->addFromString('foo', 'Un texto');
    $zip->addFromString('bar', 'Otro texto');
    $zip->setCompressionIndex(0, ZipArchive::CM_STORE);
    $zip->setCompressionIndex(1, ZipArchive::CM_DEFLATE);
    $zip->close();
    echo 'ok';
} else {
    echo 'fallo';
}
?>

   
```php
