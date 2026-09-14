---
title: constant
description: Retorna el valor de una constante
source_url: https://www.php.net/manual/es/function.constant.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/constant.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 6c3091b54
order: 47020
---

constant

Retorna el valor de una constante

## Descripción

```php
constant(string $name): mixed
```php

Retorna el valor de la constante `name`.

`constant` es útil cuando se debe leer el valor de una constante, pero su nombre solo se conoce durante la ejecución del script. Por ejemplo, este nombre puede ser el resultado de una función.

Esta función también funciona con las [constantes de clase](#language.oop5.constants) y [tipos enum](#language.types.enumerations).

## Parámetros

`name`  
El nombre de la constante.

## Valores devueltos

Retorna el valor de la constante.

## Errores/Excepciones

Si la constante no está definida, se lanza una excepción `Error`. Anteriormente a PHP 8.0.0, se emitía un error de nivel `E_WARNING` en este caso.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Si la constante no está definida, `constant` ahora lanza una excepción `Error`; anteriormente se emitía un `E_WARNING` y se retornaba `null`. |

## Ejemplos

Uso de la función `constant` con constantes

```
<?php

define("MAXSIZE", 100);

echo MAXSIZE;
echo constant("MAXSIZE"); // idéntico a la línea anterior

interface bar {
    const test = 'foobar!';
}

class foo {
    const test = 'foobar!';
}

$const = 'test';

var_dump(constant('bar::'. $const)); // string(7) "foobar!"
var_dump(constant('foo::'. $const)); // string(7) "foobar!"

?>

    
```php

Uso de la función `constant` con tipos enum (a partir de PHP 8.1.0)

```
<?php

enum Suit
{
    case Hearts;
    case Diamonds;
    case Clubs;
    case Spades;
}

$case = 'Hearts';

var_dump(constant('Suit::'. $case)); // enum(Suit::Hearts)

?>

    
```php

## Véase también

`define`, `defined`, `get_defined_constants`, La sección sobre las [constantes](#language.constants)
