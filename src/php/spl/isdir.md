---
title: SplFileInfo::isDir
description: Dice si el fichero es un directorio
source_url: https://www.php.net/manual/es/splfileinfo.isdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/isdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84200
---

SplFileInfo::isDir

Dice si el fichero es un directorio

## Descripción

```php
public SplFileInfo::isDir(): bool
```php

Este método puede ser usado para determinar si el fichero es un directorio.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si es un directorio, `false` en caso contrario.

## Ejemplos

Ejemplo de `SplFileInfo::isDir`

```
<?php
$d = new SplFileInfo(dirname(__FILE__));
var_dump($d->isDir());

$d = new SplFileInfo(__FILE__);
var_dump($d->isDir());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(false)
