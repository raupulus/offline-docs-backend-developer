---
title: ZipArchive::setArchiveFlag
description: Define una bandera global de un archivo ZIP
source_url: https://www.php.net/manual/es/ziparchive.setarchiveflag.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setarchiveflag.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108480
---

ZipArchive::setArchiveFlag

Define una bandera global de un archivo ZIP

## Descripción

```php
public ZipArchive::setArchiveFlag(int $flag, int $value): bool
```php

Define una bandera global de un archivo ZIP.

## Parámetros

`flag`  
La bandera global a cambiar, entre las constantes `AFL_*`.

- `ZipArchive::AFL_WANT_TORRENTZIP`

- `ZipArchive::AFL_CREATE_OR_KEEP_FILE_FOR_EMPTY_ARCHIVE`

`value`  
El nuevo valor de la bandera.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Crear un archivo torrentzip

```
<?php
$zip = new ZipArchive;
$res = $zip->open('test.zip', ZipArchive::CREATE);
if ($res === TRUE) {
    $zip->setArchiveFlag(ZipArchive::AFL_WANT_TORRENTZIP, 1);
    $zip->addFromString('test.txt', 'file content goes here');
    $zip->close();
    echo 'ok';
} else {
    echo 'failed';
}
?>

     
```php

## Véase también

ZipArchive::getArchiveFlag
