---
title: ReflectionClass::getStaticPropertyValue
description: Obtiene el valor de una propiedad estática
source_url: https://www.php.net/manual/es/reflectionclass.getstaticpropertyvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionclass/getstaticpropertyvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: 8a910daad
order: 69330
---

ReflectionClass::getStaticPropertyValue

Obtiene el valor de una propiedad estática

## Descripción

```php
public ReflectionClass::getStaticPropertyValue(string $name, [mixed $default]): mixed
```php

Obtiene el valor de una propiedad estática de esta clase.

## Parámetros

`name`  
El nombre de la propiedad estática para la que devolver un valor.

`default`  
Un valor predeterminado a devolver en caso de que la clase no declare propiedades estáticas con el `name` dado. Si la propiedad no existe y se omite este argumento, se lanza una `ReflectionException`.

## Valores devueltos

El valor de la propiedad estática.

## Ejemplos

Uso básico de ReflectionClass::getStaticPropertyValue

```
<?php
class Apple {
    public static $color = 'Rojo';
}

$class = new ReflectionClass('Apple');
var_dump($class->getStaticPropertyValue('color'));
?>

    
```php

El ejemplo anterior mostrará:

    string(4) "Rojo"

## Véase también

ReflectionClass::getStaticProperties, ReflectionClass::setStaticPropertyValue
