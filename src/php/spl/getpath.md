---
title: SplFileInfo::getPath
description: Obtiene la ruta sin el nombre de fichero
source_url: https://www.php.net/manual/es/splfileinfo.getpath.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getpath.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84130
---

SplFileInfo::getPath

Obtiene la ruta sin el nombre de fichero

## Descripción

```php
public SplFileInfo::getPath(): string
```php

Devuelve la ruta de el fichero, omitiendo el nombre del fichero y cualquier barra.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la ruta a el fichero.

## Ejemplos

Ejemplo de `SplFileInfo::getPath`

```
<?php
$info = new SplFileInfo('/usr/bin/php');
var_dump($info->getPath());

$info = new SplFileInfo('/usr/');
var_dump($info->getPath());?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(8) "/usr/bin"
    string(4) "/usr"

## Véase también

SplFileInfo::getRealPath, SplFileInfo::getFilename, SplFileInfo::getPathInfo
