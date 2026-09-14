---
title: IntlChar::istitle
description: Verifica si un punto de código es una letra en título
source_url: https://www.php.net/manual/es/intlchar.istitle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/istitle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: a37831eed
order: 41150
---

IntlChar::istitle

Verifica si un punto de código es una letra en título

## Descripción

```php
public static IntlChar::istitle(int $codepoint): bool
```php

Determina si el punto de código especificado es una letra en título.

`true` para la categoría general "Lt" (letra en título).

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` es una letra en título, `false` en caso contrario. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
// Letra latina en mayúscula Dz con caron U+01C4
var_dump(IntlChar::istitle("Ǆ"));
// Letra latina en mayúscula D con letra pequeña Z con caron U+01C5
var_dump(IntlChar::istitle("ǅ"));
// Letra latina en minúscula Dz con caron U+01C6
var_dump(IntlChar::istitle("ǆ"));

// Letra griega en mayúscula Alpha con prosgegrammeni U+1FBC
var_dump(IntlChar::istitle("ᾼ"));
// Letra griega en minúscula Alpha con prosgegrammeni U+1FBE
var_dump(IntlChar::istitle("ᾳ"));
// Letra griega en mayúscula Alpha U+0391
var_dump(IntlChar::istitle("Α"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(false)
    bool(true)
    bool(false)
    bool(true)
    bool(false)
    bool(false)

## Véase también

`IntlChar::isupper`, `IntlChar::islower`, `IntlChar::totitle`
