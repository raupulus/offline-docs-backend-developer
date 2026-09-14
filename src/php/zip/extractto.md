---
title: ZipArchive::extractTo
description: Extraer el contenido del archivo
source_url: https://www.php.net/manual/es/ziparchive.extractto.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/extractto.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108240
---

ZipArchive::extractTo

Extraer el contenido del archivo

## Descripción

```php
public ZipArchive::extractTo(string $pathto, [array $files]): bool
```php

Extrae el archivo completo o los ficheros dados en la ruta que se especifique.

> [!WARNING]
> Los permisos por omisión para los archivos y directorios extraídos dan el más amplio acceso posible. Esto se puede restringir estableciendo la umask actual, que se puede cambiar usando `umask`.
>
> Por razones de seguridad, los permisos originales no se restauran. Para ver un ejemplo de cómo restaurarlos, consulte el [ejemplo de código](#ziparchive.getexternalattributesindex.examples.perms) en la página de ZipArchive::getExternalAttributesIndex.

## Parámetros

`pathto`  
Destino en donde extraer los ficheros.

`files`  
Las entradas a extraer. Acepta tanto un solo nombre o un array de nombres.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Extraer todas las entradas

```
<?php
$zip = new ZipArchive;
if ($zip->open('test.zip') === TRUE) {
    $zip->extractTo('/my/destination/dir/');
    $zip->close();
    echo 'ok';
} else {
    echo 'failed';
}
?>

   
```php

Extraer dos entradas

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test_im.zip');
if ($res === TRUE) {
    $zip->extractTo('/my/destination/dir/', array('pear_item.gif', 'testfromfile.php'));
    $zip->close();
    echo 'ok';
} else {
    echo 'failed';
}
?>

   
```php

## Notas

> [!NOTE]
> Los sistemas de archivos NTFS de Windows no soportan ciertos caracteres en los nombres de fichero, como `<|>*?":`. Los nombres de fichero con un punto final no son soportados. A diferencia de algunas herramientas de extracción, este método no reemplaza estos caracteres con un guión bajo, sino que falla al extraer tales ficheros.
