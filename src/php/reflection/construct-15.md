---
title: ReflectionProperty::__construct
description: Construye un nuevo objeto ReflectionProperty
source_url: https://www.php.net/manual/es/reflectionproperty.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionproperty/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: c1aba02c4
order: 71440
---

ReflectionProperty::\_\_construct

Construye un nuevo objeto ReflectionProperty

## Descripción

```php
public ReflectionProperty::__construct(object $class, string $property)
```php

## Parámetros

`class`  
Puede ser un string que contenga el nombre de la clase a introspeccionar, o un objeto.

`property`  
El nombre de la propiedad a reflejar.

## Errores/Excepciones

Intentar recuperar o definir el valor de una propiedad privada o protegida de una clase emitirá una excepción.

## Ejemplos

Ejemplo con ReflectionProperty::\_\_construct

```
<?php

class Str
{
    public $length  = 5;
}

// Creación de una instancia de la clase ReflectionProperty
$prop = new ReflectionProperty('Str', 'length');

// Mostrar algunas informaciones
printf(
    "===> La%s%s%s%s propiedad '%s' (que fue %s)\n" .
    "     con los modificadores %s\n",
        $prop->isPublic() ? ' pública' : '',
        $prop->isPrivate() ? ' privada' : '',
        $prop->isProtected() ? ' protegida' : '',
        $prop->isStatic() ? ' estática' : '',
        $prop->getName(),
        $prop->isDefault() ? 'declarada en tiempo de compilación' : 'creada en tiempo de ejecución',
        var_export(Reflection::getModifierNames($prop->getModifiers()), true)
);

// Creación de una instancia de Str
$obj= new Str();

// Obtiene el valor actual
printf("---> Value is: ");
var_dump($prop->getValue($obj));

// Modifica el valor
$prop->setValue($obj, 10);
printf("---> Setting value to 10, new value is: ");
var_dump($prop->getValue($obj));

// Muestra el objeto
var_dump($obj);

?>

    
```php

Resultado del ejemplo anterior es similar a:

    ===> La pública propiedad 'length' (que fue declarada en tiempo de compilación)
         con los modificadores array (
      0 => 'public',
    )
    ---> Value is: int(5)
    ---> Setting value to 10, new value is: int(10)
    object(Str)#2 (1) {
      ["length"]=>
      int(10)
    }

Obtención de un valor desde una propiedad privada o protegida utilizando la clase `ReflectionProperty`

```
<?php

class Foo
{
    public $x = 1;
    protected $y = 2;
    private $z = 3;
}

$obj = new Foo;

$prop = new ReflectionProperty('Foo', 'y');
$prop->setAccessible(true);
var_dump($prop->getValue($obj)); // int(2)

$prop = new ReflectionProperty('Foo', 'z');
$prop->setAccessible(true);
var_dump($prop->getValue($obj)); // int(2)

?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(2)
    int(3)

## Véase también

ReflectionProperty::getName, [Los constructores](#language.oop5.decon.constructor)
