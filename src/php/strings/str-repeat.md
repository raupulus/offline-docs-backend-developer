---
title: str_repeat
description: Repite un string
source_url: https://www.php.net/manual/es/function.str-repeat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-repeat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: e095023e4
order: 89170
---

str_repeat

Repite un string

## Descripción

```php
str_repeat(string $string, int $times): string
```php

Retorna el string `string` repetido `times` veces.

## Parámetros

`string`  
El string a repetir.

`times`  
Número de veces que el string `string` debe ser multiplicado.

`times` debe ser positivo o nulo. Si `times` es 0, la función retorna el string vacío.

## Valores devueltos

Retorna el string, repetido `times` veces.

## Ejemplos

Ejemplo con `str_repeat`

```
<?php
echo str_repeat("-=", 10);
?>

    
```php

El ejemplo anterior mostrará:

    -=-=-=-=-=-=-=-=-=-=

## Véase también

[for](#control-structures.for), `str_pad`, `substr_count`
