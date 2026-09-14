---
title: IntlChar::getPropertyValueName
description: Devuelve el nombre Unicode para un valor de propiedad
source_url: https://www.php.net/manual/es/intlchar.getpropertyvaluename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/getpropertyvaluename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 40920
---

IntlChar::getPropertyValueName

Devuelve el nombre Unicode para un valor de propiedad

## Descripción

```php
public static IntlChar::getPropertyValueName(int $property, int $value, [int $type]): string
```php

Devuelve el nombre Unicode para un valor de propiedad dado, tal como se indica en el archivo de base de datos Unicode PropertyValueAliases.txt.

> [!NOTE]
> Algunos nombres en PropertyValueAliases.txt solo pueden obtenerse utilizando `IntlChar::PROPERTY_GENERAL_CATEGORY_MASK`, no `IntlChar::PROPERTY_GENERAL_CATEGORY`. Estos incluyen: "C" / "Otro", "L" / "Letra", "LC" / "Letra_Mayúscula", "M" / "Marca", "N" / "Número", "P" / "Puntuación", "S" / "Símbolo", "Z" / "Separador"

## Parámetros

`property`  
La propiedad Unicode a buscar (véanse las constantes `IntlChar::PROPERTY_*`).

Si está fuera de alcance, o si este método no funciona con el valor dado, se devuelve `false`.

`value`  
El selector para un valor de la propiedad dada. Si está fuera de alcance, se devuelve `false`.

En general, los valores válidos van desde `0` hasta un máximo. Hay algunas excepciones: `IntlChar::PROPERTY_BLOCK` los valores comienzan con el valor no nulo `IntlChar::BLOCK_CODE_BASIC_LATIN`, `IntlChar::PROPERTY_CANONICAL_COMBINING_CLASS` los valores no son contiguos y van de 0 a 240.

`type`  
El selector para el nombre a obtener. Si está fuera de alcance, se devuelve `false`.

Todos los valores tienen un nombre largo. La mayoría tienen un nombre corto, pero algunos no. Unicode permite nombres adicionales; si están presentes, se devolverán añadiendo 1, 2, etc. a `IntlChar::LONG_PROPERTY_NAME`.

## Valores devueltos

Devuelve el nombre, o `false` si `property` o `type` están fuera de alcance. Devuelve `null` en caso de error.

Si un `type` dado devuelve `false`, entonces todos los valores mayores de `type` devolverán `false`, con una excepción: si `false` se devuelve para `IntlChar::SHORT_PROPERTY_NAME`, entonces `IntlChar::LONG_PROPERTY_NAME` (y más) aún puede devolver un valor no-`false`.

## Ejemplos

Probar diferentes propiedades

```
    
<?php
var_dump(IntlChar::getPropertyValueName(IntlChar::PROPERTY_BLOCK, IntlChar::BLOCK_CODE_GREEK));
var_dump(IntlChar::getPropertyValueName(IntlChar::PROPERTY_BLOCK, IntlChar::BLOCK_CODE_GREEK, IntlChar::SHORT_PROPERTY_NAME));
var_dump(IntlChar::getPropertyValueName(IntlChar::PROPERTY_BLOCK, IntlChar::BLOCK_CODE_GREEK, IntlChar::LONG_PROPERTY_NAME));
var_dump(IntlChar::getPropertyValueName(IntlChar::PROPERTY_BLOCK, IntlChar::BLOCK_CODE_GREEK, IntlChar::LONG_PROPERTY_NAME + 1));
?>

   
```php

El ejemplo anterior mostrará:

        
    string(16) "Greek_And_Coptic"
    string(5) "Greek"
    string(16) "Greek_And_Coptic"
    bool(false)
