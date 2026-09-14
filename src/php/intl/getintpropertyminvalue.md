---
title: IntlChar::getIntPropertyMinValue
description: Devuelve el valor mínimo para una propiedad Unicode
source_url: https://www.php.net/manual/es/intlchar.getintpropertyminvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/getintpropertyminvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40860
---

IntlChar::getIntPropertyMinValue

Devuelve el valor mínimo para una propiedad Unicode

## Descripción

```php
public static IntlChar::getIntPropertyMinValue(int $property): int
```php

Devuelve el valor mínimo para una propiedad Unicode enumerada/entera/binaria.

## Parámetros

`property`  
La propiedad Unicode a buscar (véanse las constantes `IntlChar::PROPERTY_*`).

## Valores devueltos

El valor mínimo devuelto por `IntlChar::getIntPropertyValue` para una propiedad Unicode. `0` si el selector de propiedad está fuera de alcance.

## Ejemplos

Probar diferentes propiedades

```
    
<?php
var_dump(IntlChar::getIntPropertyMinValue(IntlChar::PROPERTY_BIDI_CLASS));
var_dump(IntlChar::getIntPropertyMinValue(IntlChar::PROPERTY_SCRIPT));
var_dump(IntlChar::getIntPropertyMinValue(IntlChar::PROPERTY_IDEOGRAPHIC));
var_dump(IntlChar::getIntPropertyMinValue(999999999)); // Un valor inventado
?>

   
```php

El ejemplo anterior mostrará:

        
    int(0)
    int(0)
    int(0)
    int(0)

## Véase también

`IntlChar::hasBinaryProperty`, `IntlChar::getIntPropertyMaxValue`, `IntlChar::getIntPropertyValue`, `IntlChar::getUnicodeVersion`
