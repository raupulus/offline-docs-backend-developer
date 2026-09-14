---
title: posix_getgroups
description: Devolver el conjunto de grupos del proceso actual
source_url: https://www.php.net/manual/es/function.posix-getgroups.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getgroups.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: f8854f6a6
order: 65220
---

posix_getgroups

Devolver el conjunto de grupos del proceso actual

## Descripción

```php
posix_getgroups(): array
```php

Obtiene el conjunto de grupos del proceso actual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array de enteros que contiene los ids numéricos del conjunto de grupos del proceso actual, o `false` si ocurre un error.

## Ejemplos

Ejemplo de uso de `posix_getgroups`

```
<?php

$groups = posix_getgroups();

print_r($groups);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => 4
        [1] => 20
        [2] => 24
        [3] => 25
        [4] => 29
        [5] => 30
        [6] => 33
        [7] => 44
        [8] => 46
        [9] => 104
        [10] => 109
        [11] => 110
        [12] => 1000
    )

## Véase también

`posix_getgrgid`
