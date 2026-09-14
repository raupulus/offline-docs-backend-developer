---
title: IntlChar::getPropertyValueEnum
description: Devuelve el valor de propiedad para un nombre de valor dado
source_url: https://www.php.net/manual/es/intlchar.getpropertyvalueenum.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlchar/getpropertyvalueenum.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40910
---

IntlChar::getPropertyValueEnum

Devuelve el valor de propiedad para un nombre de valor dado

## Descripción

```php
public static IntlChar::getPropertyValueEnum(int $property, string $name): int
```php

Devuelve el valor de propiedad entero para un nombre de valor dado, tal como se especifica en el archivo de base de datos Unicode PropertyValueAliases.txt. Las variantes cortas, largas y otras son reconocidas.

> [!NOTE]
> Algunos nombres en PropertyValueAliases.txt solo serán reconocidos con `IntlChar::PROPERTY_GENERAL_CATEGORY_MASK`, no `IntlChar::PROPERTY_GENERAL_CATEGORY`. Estos incluyen: "C" / "Otro", "L" / "Letra", "LC" / "Letra_Mayúscula", "M" / "Marca", "N" / "Número", "P" / "Puntuación", "S" / "Símbolo", "Z" / "Separador"

## Parámetros

`property`  
La propiedad Unicode a buscar (véanse las constantes `IntlChar::PROPERTY_*`).

Si está fuera de alcance, o si este método no funciona con el valor dado, `IntlChar::PROPERTY_INVALID_CODE` es devuelto.

`name`  
El valor de nombre a buscar. El nombre es comparado utilizando una "coincidencia floja" como se describe en PropertyValueAliases.txt.

## Valores devueltos

Devuelve el valor entero correspondiente, o `IntlChar::PROPERTY_INVALID_CODE` si el nombre dado no coincide con ningún valor de la propiedad dada, o si la propiedad es inválida.

## Ejemplos

Probar diferentes propiedades

```
    
<?php
var_dump(IntlChar::getPropertyValueEnum(IntlChar::PROPERTY_BLOCK, 'greek') === IntlChar::BLOCK_CODE_GREEK);
var_dump(IntlChar::getPropertyValueEnum(IntlChar::PROPERTY_BIDI_CLASS, 'RIGHT_TO_LEFT') === IntlChar::CHAR_DIRECTION_RIGHT_TO_LEFT);
var_dump(IntlChar::getPropertyValueEnum(IntlChar::PROPERTY_BIDI_CLASS, 'some made-up string') === IntlChar::PROPERTY_INVALID_CODE);
var_dump(IntlChar::getPropertyValueEnum(123456789, 'RIGHT_TO_LEFT') === IntlChar::PROPERTY_INVALID_CODE);
?>

   
```php

El ejemplo anterior mostrará:

        
    bool(true)
    bool(true)
    bool(true)
    bool(true)
