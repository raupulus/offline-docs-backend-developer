---
title: intval
description: Devuelve el valor entero equivalente de una variable
source_url: https://www.php.net/manual/es/function.intval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/intval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: false
translation_revision: 6197a68b1
order: 100540
---

intval

Devuelve el valor entero equivalente de una variable

## Descripción

```php
intval(mixed $value, [int $base]): int
```php

Devuelve el valor `int` de `value` utilizando la `base` proporcionada para la conversión (por omisión en base 10). `intval` no debería ser utilizada con objetos; en estos casos, se emitirá un error de nivel `E_WARNING` y la función devolverá 1.

## Parámetros

`value`  
El valor escalar a ser convertido en entero

`base`  
La base para la conversión

> [!NOTE]
> Si `base` es 0, la base utilizada se determina por el formato del parámetro `value`:
>
> - si la cadena incluye un prefijo "0x" (o "0X"), la base tomada será 16 (hex); de lo contrario,
>
> - si la cadena comienza por "0b" (o "0B"), la base tomada será 2 (binario); de lo contrario,
>
> - si la cadena comienza por "0", la base tomada será 8 (octal); de lo contrario,
>
> - la base tomada será 10 (decimal).

## Valores devueltos

Un valor de tipo `int` de `value` en caso de éxito o 0 en caso de fallo. Los arrays vacíos devuelven 0, los arrays no vacíos devuelven 1.

El valor máximo depende del sistema. Los sistemas de 32 bits tienen un valor entero signado máximo de -2147483648 a 2147483647. Por lo tanto, por ejemplo, en un sistema similar, `intval('1000000000000')` devolverá 2147483647. El valor entero signado máximo para un sistema de 64 bits es 9223372036854775807.

Las cadenas de caracteres devuelven la mayoría de las veces 0, esto depende de los caracteres en el extremo izquierdo de la cadena. La regla común del [moldeado de enteros](#language.types.integer.casting) se aplica.

> [!NOTE]
> Las cadenas numéricas que utilizan notación científica (que contienen la letra `e` o `E`) se analizan primero como números antes de ser convertidas a entero.
>
> Dado que la parte numérica de la cadena se analiza en su totalidad, el resultado no es simplemente la parte entera inicial. Además, los exponentes grandes pueden desbordarse hasta `PHP_INT_MAX`:
>
> <div class="informalexample">
>
> ```
> <?php
> echo intval('42.42e42'); // 9223372036854775807 en sistemas de 64 bits
> ?>
>
>     
> ```
>
> </div>
>
> Véase [Cadenas numéricas](#language.types.numeric-strings) para obtener detalles sobre cómo se interpretan estas cadenas.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | El nivel de error al convertir desde un objeto ha sido modificado de `E_NOTICE` a `E_WARNING`. |

## Ejemplos

Ejemplos con `intval`

Los ejemplos siguientes están basados en un sistema de 64 bits.

```
<?php
echo intval(42), PHP_EOL;                      // 42
echo intval(4.7), PHP_EOL;                     // 4
echo intval('42'), PHP_EOL;                    // 42
echo intval('+42'), PHP_EOL;                   // 42
echo intval('-42'), PHP_EOL;                   // -42
echo intval(042), PHP_EOL;                     // 34
echo intval('042'), PHP_EOL;                   // 42
echo intval(1e10), PHP_EOL;                    // 10000000000
echo intval('1e10'), PHP_EOL;                  // 10000000000
echo intval(0x1A), PHP_EOL;                    // 26
echo intval('0x1A'), PHP_EOL;                  // 0
echo intval('0x1A', 0), PHP_EOL;               // 26
echo intval(42000000), PHP_EOL;                // 42000000
echo intval(420000000000000000000), PHP_EOL;   // -4275113695319687168
echo intval('420000000000000000000'), PHP_EOL; // 9223372036854775807
echo intval(42, 8), PHP_EOL;                   // 42
echo intval('42', 8), PHP_EOL;                 // 34
echo intval(array()), PHP_EOL;                 // 0
echo intval(array('foo', 'bar')), PHP_EOL;     // 1
echo intval(false), PHP_EOL;                   // 0
echo intval(true), PHP_EOL;                    // 1
?>

    
```php

## Notas

> [!NOTE]
> El parámetro `base` no tiene ningún efecto a menos que el parámetro `value` sea una `string`.

## Véase también

`boolval`, `floatval`, `strval`, `settype`, `is_numeric`, [Definición del tipo](#language.types.type-juggling), [Números grandes BCMath](#ref.bc)
