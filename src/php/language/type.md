---
title: Operadores de tipos
source_url: https://www.php.net/manual/es/language.operators.type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 16934048f
order: 2770
---

## Operadores de tipos

`instanceof` se utiliza para determinar si una variable PHP es un objeto instanciado de una cierta [clase](#language.oop5.basic.class):

Uso de `instanceof` con clases

```php
<?php
class MiClase
{
}
class NoMiClase
{
}
$a = new MiClase;

var_dump($a instanceof MiClase);
var_dump($a instanceof NoMiClase);
?>

   
```

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

`instanceof` también puede ser utilizado para determinar si una variable es un objeto instanciado de una clase que hereda de una clase padre:

Uso de `instanceof` con clases heredadas

```php
<?php
class ClasePadre
{
}
class MiClase extends ClasePadre
{
}
$a = new MiClase;

var_dump($a instanceof MiClase);
var_dump($a instanceof ClasePadre);
?>
     
   
```

El ejemplo anterior mostrará:

    bool(true)
    bool(true)

Para verificar si un objeto *no es* una instancia de una clase, el [operador lógico `not`](#language.operators.logical) puede ser utilizado.

Uso de `instanceof` para verificar que el objeto *no es* una instancia de la clase

```php
<?php
class MiClase
{
}
$a = new MiClase;
var_dump(!($a instanceof stdClass));
?>

   
```

El ejemplo anterior mostrará:

    bool(true)

Y finalmente, `instanceof` puede ser utilizado para determinar si una variable es un objeto instanciado de una clase que implementa una [interface](#language.oop5.interfaces):

Uso de `instanceof` para una interface

```php
<?php
interface MiInterface
{
}
class MiClase implements MiInterface
{
}
$a = new MiClase;

var_dump($a instanceof MiClase);
var_dump($a instanceof MiInterface);
?>

   
```

El ejemplo anterior mostrará:

    bool(true)
    bool(true)

Aunque `instanceof` se utiliza habitualmente con un nombre de clase literal, también puede ser utilizado con otro objeto o una cadena representando una variable:

Uso de `instanceof` con otras variables

```php
<?php
interface MiInterface
{
}
class MiClase implements MiInterface
{
}
$a = new MiClase;
$b = new MiClase;
$c = 'MiClase';
$d = 'NoMiClase';
var_dump($a instanceof $b); // $b es un objeto de la clase MiClase
var_dump($a instanceof $c); // $c es una cadena 'MiClase'
var_dump($a instanceof $d); // $d es una cadena 'NoMiClase'
?>

   
```

El ejemplo anterior mostrará:

    bool(true)
    bool(true)
    bool(false)

instanceof no lanza ningún error si la variable probada no es un objeto, simplemente devolverá `false`. Sin embargo, las constantes no están permitidas.

Uso de `instanceof` para probar otras variables

```php
<?php
$a = 1;
$b = NULL;
$c = fopen('/tmp/', 'r');
var_dump($a instanceof stdClass); // $a es un entero
var_dump($b instanceof stdClass); // $b vale NULL
var_dump($c instanceof stdClass); // $c es un recurso
var_dump(FALSE instanceof stdClass);
?>

   
```

El ejemplo anterior mostrará:

    bool(false)
    bool(false)
    bool(false)
    PHP Fatal error:  instanceof espera una instancia de objeto, constante dada

A partir de PHP 7.3.0, las constantes están permitidas en el lado izquierdo del operador `instanceof`.

Uso de `instanceof` para probar constantes

```php
<?php
var_dump(FALSE instanceof stdClass);
?>

   
```

Resultado del ejemplo anterior en PHP 7.3:

    bool(false)

A partir de PHP 8.0.0, `instanceof` puede ahora ser utilizado con expresiones arbitrarias. La expresión debe estar entre paréntesis y producir una `string`.

Uso de `instanceof` con una expresión arbitraria

```php
<?php

class ClaseA extends \stdClass {}
class ClaseB extends \stdClass {}
class ClaseC extends ClaseB {}
class ClaseD extends ClaseA {}

function obtenerAlgunaClase(): string
{
    return ClaseA::class;
}

var_dump(new ClaseA instanceof ('std' . 'Class'));
var_dump(new ClaseB instanceof ('Class' . 'B'));
var_dump(new ClaseC instanceof ('Class' . 'A'));
var_dump(new ClaseD instanceof (obtenerAlgunaClase()));
?>

   
```

Resultado del ejemplo anterior en PHP 8:

    bool(true)
    bool(true)
    bool(false)
    bool(true)

El operador `instanceof` tiene una variante funcional con la función `is_a`.

## Véase también

`get_class`, `is_a`
