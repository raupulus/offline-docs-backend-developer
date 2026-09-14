---
title: ReflectionParameter::getAttributes
description: Devuelve los atributos
source_url: https://www.php.net/manual/es/reflectionparameter.getattributes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionparameter/getattributes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 54c9db669
order: 71230
---

ReflectionParameter::getAttributes

Devuelve los atributos

## Descripción

```php
public ReflectionParameter::getAttributes([string $name], [int $flags]): array
```php

Devuelve todos los atributos declarados en este parámetro en forma de un array de objetos `ReflectionAttribute`.

## Parámetros

`name`  
Filtrar los resultados para incluir únicamente las instancias de `ReflectionAttribute` para los atributos correspondientes a este nombre de clase.

`flags`  
Flags para determinar cómo filtrar los resultados, si `name` es proporcionado.

El valor predeterminado es `0` que solo retornará los resultados para los atributos que son de la clase `name`.

La única otra opción disponible es utilizar `ReflectionAttribute::IS_INSTANCEOF`, que utilizará `instanceof` para el filtrado.

## Valores devueltos

Un array de atributos, en forma de objetos `ReflectionAttribute`.

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

function fruitBasket(
   #[Fruit]
   #[Red]
   string $apple
) { }

$reflection = new ReflectionFunction('fruitBasket');
$parameter = $reflection->getParameters()[0];
$attributes = $parameter->getAttributes();
print_r(array_map(fn($attribute) => $attribute->getName(), $attributes));
?>

    
```php

El ejemplo anterior mostrará:

         
    Array
    (
        [0] => Fruit
        [1] => Red
    )

Resultados filtrados por nombre de clase

```
     
<?php
#[Attribute]
class Fruit {
}

#[Attribute]
class Red {
}

function fruitBasket(
   #[Fruit]
   #[Red]
   string $apple
) { }

$reflection = new ReflectionFunction('fruitBasket');
$parameter = $reflection->getParameters()[0];
$attributes = $parameter->getAttributes('Fruit');
print_r(array_map(fn($attribute) => $attribute->getName(), $attributes));
?>

    
```php

El ejemplo anterior mostrará:

         
    Array
    (
        [0] => Fruit
    )

Resultados filtrados por nombre de clase, con herencia

```
     
<?php
interface Color {
}

#[Attribute]
class Fruit {
}

#[Attribute]
class Red implements Color {
}

function fruitBasket(
   #[Fruit]
   #[Red]
   string $apple
) { }

$reflection = new ReflectionFunction('fruitBasket');
$parameter = $reflection->getParameters()[0];
$attributes = $parameter->getAttributes('Color', ReflectionAttribute::IS_INSTANCEOF);
print_r(array_map(fn($attribute) => $attribute->getName(), $attributes));
?>

    
```php

El ejemplo anterior mostrará:

         
    Array
    (
        [0] => Red
    )

## Véase también

ReflectionClass::getAttributes, ReflectionClassConstant::getAttributes, ReflectionFunctionAbstract::getAttributes, ReflectionProperty::getAttributes
