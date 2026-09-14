---
title: SplFileInfo::getExtension
description: Obtiene la extensión del fichero
source_url: https://www.php.net/manual/es/splfileinfo.getextension.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getextension.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 62126c55f
order: 84050
---

SplFileInfo::getExtension

Obtiene la extensión del fichero

## Descripción

```php
public SplFileInfo::getExtension(): string
```php

Devuelve la extensión del fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` que contiene la extensión del fichero, o un vacío `string` si el archivo no tiene extensión.

## Ejemplos

`SplFileInfo::getExtension` ejemplo

```
<?php

$info = new SplFileInfo('foo.txt');
var_dump($info->getExtension());

$info = new SplFileInfo('photo.jpg');
var_dump($info->getExtension());

$info = new SplFileInfo('something.tar.gz');
var_dump($info->getExtension());

?>

   
```php

El ejemplo anterior mostrará:

    string(3) "txt"
    string(3) "jpg"
    string(2) "gz"

## Notas

> [!NOTE]
> Otra forma de obtener la extensión es usar la función `pathinfo`.
>
> <div class="informalexample">
>
> ```
> <?php
> $extension = pathinfo($info->getFilename(), PATHINFO_EXTENSION);
> ?>
>
>     
> ```
>
> </div>

## Véase también

SplFileInfo::getFilename

SplFileInfo::getBasename

pathinfo
