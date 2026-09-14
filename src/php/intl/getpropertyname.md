---
title: IntlChar::getPropertyName
description: Devuelve el nombre Unicode de una propiedad
source_url: https://www.php.net/manual/es/intlchar.getpropertyname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/getpropertyname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 40900
---

IntlChar::getPropertyName

Devuelve el nombre Unicode de una propiedad

## Descripción

```php
public static IntlChar::getPropertyName(int $property, [int $type]): string
```php

Devuelve el nombre Unicode de una propiedad dada, tal como se indica en el archivo de base de datos Unicode PropertyAliases.txt.

Además, esta función mapea la propiedad `IntlChar::PROPERTY_GENERAL_CATEGORY_MASK` a los nombres sintéticos "gcm" / "General_Category_Mask". Estos nombres no están en PropertyAliases.txt.

Esta función complementa `IntlChar::getPropertyEnum`.

## Parámetros

`property`  
La propiedad Unicode a buscar (véanse las constantes `IntlChar::PROPERTY_*`).

`IntlChar::PROPERTY_INVALID_CODE` no debe ser utilizado. Además, si `property` está fuera de rango, `false` es devuelto.

`type`  
El selector para el nombre a obtener. Si está fuera de rango, `false` es devuelto.

Todas las propiedades tienen un nombre largo. La mayoría tienen un nombre corto, pero algunas no lo tienen. Unicode permite nombres adicionales; si están presentes, serán devueltos añadiendo 1, 2, etc. a `IntlChar::LONG_PROPERTY_NAME`.

## Valores devueltos

Devuelve el nombre, o `false` si `property` o `type` están fuera de rango.

Si un `type` dado devuelve `false`, entonces todos los valores más grandes de `type` devolverán `false`, con una excepción: si `false` es devuelto para `IntlChar::SHORT_PROPERTY_NAME`, entonces `IntlChar::LONG_PROPERTY_NAME` (y más) puede aún devolver un valor no-`false`.

## Ejemplos

Probar diferentes propiedades

```
    
<?php
var_dump(IntlChar::getPropertyName(IntlChar::PROPERTY_BIDI_CLASS));
var_dump(IntlChar::getPropertyName(IntlChar::PROPERTY_BIDI_CLASS, IntlChar::SHORT_PROPERTY_NAME));
var_dump(IntlChar::getPropertyName(IntlChar::PROPERTY_BIDI_CLASS, IntlChar::LONG_PROPERTY_NAME));
var_dump(IntlChar::getPropertyName(IntlChar::PROPERTY_BIDI_CLASS, IntlChar::LONG_PROPERTY_NAME + 1));
?>

   
```php

El ejemplo anterior mostrará:

        
    string(10) "Bidi_Class"
    string(2) "bc"
    string(10) "Bidi_Class"
    bool(false)

## Véase también

`IntlChar::getPropertyEnum`
