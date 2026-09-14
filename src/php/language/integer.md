---
title: Los enteros
source_url: https://www.php.net/manual/es/language.types.integer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/integer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 78a11d3ca
order: 4440
---

## Los enteros

Un `int` es un número perteneciente al conjunto ℤ = {..., -2, -1, 0, 1, 2, ...}.

## Véase también

[Los números de coma flotante](#language.types.float), [Las precisiones arbitrarias / BCMath](#book.bc), [Los enteros de longitud arbitraria / GMP](#book.gmp)

## Sintaxis

Los `int`s pueden ser especificados en notación decimal (base 10), hexadecimal (base 16), octal (base 8), o binaria (base 2). El [operador de negación](#language.operators.arithmetic) puede ser utilizado para designar un `int` negativo.

Para utilizar la notación octal, preceda el número de un `0` (cero). A partir de PHP 8.1.0, la notación octal puede ser precedida con `0o` o `0O`. Para utilizar la notación hexadecimal, preceda el número de `0x`. Para utilizar la notación binaria, preceda el número de `0b`.

A partir de PHP 7.4.0, los enteros literales pueden contener underscores (`_`) entre los dígitos, para una mejor legibilidad de los literales. Estos underscores son eliminados por el escáner de PHP.

Los enteros literales

```php
<?php
$a = 1234; // un número decimal
$a = 0123; // un número octal (equivalente a 83 en decimal)
$a = 0o123; // un número octal (a partir de PHP 8.1.0)
$a = 0x1A; // un número hexadecimal (equivalente a 26 en decimal)
$a = 0b11111111; // un número binario (equivalente a 255 en decimal)
$a = 1_234_567; // un número decimal (a partir de PHP 7.4.0)
?>

   
```

Formalmente, la estructura de un `int` literal es a partir de PHP 8.1.0 (anteriormente, los prefijos octales `0o` o `0O` no estaban permitidos, y antes de PHP 7.4.0, los underscores no estaban permitidos.

    decimal     : [1-9][0-9]*(_[0-9]+)*
                | 0

    hexadecimal : 0[xX][0-9a-fA-F]+(_[0-9a-fA-F]+)*

    octal       : 0[oO]?[0-7]+(_[0-7]+)*

    binary      : 0[bB][01]+(_[01]+)*

    integer     : decimal
                | hexadecimal
                | octal
                | binary

El tamaño de un `int` es dependiente de la plataforma, sin embargo, un valor máximo de aproximadamente 2 mil millones es habitual (esto corresponde a 32 bits con signo). Las plataformas de 64 bits tienen habitualmente un valor máximo de aproximadamente 9E18. PHP no soporta los `int`s sin signo. El tamaño de un `int` puede ser determinado utilizando la constante `PHP_INT_SIZE`, el valor máximo, utilizando la constante `PHP_INT_MAX`, y el valor mínimo utilizando la constante `PHP_INT_MIN`.

## Desbordamiento de entero

Si PHP encuentra un número superior al máximo de un `int`, será interpretado como un `float`. De la misma manera, una operación que resulte en un número fuera del rango del tipo `int` devolverá un `float`.

Desbordamiento de entero en un sistema de 32 bits

```php
<?php

$large_number = 50000000000000000000;
var_dump($large_number);         // float(5.0E+19)
var_dump(PHP_INT_MAX + 1);       // sistema de 32 bits: float(2147483648)
                                 // sistema de 64 bits: float(9.2233720368548E+18)
?>

   
```

## División de entero

No hay operador de división de `int` en PHP, para lograr esto utilizar la función `intdiv`. `1/2` produce el `float` (`0.5`). El valor puede ser convertido en un `int` para redondear hacia cero, o utilizando la función `round` para tener un control más fino sobre cómo se realiza el redondeo.

División

```php
<?php
var_dump(25/7);         // float(3.5714285714286)
var_dump((int) (25/7)); // int(3)
var_dump(round(25/7));  // float(4)
?>

   
```

## Conversión en entero

Para convertir explícitamente un valor a `int`, utilice la conversión `(int)`. Sin embargo, en la mayoría de los casos no es necesaria la conversión, ya que un valor se convertirá automáticamente si un operador, función o estructura de control requiere un argumento `int`. Un valor puede también ser convertido en un `int` utilizando la función `intval`.

Si un `resource` es convertido a un `int`, entonces el resultado será el identificador único del `resource` asignado por PHP en la ejecución.

Ver también [el transtipado](#language.types.type-juggling).

### Desde un [booléen](#language.types.boolean)

`false` corresponde a `0` (cero), y `true` corresponde a `1` (uno).

### Desde [un número de coma flotante](#language.types.float)

Al convertir un `float` en `int`, el número es redondeado *hacia cero*. A partir de PHP 8.1.0, se emite una notificación de deprecación al realizar la conversión implícita de un `float` no integral en `int` perdiendo precisión.

Conversión desde números flotantes

```php
<?php

function foo($value): int {
  return $value;
}

var_dump(foo(8.1)); // "Deprecated: Implicit conversion from float 8.1 to int loses precision" a partir de PHP 8.1.0
var_dump(foo(8.1)); // Antes de PHP 8.1.0
var_dump(foo(8.0)); // 8 en ambos casos

var_dump((int) 8.1); // 8 en ambos casos
var_dump(intval(8.1)); // 8 en ambos casos
?>

    
```

Si el número de coma flotante está más allá de los límites de los `int`s (habitualmente, `+/- 2.15e+9 = 2^31` en plataformas de 32 bits y `+/- 9.22e+18 = 2^63` en plataformas de 64 bits), el resultado será indefinido, ya que el `float` no tiene suficiente precisión para dar un resultado `int` exacto. ¡No se emite ninguna alerta cuando ocurre este comportamiento!

> [!NOTE]
> `NaN`, `Infinity` y `-Inf` son siempre igual a cero al convertir en `int`.

> [!WARNING]
> Nunca convierta una fracción desconocida en un `int`, esto puede generar resultados inesperados.
>
> <div class="informalexample">
>
> ```
> <?php
> echo (int) ( (0.1+0.7) * 10 ); // Muestra 7 !
> ?>
>
>      
> ```
>
> </div>
>
> Ver también la sección sobre [las alertas concernientes a la precisión de los números de coma flotante](#warn.float-precision).

### Desde cadenas de caracteres

Si una cadena es [numérica](#language.types.numeric-strings) o numérica de cabeza entonces será transformada en su valor entero correspondiente, de lo contrario será convertida a cero (`0`).

### Desde `NULL`

`null` es siempre convertido en cero (`0`).

### Desde otros tipos

> [!CAUTION]
> El comportamiento de la conversión en `int` es indefinido desde otros tipos. No reportar *ningún* comportamiento observado, sabiendo que pueden cambiar sin previo aviso.
