---
title: ZipArchive::open
description: Abrir un fichero de archivo en formato ZIP
source_url: https://www.php.net/manual/es/ziparchive.open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108410
---

ZipArchive::open

Abrir un fichero de archivo en formato ZIP

## Descripción

```php
public ZipArchive::open(string $filename, [int $flags]): bool
```php

Abre un archivo zip nuevo o existente para leer, escribir o modificar.

Desde libzip 1.6.0, un archivo vacío ya no es un archivo válido.

## Parámetros

`filename`  
El nombre del fichero del archivo ZIP para ser abierto.

`flags`  
El modo a utilizar para abrir el archivo.

- `ZipArchive::OVERWRITE`

- `ZipArchive::CREATE`

- `ZipArchive::RDONLY`

- `ZipArchive::EXCL`

- `ZipArchive::CHECKCONS`

## Valores devueltos

Devuelve `true` en caso de éxito, `false` o uno de los siguientes códigos de error en caso de error:

`ZipArchive::ER_EXISTS`  
El fichero ya existe.

`ZipArchive::ER_INCONS`  
Archivo zip inconsistente.

`ZipArchive::ER_INVAL`  
Argumento no válido.

`ZipArchive::ER_MEMORY`  
Falló malloc.

`ZipArchive::ER_NOENT`  
No existe el fichero.

`ZipArchive::ER_NOZIP`  
No es un archivo zip.

`ZipArchive::ER_OPEN`  
No se puede abrir el fichero.

`ZipArchive::ER_READ`  
Error de lectura.

`ZipArchive::ER_SEEK`  
Error de búsqueda.

## Ejemplos

Abrir y extraer

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test.zip');
if ($res === TRUE) {
    echo 'ok';
    $zip->extractTo('test');
    $zip->close();
} else {
    echo 'falló, código:' . $res;
}
?>

   
```php

Crear un fichero

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test.zip', ZipArchive::CREATE);
if ($res === TRUE) {
    $zip->addFromString('test.txt', 'el contenido del fichero va aquí');
    $zip->addFile('data.txt', 'entryname.txt');
    $zip->close();
    echo 'ok';
} else {
    echo 'falló';
}
?>

   
```php

Crear un fichero temporal

```
<?php
$name = tempnam(sys_get_temp_dir(), "FOO");
$zip = new ZipArchive;
$res = $zip->open($name, ZipArchive::OVERWRITE); /* truncate as empty file is not valid */
if ($res === TRUE) {
    $zip->addFile('data.txt', 'entryname.txt');
    $zip->close();
    echo 'ok';
} else {
    echo 'failed';
}
?>

     
```php
