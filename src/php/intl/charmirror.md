---
title: IntlChar::charMirror
description: Devuelve el carácter "imagen-espejo" para un punto de código
source_url: https://www.php.net/manual/es/intlchar.charmirror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/charmirror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40720
---

IntlChar::charMirror

Devuelve el carácter "imagen-espejo" para un punto de código

## Descripción

```php
public static IntlChar::charMirror(int $codepoint): int
```php

Vincula el carácter especificado a un carácter "imagen-espejo".

Para los caracteres con la propiedad *Bidi_Mirrored*, las implementaciones a veces necesitan una correspondencia "pobre" hacia otro punto de código Unicode (code point) de tal manera que el glifo por defecto pueda servir como glifo espejo del glifo por defecto del carácter especificado. Esto es útil para la conversión de texto hacia y desde páginas de códigos con un orden visual, y para los displays sin capacidades de selección de glifo.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve otro punto de código Unicode que puede servir como sustituto imagen-espejo, o `codepoint` mismo si no hay correspondencia o si `codepoint` no tiene la propiedad *Bidi_Mirrored*.

El tipo de retorno es `int` a menos que el punto de código haya sido pasado como un `string` UTF-8, en cuyo caso se devuelve un `string`. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::charMirror("A"));
var_dump(IntlChar::charMirror("<"));
var_dump(IntlChar::charMirror("("));
?>

   
```php

El ejemplo anterior mostrará:

        
    string(1) "A"
    string(1) ">"
    string(2) ")"

## Véase también

`IntlChar::isMirrored`, `IntlChar::PROPERTY_BIDI_MIRRORED`
