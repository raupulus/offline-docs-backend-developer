---
title: IntlChar::isdefined
description: Verifica si un punto de código está definido
source_url: https://www.php.net/manual/es/intlchar.isdefined.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isdefined.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41000
---

IntlChar::isdefined

Verifica si un punto de código está definido

## Descripción

```php
public static IntlChar::isdefined(int $codepoint): bool
```php

Determina si el punto de código especificado está "definido", lo cual generalmente significa que está asignado a un carácter.

`true` para las categorías generales distintas de "Cn" (otro, no asignado).

> [!NOTE]
> Es importante señalar que los puntos de código no caracteres (por ejemplo, U+FDD0) no están "definidos" (son Cn), pero los puntos de código de sustitución sí están "definidos" (Cs).

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un carácter definido, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isdefined("A"));
var_dump(IntlChar::isdefined(" "));
var_dump(IntlChar::isdefined("\u{FDD0}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(false)

## Véase también

`IntlChar::isdigit`, `IntlChar::isalpha`, `IntlChar::isalnum`, `IntlChar::isupper`, `IntlChar::islower`, `IntlChar::istitle`
