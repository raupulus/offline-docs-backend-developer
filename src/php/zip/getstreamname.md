---
title: ZipArchive::getStreamName
description: Recupera un manejador de archivo para la entrada definida por su nombre
  (solo lectura)
source_url: https://www.php.net/manual/es/ziparchive.getstreamname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/getstreamname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108370
---

ZipArchive::getStreamName

Recupera un manejador de archivo para la entrada definida por su nombre (solo lectura)

## Descripción

```php
public ZipArchive::getStreamName(string $name, [int $flags]): resource
```php

Recupera un manejador de archivo para la entrada definida por su nombre. Actualmente, esta función solo soporta operaciones de lectura.

## Parámetros

`name`  
El nombre de la entrada a utilizar.

`flags`  
Si `flags` se define como `ZipArchive::FL_UNCHANGED`, el flujo original es devuelto.

## Valores devueltos

Devuelve un puntero de archivo (recurso) en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Obtener el contenido de la entrada con `fread` y almacenarlo

```
<?php
$contents = '';
$z = new ZipArchive();
if ($z->open('test.zip')) {
    $fp = $z->getStreamName('test', ZipArchive::FL_UNCHANGED);
    if(!$fp) die($z->getStatusString());

    echo stream_get_contents($fp);

    fclose($fp);
}
?>

     
```php

## Véase también

ZipArchive::getStreamIndex
