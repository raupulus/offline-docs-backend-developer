---
title: filter_list
description: Devuelve una lista de todos los filtros soportados
source_url: https://www.php.net/manual/es/function.filter-list.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filter/functions/filter-list.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filter
translation_status: ready
translation_reviewed: false
translation_revision: 627f933cf
order: 24210
---

filter_list

Devuelve una lista de todos los filtros soportados

## Descripción

```php
filter_list(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array con los nombres de todos los filtros soportados, o un array vacío si no hay tales filtros. Los índices de este array no son los IDs de los filtros, estos se pueden obtener con `filter_id` a partir de un nombre.

## Ejemplos

Ejemplo de `filter_list`

```
<?php
print_r(filter_list());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => int
        [1] => boolean
        [2] => float
        [3] => validate_regexp
        [4] => validate_url
        [5] => validate_email
        [6] => validate_ip
        [7] => string
        [8] => stripped
        [9] => encoded
        [10] => special_chars
        [11] => unsafe_raw
        [12] => email
        [13] => url
        [14] => number_int
        [15] => number_float
        [16] => magic_quotes
        [17] => callback
    )
