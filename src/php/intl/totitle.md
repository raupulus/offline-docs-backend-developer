---
title: IntlChar::totitle
description: Convierte un carácter Unicode en letra de título
source_url: https://www.php.net/manual/es/intlchar.totitle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/totitle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 22583751f
order: 41250
---

IntlChar::totitle

Convierte un carácter Unicode en letra de título

## Descripción

```php
public static IntlChar::totitle(int $codepoint): int
```php

El carácter dado se mapea a su equivalente en letra de título. Si el carácter no tiene equivalente en letra de título, se devuelve el carácter original.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve el Simple_Titlecase_Mapping del punto de código, si está disponible; de lo contrario, devuelve el punto de código mismo. Devuelve `null` en caso de error.

El tipo de retorno es `int` a menos que el punto de código haya sido pasado como un `string` UTF-8, en cuyo caso se devuelve un `string`. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::totitle("Ǆ"));
var_dump(IntlChar::totitle("ǆ"));
var_dump(IntlChar::totitle("Φ"));
var_dump(IntlChar::totitle("φ"));
var_dump(IntlChar::totitle("1"));
var_dump(IntlChar::totitle("ᾳ"));
var_dump(IntlChar::totitle(ord("A")));
?>

   
```php

El ejemplo anterior mostrará:

        
    string(1) "ǅ"
    string(1) "ǅ"
    string(2) "Φ"
    string(2) "φ"
    string(1) "1"
    string(1) "ᾼ"
    int(65)

## Véase también

`IntlChar::tolower`, `IntlChar::toupper`, `IntlChar::istitle`, `mb_convert_case`
