---
title: print_r
description: Muestra información legible para una variable
source_url: https://www.php.net/manual/es/function.print-r.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/print-r.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: d816a0fad
order: 100730
---

print_r

Muestra información legible para una variable

## Descripción

```php
print_r(mixed $value, [bool $return]): string
```php

`print_r` muestra información sobre una variable, de manera que sea legible.

`print_r`, `var_dump` y `var_export` muestran asimismo las propiedades protegidas y privadas de un objeto. Los miembros de clases estáticas no serán mostrados.

## Parámetros

`value`  
La expresión a mostrar.

`return`  
Si se desea obtener el resultado de `print_r` en una cadena, se debe utilizar el parámetro `return`. Cuando este parámetro vale `true`, `print_r` retornará la información en lugar de mostrarla.

## Valores devueltos

Si se proporciona una `string`, un `int` o un `float`, se mostrará su valor. Si se proporciona un `array`, los valores se mostrarán en un formato que permite ver las claves y los elementos. Un formato similar se utilizará asimismo para los `object`s.

Cuando el parámetro `return` vale `true`, esta función retornará una `string`. De lo contrario, el valor de retorno será `true`.

## Historial de cambios

| Versión | Descripción                                                    |
|---------|----------------------------------------------------------------|
| 8.4.0   | El tipo de retorno ha cambiado de `stringbool` a `stringtrue`. |

## Ejemplos

Ejemplo con `print_r`

```
<pre>
<?php
$a = array ('a' => 'apple', 'b' => 'banana', 'c' => array ('x', 'y', 'z'));
print_r($a);
?>
</pre>

    
```php

El ejemplo anterior mostrará:

    <pre>
    Array
    (
        [a] => apple
        [b] => banana
        [c] => Array
            (
                [0] => x
                [1] => y
                [2] => z
            )
    )
    </pre>

Ejemplo con el parámetro `return`

```
<?php
$b = array ('m' => 'monkey', 'foo' => 'bar', 'x' => array ('x', 'y', 'z'));
$results = print_r($b, true); // $results contiene la salida de print_r

print_r($results);
?>

    
```php

## Notas

> [!NOTE]
> Cuando el parámetro `return` es utilizado, esta función utilizaba el buffer interno de salida anterior a PHP 7.1.0, y por lo tanto no puede ser utilizado en la función de devolución de llamada de `ob_start`.

## Véase también

`ob_start`, `var_dump`, `var_export`
