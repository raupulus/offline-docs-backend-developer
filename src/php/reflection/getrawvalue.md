---
title: ReflectionProperty::getRawValue
description: Devuelve el valor de la propiedad, evitando un hook get si está definido
source_url: https://www.php.net/manual/es/reflectionproperty.getrawvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/getrawvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 79c0572a5
order: 71540
---

ReflectionProperty::getRawValue

Devuelve el valor de la propiedad, evitando un hook get si está definido

## Descripción

```php
public ReflectionProperty::getRawValue(object $object): mixed
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Devuelve el valor de una propiedad, evitando un hook `get` si está definido.

## Parámetros

`object`  
El objeto a partir del cual recuperar un valor.

## Valores devueltos

El valor almacenado de la propiedad, evitando un hook `get` si está definido.

## Errores/Excepciones

Si la propiedad es virtual, se lanzará una `Error`, ya que no hay valor bruto que recuperar.

## Ejemplos

Ejemplo de ReflectionProperty::getRawValue

```
<?php

class Example
{
    public string $tag {
        get => strtolower($this->tag);
    }
}

$example = new Example();
$example->tag = 'PHP';

$rClass = new \ReflectionClass(Example::class);
$rProp = $rClass->getProperty('tag');

// Esto pasaría por el hook get, produciendo "php".
echo $example->tag, PHP_EOL;
echo $rProp->getValue($example), PHP_EOL;

// Pero esto evitaría el hook y produciría "PHP"
echo $rProp->getRawValue($example);

?>

   
```php

El ejemplo anterior mostrará:

    php
    php
    PHP

## Véase también

Visibilidad de propiedad asimétrica
