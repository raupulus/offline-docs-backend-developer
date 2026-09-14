---
title: IntlChar::getIntPropertyMaxValue
description: Devuelve el valor máximo para una propiedad Unicode
source_url: https://www.php.net/manual/es/intlchar.getintpropertymaxvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/getintpropertymaxvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40850
---

IntlChar::getIntPropertyMaxValue

Devuelve el valor máximo para una propiedad Unicode

## Descripción

```php
public static IntlChar::getIntPropertyMaxValue(int $property): int
```php

Devuelve el valor máximo para una propiedad Unicode enumerada/entera/binaria.

## Parámetros

`property`  
La propiedad Unicode a buscar (véanse las constantes `IntlChar::PROPERTY_*`).

## Valores devueltos

El valor máximo devuelto por `IntlChar::getIntPropertyValue` para una propiedad Unicode. `<=0` si el selector de propiedad está fuera de alcance.

## Ejemplos

Probar diferentes propiedades

```
    
<?php
var_dump(IntlChar::getIntPropertyMaxValue(IntlChar::PROPERTY_BIDI_CLASS));
var_dump(IntlChar::getIntPropertyMaxValue(IntlChar::PROPERTY_SCRIPT));
var_dump(IntlChar::getIntPropertyMaxValue(IntlChar::PROPERTY_IDEOGRAPHIC));
var_dump(IntlChar::getIntPropertyMaxValue(999999999)); // Un valor inventado
?>

   
```php

El ejemplo anterior mostrará:

        
    int(22)
    int(166)
    int(1)
    int(-1)

## Véase también

`IntlChar::hasBinaryProperty`, `IntlChar::getIntPropertyMinValue`, `IntlChar::getIntPropertyValue`, `IntlChar::getUnicodeVersion`
