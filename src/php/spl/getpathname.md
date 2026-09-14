---
title: SplFileInfo::getPathname
description: Obtiene la ruta de un fichero
source_url: https://www.php.net/manual/es/splfileinfo.getpathname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getpathname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84150
---

SplFileInfo::getPathname

Obtiene la ruta de un fichero

## Descripción

```php
public SplFileInfo::getPathname(): string
```php

Devuelve la ruta de el fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

la ruta de el fichero.

## Ejemplos

Ejemplo de `SplFileInfo::getPathname`

```
<?php
$info = new SplFileInfo('/usr/bin/php');
var_dump($info->getPathname());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(12) "/usr/bin/php"

## Véase también

SplFileInfo::getRealPath
