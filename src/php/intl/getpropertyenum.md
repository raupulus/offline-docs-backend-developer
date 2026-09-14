---
title: IntlChar::getPropertyEnum
description: Devuelve el valor de la constante de propiedad para un nombre de propiedad
  dado
source_url: https://www.php.net/manual/es/intlchar.getpropertyenum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/getpropertyenum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40890
---

IntlChar::getPropertyEnum

Devuelve el valor de la constante de propiedad para un nombre de propiedad dado

## Descripción

```php
public static IntlChar::getPropertyEnum(string $alias): int
```php

Devuelve el valor de la constante de propiedad para un nombre de propiedad dado, tal como se especifica en el archivo de base de datos Unicode PropertyAliases.txt. Se reconocen las variantes cortas, largas y otras.

Además, esta función mapea los nombres sintéticos "gcm" / "General_Category_Mask" a la propiedad `IntlChar::PROPERTY_GENERAL_CATEGORY_MASK`. Estos nombres no están en PropertyAliases.txt.

Esta función complementa `IntlChar::getPropertyName`.

## Parámetros

`alias`  
El nombre de la propiedad a buscar. El nombre se compara utilizando una "coincidencia flexible" como se describe en PropertyAliases.txt.

## Valores devueltos

Devuelve un valor de constante `IntlChar::PROPERTY_`, o `IntlChar::PROPERTY_INVALID_CODE` si el nombre dado no coincide con ninguna propiedad.

## Ejemplos

Probar diferentes propiedades

```
    
<?php
var_dump(IntlChar::getPropertyEnum('Bidi_Class') === IntlChar::PROPERTY_BIDI_CLASS);
var_dump(IntlChar::getPropertyEnum('script') === IntlChar::PROPERTY_SCRIPT);
var_dump(IntlChar::getPropertyEnum('IDEOGRAPHIC') === IntlChar::PROPERTY_IDEOGRAPHIC);
var_dump(IntlChar::getPropertyEnum('Some made-up string') === IntlChar::PROPERTY_INVALID_CODE);
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(true)
    bool(true)

## Véase también

`IntlChar::getPropertyName`
