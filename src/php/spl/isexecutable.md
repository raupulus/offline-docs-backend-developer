---
title: SplFileInfo::isExecutable
description: Comprueba si el fichero es ejecutable
source_url: https://www.php.net/manual/es/splfileinfo.isexecutable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/isexecutable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84210
---

SplFileInfo::isExecutable

Comprueba si el fichero es ejecutable

## Descripción

```php
public SplFileInfo::isExecutable(): bool
```php

Comprueba si el fichero es ejecutable.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si es ejecutable, en caso contrario `false`.

## Ejemplos

Ejemplo de `SplFileInfo::isExecutable`

```
<?php
$info = new SplFileInfo('/usr/bin/php');
var_dump($info->isExecutable());

$info = new SplFileInfo('/usr/bin');
var_dump($info->isExecutable());

$info = new SplFileInfo('foo');
var_dump($info->isExecutable());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    bool(false)
