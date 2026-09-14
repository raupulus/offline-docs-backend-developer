---
title: PharData::addEmptyDir
description: Añade un directorio vacío al archivo tar/zip
source_url: https://www.php.net/manual/es/phardata.addemptydir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/addEmptyDir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64440
---

PharData::addEmptyDir

Añade un directorio vacío al archivo tar/zip

## Descripción

```php
public PharData::addEmptyDir(string $directory): void
```php

Con este método, se crea un directorio vacío con la ruta `dirname`. Este método es idéntico a `ZipArchive::addEmptyDir`.

## Parámetros

`directory`  
El nombre del directorio vacío a crear en el archivo phar

## Valores devueltos

No se devuelve ningún valor, se lanza una excepción en caso de fallo.

## Ejemplos

Un ejemplo con `PharData::addEmptyDir`

```
<?php
try {
    $a = new PharData('/ruta/al/archivo.tar');

    $a->addEmptyDir('/ruta/completa/al/fichero');
    // muestra cómo se almacena el fichero
    $b = $a['ruta/completa/al/fichero']->isDir();
} catch (Exception $e) {
    // los errores se manejan aquí
}
?>

    
```php

## Véase también

`Phar::addEmptyDir`, `PharData::addFile`, `PharData::addFromString`
