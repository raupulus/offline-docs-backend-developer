---
title: get_included_files
description: Devuelve un array con los nombres de los ficheros que son incluidos en
  un script
source_url: https://www.php.net/manual/es/function.get-included-files.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/get-included-files.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 8dd14a886
order: 38890
---

get_included_files

Devuelve un array con los nombres de los ficheros que son incluidos en un script

## Descripción

```php
get_included_files(): array
```php

Devuelve un array que contiene los nombres de todos los ficheros que han sido añadidos al script con las funciones `include`, `include_once`, `require` o `require_once`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array que contiene los nombres de todos los ficheros.

El script en curso es considerado como fichero incluido, por lo que será listado junto con los otros ficheros a los que se hace referencia con `include` y las funciones similares.

Los ficheros incluidos o requeridos varias veces solo se muestran una vez en el array devuelto.

## Ejemplos

Ejemplo con `get_included_files`

```
<?php
// Este fichero es abc.php

include 'test1.php';
include_once 'test2.php';
require 'test3.php';
require_once 'test4.php';

$included_files = get_included_files();

foreach ($included_files as $filename) {
    echo "$filename\n";
}

?>

    
```php

El ejemplo anterior mostrará:

    /path/to/abc.php
    /path/to/test1.php
    /path/to/test2.php
    /path/to/test3.php
    /path/to/test4.php

## Véase también

`include`, `include_once`, `require`, `require_once`, `get_required_files`
