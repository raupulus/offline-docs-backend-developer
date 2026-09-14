---
title: SplFileInfo::getRealPath
description: Obtiene la ruta absoluta al fichero
source_url: https://www.php.net/manual/es/splfileinfo.getrealpath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getrealpath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84170
---

SplFileInfo::getRealPath

Obtiene la ruta absoluta al fichero

## Descripción

```php
public SplFileInfo::getRealPath(): string
```php

Este método expande todos los enlaces simbólicos, resuelve las referencias relativas y retorna la ruta real al fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la ruta al fichero, o `false` si el fichero no existe.

## Ejemplos

Ejemplo de `SplFileInfo::getRealPath`

```
<?php
$info = new SplFileInfo('/..//./../../'.__FILE__);
var_dump($info->getRealPath());

$info = new SplFileInfo('/tmp');
var_dump($info->getRealPath());

$info = new SplFileInfo('/I/Do/Not/Exist');
var_dump($info->getRealPath());

$info = new SplFileInfo('php://output');
var_dump($info->getRealPath());

$info = new SplFileInfo("");
var_dump($info->getRealPath());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(28) "/private/tmp/phptempfile.php"
    string(12) "/private/tmp"
    bool(false)
    bool(false)
    string(12) "/private/tmp"

## Véase también

SplFileInfo::isLink, realpath
