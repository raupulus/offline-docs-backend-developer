---
title: ZipArchive::getArchiveFlag
description: Devuelve el valor de una bandera global del archivo
source_url: https://www.php.net/manual/es/ziparchive.getarchiveflag.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/getarchiveflag.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108260
---

ZipArchive::getArchiveFlag

Devuelve el valor de una bandera global del archivo

## Descripción

```php
public ZipArchive::getArchiveFlag(int $flag, [int $flags]): int
```php

Devuelve el valor de una bandera global del archivo.

## Parámetros

`flag`  
La bandera global a recuperar, entre las constantes `AFL_*`:

- `ZipArchive::AFL_RDONLY`

- `ZipArchive::AFL_IS_TORRENTZIP`

- `ZipArchive::AFL_WANT_TORRENTZIP`

- `ZipArchive::AFL_CREATE_OR_KEEP_FILE_FOR_EMPTY_ARCHIVE`

`flags`  
Si `flags` se define como `ZipArchive::FL_UNCHANGED`, la bandera original no se modifica y se devuelve.

## Valores devueltos

Devuelve 1 si la bandera está definida para el archivo, 0 si no lo está, y -1 si ocurre un error.

## Ejemplos

Prueba si el archivo está en formato torrentzip

```
<?php

$zip = new ZipArchive;
$res = $zip->open('test.zip');

if ($res === TRUE) {
    var_dump($zip->getArchiveFlag(ZipArchive::AFL_IS_TORRENTZIP));
} else {
    echo 'Fallo, código: ' . $res;
}
?>

   
```php

## Véase también

ZipArchive::setArchiveFlag
