---
title: IntlChar::getBidiPairedBracket
description: Devuelve el carácter de paréntesis emparejado para un punto de código
source_url: https://www.php.net/manual/es/intlchar.getbidipairedbracket.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/getbidipairedbracket.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 454c84c4f
order: 40810
---

IntlChar::getBidiPairedBracket

Devuelve el carácter de paréntesis emparejado para un punto de código

## Descripción

```php
public static IntlChar::getBidiPairedBracket(int $codepoint): int
```php

Mapea el carácter especificado a su carácter de paréntesis emparejado.

Para `IntlChar::PROPERTY_BIDI_PAIRED_BRACKET_TYPE !== IntlChar::BPT_NONE`, esto equivale a `IntlChar::charMirror`.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve el punto de código del paréntesis emparejado, o `codepoint` mismo si no hay mapeo. Devuelve `null` en caso de error.

El tipo de retorno es `int` a menos que el punto de código haya sido pasado como un `string` UTF-8, en cuyo caso se devuelve un `string`. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::getBidiPairedBracket(91));
var_dump(IntlChar::getBidiPairedBracket('['));
?>

   
```php

El ejemplo anterior mostrará:

        
    int(93)
    string(1) "]"

## Notas

> [!NOTE]
> Este método está disponible desde la versión 52 de ICU.

## Véase también

`IntlChar::charMirror`, `IntlChar::PROPERTY_BIDI_PAIRED_BRACKET`, `IntlChar::PROPERTY_BIDI_PAIRED_BRACKET_TYPE`
