---
title: ReflectionConstant::getAttributes
description: Obtiene los atributos
source_url: https://www.php.net/manual/es/reflectionconstant.getattributes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionconstant/getattributes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: 543f98255
order: 69890
---

ReflectionConstant::getAttributes

Obtiene los atributos

## Descripción

```php
public ReflectionConstant::getAttributes([string $name], [int $flags]): array
```php

Devuelve todos los atributos declarados en esta constante global como un array de `ReflectionAttribute`.

## Parámetros

`name`  
Filtrar los resultados para incluir únicamente las instancias de `ReflectionAttribute` para los atributos correspondientes a este nombre de clase.

`flags`  
Flags para determinar cómo filtrar los resultados, si `name` es proporcionado.

El valor predeterminado es `0` que solo retornará los resultados para los atributos que son de la clase `name`.

La única otra opción disponible es utilizar `ReflectionAttribute::IS_INSTANCEOF`, que utilizará `instanceof` para el filtrado.

## Valores devueltos

Array de atributos, como objetos `ReflectionAttribute`.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.5.0   | Este método fue introducido. |

## Ejemplos

Uso básico

```
<?php
#[Attribute]
class Fruit {
}

#[Attribute]
class Red {
}

#[Fruit]
#[Red]
const APPLE = 'apple';

$constant = new ReflectionConstant('APPLE');
$attributes = $constant->getAttributes();
print_r(array_map(fn($attribute) => $attribute->getName(), $attributes));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Fruit
        [1] => Red
    )

## Véase también

ReflectionClass::getAttributes

ReflectionClassConstant::getAttributes

ReflectionFunctionAbstract::getAttributes

ReflectionProperty::getAttributes
