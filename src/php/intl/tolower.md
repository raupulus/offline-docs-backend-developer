---
title: IntlChar::tolower
description: Convierte un carácter Unicode a minúscula
source_url: https://www.php.net/manual/es/intlchar.tolower.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/tolower.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41240
---

IntlChar::tolower

Convierte un carácter Unicode a minúscula

## Descripción

```php
public static IntlChar::tolower(int $codepoint): int
```php

El carácter dado se mapea a su equivalente en minúscula. Si el carácter no tiene equivalente en minúscula, se devuelve el carácter original.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve el Simple_Lowercase_Mapping del punto de código, si está disponible; de lo contrario, el punto de código mismo. Devuelve `null` en caso de error.

El tipo de retorno es `int` a menos que el punto de código haya sido pasado como un `string` UTF-8, en cuyo caso se devuelve un `string`. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::tolower("A"));
var_dump(IntlChar::tolower("a"));
var_dump(IntlChar::tolower("Φ"));
var_dump(IntlChar::tolower("φ"));
var_dump(IntlChar::tolower("1"));
var_dump(IntlChar::tolower(ord("A")));
var_dump(IntlChar::tolower(ord("a")));
?>

   
```php

El ejemplo anterior mostrará:

        
    string(1) "a"
    string(1) "a"
    string(2) "φ"
    string(2) "φ"
    string(1) "1"
    int(97)
    int(97)

## Véase también

`IntlChar::totitle`, `IntlChar::toupper`, `mb_strtolower`
