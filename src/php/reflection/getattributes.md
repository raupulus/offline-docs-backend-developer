---
title: ReflectionClass::getAttributes
description: Recupera los atributos de una clase
source_url: https://www.php.net/manual/es/reflectionclass.getattributes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getattributes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: fadab82e1
order: 69070
---

ReflectionClass::getAttributes

Recupera los atributos de una clase

## Descripción

```php
public ReflectionClass::getAttributes([string $name], [int $flags]): array
```php

Devuelve todos los atributos declarados en esta clase en forma de un array de objetos `ReflectionAttribute`.

## Parámetros

`name`  
Filtrar los resultados para incluir únicamente las instancias de `ReflectionAttribute` para los atributos correspondientes a este nombre de clase.

`flags`  
Flags para determinar cómo filtrar los resultados, si `name` es proporcionado.

El valor predeterminado es `0` que solo retornará los resultados para los atributos que son de la clase `name`.

La única otra opción disponible es utilizar `ReflectionAttribute::IS_INSTANCEOF`, que utilizará `instanceof` para el filtrado.

## Valores devueltos

Un array de atributos, en forma de objetos de tipo `ReflectionAttribute`.

## Ejemplos

Uso básico de ReflectionClass::getAttributes

```
<?php
#[Attribute]
class Fruit {
}

#[Attribute]
class Rouge {
}

#[Fruit]
#[Rouge]
class Pomme {
}

$class = new ReflectionClass('Pomme');
$attributes = $class->getAttributes();
print_r(array_map(fn($attribute) => $attribute->getName(), $attributes));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Fruit
        [1] => Rouge
    )

Filtrar los resultados por un nombre de clase

```
<?php
#[Attribute]
class Fruit {
}

#[Attribute]
class Rouge {
}

#[Fruit]
#[Rouge]
class Pomme {
}

$class = new ReflectionClass('Pomme');
$attributes = $class->getAttributes('Fruit');
print_r(array_map(fn($attribute) => $attribute->getName(), $attributes));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Fruit
    )

Filtrar los resultados por nombre de clase, con herencia

```
<?php
interface Couleur {
}

#[Attribute]
class Fruit {
}

#[Attribute]
class Rouge implements Couleur {
}

#[Fruit]
#[Rouge]
class Pomme {
}

$class = new ReflectionClass('Pomme');
$attributes = $class->getAttributes(Couleur::class, ReflectionAttribute::IS_INSTANCEOF);
print_r(array_map(fn($attribute) => $attribute->getName(), $attributes));
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Rouge
    )

## Véase también

ReflectionClassConstant::getAttributes, ReflectionFunctionAbstract::getAttributes, ReflectionParameter::getAttributes, ReflectionProperty::getAttributes
