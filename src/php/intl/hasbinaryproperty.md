---
title: IntlChar::hasBinaryProperty
description: Verifica una propiedad Unicode binaria para un punto de código
source_url: https://www.php.net/manual/es/intlchar.hasbinaryproperty.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/hasbinaryproperty.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: e8ac70bf5
order: 40940
---

IntlChar::hasBinaryProperty

Verifica una propiedad Unicode binaria para un punto de código

## Descripción

```php
public static IntlChar::hasBinaryProperty(int $codepoint, int $property): bool
```php

Verifica una propiedad Unicode binaria para un punto de código.

Unicode, en particular en la versión 3.2, define muchas más propiedades que el conjunto original en UnicodeData.txt.

Las API de propiedades están destinadas a reflejar las propiedades Unicode tal como se definen en la base de datos de caracteres Unicode (UCD) y los informes técnicos Unicode (UTR). Para más detalles sobre las propiedades, ver <http://www.unicode.org/ucd/>. Para los nombres de las propiedades Unicode, ver el archivo UCD PropertyAliases.txt.

## Parámetros

`codepoint`  
El valor `int` del punto de código (por ejemplo, `0x2603` para *U+2603 SNOWMAN*), o el carácter codificado como un `string` UTF-8 (por ejemplo, `"\u{2603}"`)

`property`  
La propiedad Unicode a buscar (véanse las constantes `IntlChar::PROPERTY_*`).

## Valores devueltos

Devuelve `true` o `false` según el valor de la propiedad Unicode binaria para `codepoint`. También devuelve `false` si `property` está fuera de alcance o si la versión Unicode no tiene datos para la propiedad en absoluto, o no para este punto de código. Devuelve `null` en caso de fallo.

## Ejemplos

Probar diferentes propiedades

```
    
<?php
var_dump(IntlChar::hasBinaryProperty("A", IntlChar::PROPERTY_ALPHABETIC));
var_dump(IntlChar::hasBinaryProperty("A", IntlChar::PROPERTY_CASE_SENSITIVE));
var_dump(IntlChar::hasBinaryProperty("A", IntlChar::PROPERTY_BIDI_MIRRORED));
var_dump(IntlChar::hasBinaryProperty("[", IntlChar::PROPERTY_ALPHABETIC));
var_dump(IntlChar::hasBinaryProperty("[", IntlChar::PROPERTY_CASE_SENSITIVE));
var_dump(IntlChar::hasBinaryProperty("[", IntlChar::PROPERTY_BIDI_MIRRORED));
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(false)
    bool(false)
    bool(false)
    bool(true)

## Véase también

`IntlChar::getIntPropertyValue`, `IntlChar::getUnicodeVersion`
