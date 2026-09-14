---
title: ZipArchive::setCompressionName
description: Establecer el método de compresión de una entrada definida por su nombre
source_url: https://www.php.net/manual/es/ziparchive.setcompressionname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setcompressionname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108520
---

ZipArchive::setCompressionName

Establecer el método de compresión de una entrada definida por su nombre

## Descripción

```php
public ZipArchive::setCompressionName(string $name, int $method, [int $compflags]): bool
```php

Establecer el método de compresión de una entrada definida por su nombre.

## Parámetros

`name`  
El nombre de la entrada.

`method`  
El método de compresión. Una de las constantes `ZipArchive::CM_*`.

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
    $zip->setCompressionName('foo', ZipArchive::CM_STORE);
    $zip->setCompressionName('bar', ZipArchive::CM_DEFLATE);
    $zip->close();
    echo 'ok';
} else {
    echo 'fallo';
}
?>

   
```php

Añadir fichero y establecer el método de compresión

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test.zip', ZipArchive::CREATE);
if ($res === TRUE) {
    $zip->addFile('foo.jpg', 'bar.jpg');
    $zip->setCompressionName('bar.jpg', ZipArchive::CM_XZ);
    $zip->close();
    echo 'ok';
} else {
    echo 'failed';
}
?>

   
```php
