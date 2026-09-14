---
title: SplFileInfo::isFile
description: Dice si el objeto hace referencia a un fichero normal
source_url: https://www.php.net/manual/es/splfileinfo.isfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/isfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84220
---

SplFileInfo::isFile

Dice si el objeto hace referencia a un fichero normal

## Descripción

```php
public SplFileInfo::isFile(): bool
```php

Comprueba si el fichero que el objecto SplFileInfo hace referencia existe es un fichero regular.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si el fichero existe y si es un fichero normal (no un enlace), `false` en caso contrario.

## Ejemplos

Ejemplo de `SplFileInfo::isFile`

```
<?php
$info = new SplFileInfo(__FILE__);
var_dump($info->isFile());

$info = new SplFileInfo(dirname(__FILE__));
var_dump($info->isFile());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(false)
