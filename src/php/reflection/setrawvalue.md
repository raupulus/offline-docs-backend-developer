---
title: ReflectionProperty::setRawValue
description: Define la valor de una propiedad, omitiendo un hook de definición si
  está definido
source_url: https://www.php.net/manual/es/reflectionproperty.setrawvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/setrawvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 49ef347a1
order: 71780
---

ReflectionProperty::setRawValue

Define la valor de una propiedad, omitiendo un hook de definición si está definido

## Descripción

```php
public ReflectionProperty::setRawValue(object $object, mixed $value): void
```php

Define la valor de una propiedad, omitiendo un hook `set` si está definido.

## Parámetros

`object`  
El objeto sobre el cual definir la valor de la propiedad.

`value`  
La valor a escribir. Debe ser siempre válida según el tipo de la propiedad.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Si la propiedad es virtual, se lanzará una `Error`, ya que no hay valor bruto a definir.

## Ejemplos

Ejemplo de ReflectionProperty::setRawValue

```
<?php
class Example
{
    public int $age {
        set {
            if ($value <= 0) {
               throw new \InvalidArgumentException();
            }
            $this->age = $value;
        }
    }
}

$example = new Example();

$rClass = new \ReflectionClass(Example::class);
$rProp = $rClass->getProperty('age');

// Esto pasaría por el hook set, y lanzaría una excepción.
$example->age = -2;
try {
    $example->age = -2;
} catch (InvalidArgumentException) {
    print "InvalidArgumentException para establecer la propiedad en -2\n";
}
try {
    $rProp->setValue($example, -2);
} catch (InvalidArgumentException) {
    print "InvalidArgumentException para usar ReflectionProperty::setValue() con -2\n";
}

// Pero esto establecería $age a -2 sin error.
$rProp->setRawValue($example, -2);
echo $example->age;
?>

   
```php

El ejemplo anterior mostrará:

    InvalidArgumentException para establecer la propiedad en -2
    InvalidArgumentException para usar ReflectionProperty::setValue() con -2
    -2

## Véase también

Visibilidad de propiedad asimétrica
