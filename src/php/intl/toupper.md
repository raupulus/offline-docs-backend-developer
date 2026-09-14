---
title: IntlChar::toupper
description: Convierte un carácter Unicode a mayúscula
source_url: https://www.php.net/manual/es/intlchar.toupper.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/toupper.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41260
---

IntlChar::toupper

Convierte un carácter Unicode a mayúscula

## Descripción

```php
public static IntlChar::toupper(int $codepoint): int
```php

El carácter dado se mapea a su equivalente en mayúscula. Si el carácter no tiene equivalente en mayúscula, se devuelve el carácter original.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve el Simple_Uppercase_Mapping del punto de código, si está disponible; de lo contrario, el punto de código mismo.

El tipo de retorno es `int` a menos que el punto de código haya sido pasado como un `string` UTF-8, en cuyo caso se devuelve un `string`. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::toupper("A"));
var_dump(IntlChar::toupper("a"));
var_dump(IntlChar::toupper("Φ"));
var_dump(IntlChar::toupper("φ"));
var_dump(IntlChar::toupper("1"));
var_dump(IntlChar::toupper(ord("A")));
var_dump(IntlChar::toupper(ord("a")));
?>

   
```php

El ejemplo anterior mostrará:

        
    string(1) "A"
    string(1) "A"
    string(2) "Φ"
    string(2) "Φ"
    string(1) "1"
    int(65)
    int(65)

## Véase también

`IntlChar::tolower`, `IntlChar::totitle`, `mb_strtoupper`
