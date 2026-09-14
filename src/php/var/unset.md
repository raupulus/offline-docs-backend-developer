---
title: unset
description: unset destruye una variable
source_url: https://www.php.net/manual/es/function.unset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/unset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: d816a0fad
order: 100780
---

unset

unset

destruye una variable

## Descripción

```php
unset(mixed $var, mixed ...$vars): void
```php

`unset` destruye la o las variables cuyo nombre ha sido pasado como argumento `var`.

El comportamiento de `unset` dentro de una función puede variar según el tipo de variable que se desee destruir.

Si una variable global es destruida con `unset` desde una función, solo la variable local será destruida. La variable global mantendrá el valor adquirido antes de la llamada a `unset`.

Utilización de `unset`

```
<?php
function destroy_foo()
{
    global $foo;
    unset($foo);
}

$foo = 'bar';
destroy_foo();
echo $foo;
?>

    
```php

Para destruir una variable global dentro de una función, se puede utilizar el array `$GLOBALS`:

`unset` una variable global

```
<?php
function foo()
{
    unset($GLOBALS['bar']);
}

$bar = "truc";
foo();
?>

    
```php

Si una variable que es pasada por referencia es destruida dentro de una función, solo la variable local será destruida. La variable global conservará el mismo valor que tenía antes de la llamada a `unset`.

`unset` con referencia

```
<?php
function foo(&$bar)
{
    unset($bar);
    $bar = "blah";
}

$bar = 'truc';
echo "$bar\n";

foo($bar);
echo "$bar\n";
?>

    
```php

Si una variable estática es destruida dentro de una función, `unset` destruirá la variable solo en el contexto del resto de la función. Las llamadas siguientes restaurarán el valor anterior de la variable.

`unset` con variable estática

```
<?php
function foo()
{
    static $bar;
    $bar++;
    echo "Antes de unset: $bar, ";
    unset($bar);
    $bar = 23;
    echo "después de unset: $bar\n";
}

foo();
foo();
foo();
?>

    
```php

## Parámetros

`var`  
La variable a destruir.

`vars`  
Variables adicionales.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `unset`

```
<?php
// Destrucción de una sola variable
unset($foo);

// Destrucción de un elemento de array
unset($bar['quux']);

// Destrucción de múltiples variables
unset($foo1, $foo2, $foo3);
?>

    
```php

## Notas

> [!NOTE]
> Como esto es una estructura del lenguaje, y no una función, no es posible llamarla con las [funciones variables](#functions.variable-functions) o [argumentos nombrados](#functions.named-arguments).

> [!NOTE]
> Es posible destruir cualquier propiedad visible en el contexto actual.
>
> Si está declarado, [\_\_get()](#object.get) es llamado al acceder a una propiedad no definida, y [\_\_set()](#object.set) es llamado al definir una propiedad no definida.

> [!NOTE]
> No es posible destruir la variable especial `$this` dentro de un método de un objeto.

> [!NOTE]
> Al utilizar esta función en propiedades de objeto inaccesibles, el método mágico [\_\_unset](#object.unset) será llamado, si existe.

## Véase también

`isset`, [\_\_unset()](#object.unset), `empty`, `array_splice`, [(unset) casting](#language.types.null.casting)
