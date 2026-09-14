---
title: IntlChar::isIDPart
description: Verifica si un punto de código es permitido en un identificador
source_url: https://www.php.net/manual/es/intlchar.isidpart.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/isidpart.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 41040
---

IntlChar::isIDPart

Verifica si un punto de código es permitido en un identificador

## Descripción

```php
public static IntlChar::isIDPart(int $codepoint): bool
```php

Determina si el carácter especificado es permitido en un identificador.

`true` para los caracteres de categorías generales "L" (letras), "Nl" (números letras), "Nd" (números decimales), "Mc" y "Mn" (marcas de combinación), "Pc" (signos de puntuación de conexión), y u_isIDIgnorable(c).

> [!NOTE]
> Esto es casi lo mismo que ID_Continue de Unicode (`IntlChar::PROPERTY_ID_CONTINUE`) excepto que Unicode recomienda ignorar Cf que es inferior a `IntlChar::isIDIgnorable`.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

## Valores devueltos

Devuelve `true` si `codepoint` puede aparecer en un identificador, `false` de lo contrario. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes puntos de código

```
    
<?php
var_dump(IntlChar::isIDPart("A"));
var_dump(IntlChar::isIDPart("$"));
var_dump(IntlChar::isIDPart("\n"));
var_dump(IntlChar::isIDPart("\u{2603}"));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(false)
    bool(false)
    bool(false)

## Véase también

`IntlChar::isIDIgnorable`, `IntlChar::isIDStart`, `IntlChar::PROPERTY_ID_CONTINUE`
