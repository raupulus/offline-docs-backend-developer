---
title: bcpow
description: Elevar un número de precisión arbitraria a otro
source_url: https://www.php.net/manual/es/function.bcpow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcpow.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c9490d424
order: 6300
---

bcpow

Elevar un número de precisión arbitraria a otro

## Descripción

```php
bcpow(string $num, string $exponent, [int $scale]): string
```php

Eleva `num` a la potencia `exponent`.

## Parámetros

`num`  
La base, como un string.

`exponent`  
El exponente, como un string. Debe ser un valor sin parte fraccionaria. El rango válido del exponente es específico de la plataforma, pero es al menos de `-2147483648` a `2147483647`.

## Valores devueltos

Devuelve el resultado como un string.

## Errores/Excepciones

Esta función lanza una ValueError en los siguientes casos: `num` o `exponent` no es un string numérico con formato válido de BCMath, `exponent` tiene una parte fraccionaria, `exponent` o `scale` están fuera del rango válido

Esta función lanza una DivisionByZeroError si `num` es `0` y `exponent` es un valor negativo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Las potencias negativas de `0` anteriormente devolvían `0`, pero ahora lanzan una excepción DivisionByZeroError. |
| 8.0.0 | Cuando `exponent` tiene una parte fraccionaria, ahora lanza un ValueError en lugar de truncar. |
| 7.3.0 | `bcpow` ahora devuelve números con la escala solicitada. Anteriormente, los números devueltos podían omitir los ceros decimales finales. |

## Ejemplos

Ejemplo de `bcpow`

```
<?php

echo bcpow('4.2', '3', 2); // 74.08

?>

   
```php

## Notas

> [!NOTE]
> Antes de PHP 7.3.0, `bcpow` podría devolver un resultado con menos dígitos después del punto decimal que los indicados en el parámetro `scale`. Esto sucede únicamente cuando el resultado no necesita toda la precisión disponible por `scale`. Por ejemplo:
>
> <div class="example">
>
> <div class="title">
>
> Ejemplo de escalado de `bcpow`
>
> </div>
>
> ```
> <?php
> echo bcpow('5', '2', 2);     // Imprime "25", no "25.00"
> ?>
>
>      
> ```
>
> </div>

## Véase también

`bcpowmod`, `bcsqrt`, BcMath\Number::pow
