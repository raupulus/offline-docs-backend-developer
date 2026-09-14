---
title: get_loaded_extensions
description: Devuelve la lista de todos los módulos compilados y cargados
source_url: https://www.php.net/manual/es/function.get-loaded-extensions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/get-loaded-extensions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: ec0e47953
order: 38900
---

get_loaded_extensions

Devuelve la lista de todos los módulos compilados y cargados

## Descripción

```php
get_loaded_extensions([bool $zend_extensions]): array
```php

Devuelve un array que contiene los nombres de todos los módulos compilados y cargados por la aplicación PHP actual.

## Parámetros

`zend_extensions`  
Devuelve únicamente las extensiones Zend. Por omisión vale `false` y solo lista las extensiones PHP clásicas como mysqli por ejemplo.

## Valores devueltos

Devuelve un array indexado con los nombres de todos los módulos.

## Ejemplos

Ejemplo con `get_loaded_extensions`

```
<?php
print_r(get_loaded_extensions());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Core
        [1] => date
        [2] => libxml
        [3] => pcre
        [4] => sqlite3
        [5] => zlib
        [6] => ctype
        [7] => dom
        [8] => fileinfo
        [9] => filter
        [10] => hash
        [11] => json
        [12] => mbstring
        [13] => SPL
        [14] => PDO
        [15] => session
        [16] => posix
        [17] => Reflection
        [18] => standard
        [19] => SimpleXML
        [20] => pdo_sqlite
        [21] => Phar
        [22] => tokenizer
        [23] => xml
        [24] => xmlreader
        [25] => xmlwriter
        [26] => gmp
        [27] => iconv
        [28] => intl
        [29] => bcmath
        [30] => sodium
        [31] => Zend OPcache
    )

## Véase también

`get_extension_funcs`, `extension_loaded`, `dl`, `phpinfo`
