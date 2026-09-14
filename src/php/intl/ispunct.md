---
title: IntlChar::ispunct
description: Verifica si un punto de código es un carácter de puntuación
source_url: https://www.php.net/manual/es/intlchar.ispunct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/ispunct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: e20e74073
order: 41130
---

IntlChar::ispunct

Verifica si un punto de código es un carácter de puntuación

## Descripción

```php
public static IntlChar::ispunct(int $codepoint): bool
```php

Determina si el punto de código especificado es un carácter de puntuación.

`true` para los caracteres de categoría general "P" (puntuación).

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un carácter de puntuación, `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::ispunct("."));
var_dump(IntlChar::ispunct(","));
var_dump(IntlChar::ispunct("\n"));
var_dump(IntlChar::ispunct("$"));

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(false)
    bool(false)

## Véase también

`ctype_punct`
