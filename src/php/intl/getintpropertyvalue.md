---
title: IntlChar::getIntPropertyValue
description: Devuelve el valor de una propiedad Unicode para un punto de código
source_url: https://www.php.net/manual/es/intlchar.getintpropertyvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/getintpropertyvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40870
---

IntlChar::getIntPropertyValue

Devuelve el valor de una propiedad Unicode para un punto de código

## Descripción

```php
public static IntlChar::getIntPropertyValue(int $codepoint, int $property): int
```php

Devuelve el valor de una propiedad Unicode enumerada o entera para un punto de código. Asimismo, devuelve los valores de propiedad binaria y de máscara.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

`property`  
La propiedad Unicode a buscar (véanse las constantes `IntlChar::PROPERTY_*`).

## Valores devueltos

Devuelve el valor numérico que es directamente el valor de la propiedad o, para las propiedades enumeradas, corresponde al valor numérico de la constante enumerada del tipo de enumeración de valor de propiedad respectiva. Devuelve `null` en caso de error.

Devuelve `0` o `1` (para `false`/`true`) para las propiedades binarias Unicode.

Devuelve una máscara de bits para las propiedades de máscara.

Devuelve `0` si `property` está fuera de alcance o si la versión Unicode no tiene datos para la propiedad, o no para este punto de código.

## Ejemplos

Probar diferentes propiedades

```
    
<?php
var_dump(IntlChar::getIntPropertyValue("A", IntlChar::PROPERTY_ALPHABETIC) === 1);
var_dump(IntlChar::getIntPropertyValue("[", IntlChar::PROPERTY_BIDI_MIRRORED) === 1);
var_dump(IntlChar::getIntPropertyValue("Φ", IntlChar::PROPERTY_BLOCK) === IntlChar::BLOCK_CODE_GREEK);
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(true)

## Véase también

`IntlChar::hasBinaryProperty`, `IntlChar::getIntPropertyMinValue`, `IntlChar::getIntPropertyMaxValue`, `IntlChar::getUnicodeVersion`
