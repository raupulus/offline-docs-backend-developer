---
title: ReflectionProperty::getDocComment
description: Recupera el comentario de documentación de una propiedad
source_url: https://www.php.net/manual/es/reflectionproperty.getdoccomment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/getdoccomment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 71490
---

ReflectionProperty::getDocComment

Recupera el comentario de documentación de una propiedad

## Descripción

```php
public ReflectionProperty::getDocComment(): string
```php

Recupera el comentario de documentación de una propiedad.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El comentario de documentación si existe, de lo contrario `false`.

## Ejemplos

ReflectionProperty::getDocComment ejemplo

```
<?php
class Str
{
    /**
     * @var int  El tamaño de la cadena de caracteres
     */
    public $length = 5;
}

$prop = new ReflectionProperty('Str', 'length');

var_dump($prop->getDocComment());

?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(53) "/**
         * @var int  El tamaño de la cadena de caracteres
         */"

Múltiples declaraciones de propiedades

Si múltiples declaraciones de propiedades son precedidas por un único comentario de documentación, el comentario de documentación hace referencia únicamente a la primera propiedad.

```
<?php
class Foo
{
    /** @var string */
    public $a, $b;
}
$class = new \ReflectionClass('Foo');
foreach ($class->getProperties() as $property) {
    echo $property->getName() . ': ' . var_export($property->getDocComment(), true) . PHP_EOL;
}
?>

    
```php

El ejemplo anterior mostrará:

    a: '/** @var string */'
    b: false

## Véase también

ReflectionProperty::getModifiers, ReflectionProperty::getName, ReflectionProperty::getValue
