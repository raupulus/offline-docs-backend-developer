---
title: ZipArchive::renameName
description: Renombra una entrada definida por su nombre
source_url: https://www.php.net/manual/es/ziparchive.renamename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/renamename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_revision: 963af75fa
order: 108450
---

ZipArchive::renameName

Renombra una entrada definida por su nombre

## Descripción

```php
public ZipArchive::renameName(string $name, string $new_name): bool
```php

Renombra una entrada definida por su nombre.

## Parámetros

`name`  
Nombre de la entrada a renombrar.

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
    $zip->renameName('currentname.txt','newname.txt');
    $zip->close();
} else {
    echo 'falló, código:' . $res;
}
?>

   
```php
