---
title: ArrayObject::setFlags
description: Configura las opciones de comportamiento
source_url: https://www.php.net/manual/es/arrayobject.setflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/arrayobject/setflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 52e3799c4
order: 81520
---

ArrayObject::setFlags

Configura las opciones de comportamiento

## Descripción

```php
public ArrayObject::setFlags(int $flags): void
```php

Configura las opciones que modifican el comportamiento de los objetos `ArrayObject`.

## Parámetros

`flags`  
El nuevo comportamiento de `ArrayObject`. Esto puede ser un campo de bits o constantes nombradas. El uso de las constantes es altamente recomendado, para asegurar la compatibilidad con futuras versiones.

Las opciones de comportamiento disponibles se listan a continuación. Su significado se describe en las [constantes predefinidas](#arrayobject.constants).

| Valor | Constante |
|----|----|
| 1 | [ArrayObject::STD_PROP_LIST](#arrayobject.constants.std-prop-list) |
| 2 | [ArrayObject::ARRAY_AS_PROPS](#arrayobject.constants.array-as-props) |

Opciones de comportamiento de `ArrayObject`

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `ArrayObject::setFlags`

```
<?php
// Lista de frutas
$fruits = array("citrons" => 1, "oranges" => 4, "bananes" => 5, "pommes" => 10);

$fruitsArrayObject = new ArrayObject($fruits);

// Uso de las claves del array como propiedades
var_dump($fruitsArrayObject->citrons);
// Configura el array para que las claves puedan usarse como propiedades
$fruitsArrayObject->setFlags(ArrayObject::ARRAY_AS_PROPS);
// Intento nuevamente
var_dump($fruitsArrayObject->citrons);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Warning: Undefined property: ArrayObject::$lemons in ...
    NULL
    int(1)
