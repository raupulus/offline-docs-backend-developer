---
title: SplFileInfo::getFilename
description: Obtiene el nombre del fichero
source_url: https://www.php.net/manual/es/splfileinfo.getfilename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getfilename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 4532dcab5
order: 84070
---

SplFileInfo::getFilename

Obtiene el nombre del fichero

## Descripción

```php
public SplFileInfo::getFilename(): string
```php

Obtiene el nombre del fichero sin ningún tipo de información de la ruta de acceso.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El nombre del fichero.

## Ejemplos

`SplFileInfo::getFilename` ejemplo

```
<?php
$info = new SplFileInfo('foo.txt');
var_dump($info->getFilename());

$info = new SplFileInfo('/path/to/foo.txt');
var_dump($info->getFilename());

$info = new SplFileInfo('http://www.php.net/');
var_dump($info->getFilename());

$info = new SplFileInfo('http://www.php.net/svn.php');
var_dump($info->getFilename());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(7) "foo.txt"
    string(7) "foo.txt"
    string(11) "www.php.net"
    string(7) "svn.php"

## Véase también

SplFileInfo::getBasename
