---
title: ReflectionProperty::isVirtual
description: Determina si la propiedad es virtual
source_url: https://www.php.net/manual/es/reflectionproperty.isvirtual.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/isvirtual.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: a16ad380e
order: 71760
---

ReflectionProperty::isVirtual

Determina si la propiedad es virtual

## Descripción

```php
public ReflectionProperty::isVirtual(): bool
```php

Determina si una propiedad es virtual.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si la propiedad es virtual, de lo contrario `false`.

## Ejemplos

ReflectionProperty::isVirtual ejemplo

```
<?php
class Example
{
    // Ninguno de los hooks hace referencia a la propiedad,
    // por lo que es virtual.
    public string $name { get => "Nombre aquí"; }

    // Este hook hace referencia a la propiedad por su nombre,
    // por lo que no es virtual.
    public int $age {
        set {
            if ($value <= 0) {
               throw new \InvalidArgumentException();
            }
            $this->age = $value;
        }
    }

    // Las propiedades no hookeadas siempre son no virtuales.
    public string $job;
}

$rClass = new \ReflectionClass(Example::class);

var_dump($rClass->getProperty('name')->isVirtual());
var_dump($rClass->getProperty('age')->isVirtual());
var_dump($rClass->getProperty('job')->isVirtual());
?>

   
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    bool(false)

## Véase también

Propiedad virtual
