---
title: SplFileInfo::getBasename
description: Obtiene el nombre base del fichero
source_url: https://www.php.net/manual/es/splfileinfo.getbasename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getbasename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84030
---

SplFileInfo::getBasename

Obtiene el nombre base del fichero

## Descripción

```php
public SplFileInfo::getBasename([string $suffix]): string
```php

Este método devuelve el nombre base del fichero, directorio o enlace sin informacion de la ruta de acceso.

> [!CAUTION]
> `SplFileInfo::getBasename` es consciente de la configuración regional, por lo que para que vea el nombre base correcto con rutas de caracteres multibyte, la configuración regional correspondiente debe con la función `setlocale`.

## Parámetros

`suffix`  
Sufijo opcional para omitir el nombre de la base devuelta.

## Valores devueltos

Devuelve el nombre de la base, sin información de la ruta de acceso.

## Ejemplos

`SplFileInfo::getBasename`ejemplo

```
<?php
$info = new SplFileInfo('file.txt');
var_dump($info->getBasename());

$info = new SplFileInfo('/path/to/file.txt');
var_dump($info->getBasename());

$info = new SplFileInfo('/path/to/file.txt');
var_dump($info->getBasename('.txt'));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(8) "file.txt"
    string(8) "file.txt"
    string(4) "file"

## Véase también

SplFileInfo::getFilename
