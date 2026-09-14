---
title: IntlChar::isgraph
description: Verifica si un punto de código es un carácter gráfico
source_url: https://www.php.net/manual/es/intlchar.isgraph.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isgraph.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: e20e74073
order: 41020
---

IntlChar::isgraph

Verifica si un punto de código es un carácter gráfico

## Descripción

```php
public static IntlChar::isgraph(int $codepoint): bool
```php

Determina si el punto de código especificado es un carácter "gráfico" (mostrable, excluyendo los espacios).

`true` para todos los caracteres excepto aquellos con las categorías generales "Cc" (códigos de control), "Cf" (controles de formato), "Cs" (sustitutos), "Cn" (no asignados) y "Z" (separadores).

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es un carácter "gráfico", `false` en caso contrario. Devuelve `null` en caso de error.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isgraph("A"));
var_dump(IntlChar::isgraph("1"));
var_dump(IntlChar::isgraph("\u{2603}"));
var_dump(IntlChar::isgraph("\n"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(true)
    bool(false)

## Véase también

`ctype_graph`
