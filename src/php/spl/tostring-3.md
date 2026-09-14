---
title: SplFileInfo::__toString
description: Devuelve la ruta de el fichero como un string
source_url: https://www.php.net/manual/es/splfileinfo.tostring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/tostring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84290
---

SplFileInfo::\_\_toString

Devuelve la ruta de el fichero como un string

## Descripción

```php
public SplFileInfo::__toString(): string
```php

Este método retornará el nombre de fichero de el fichero referenciado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la ruta a el fichero.

## Ejemplos

Ejemplo de `SplFileInfo::__toString`

```
<?php
$info = new SplFileInfo('foo');
var_dump($info->__toString());
echo $info.PHP_EOL;

$info = new SplFileInfo('/usr/bin/php');
var_dump($info->__toString());
echo $info.PHP_EOL;
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(3) "foo"
    foo
    string(12) "/usr/bin/php"
    /usr/bin/php
