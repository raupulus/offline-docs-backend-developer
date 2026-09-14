---
title: bcpowmod
description: Eleva un número de precisión arbitraria a otro, reducido por un módulo
  especificado
source_url: https://www.php.net/manual/es/function.bcpowmod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcpowmod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: '329574156'
order: 6310
---

bcpowmod

Eleva un número de precisión arbitraria a otro, reducido por un módulo especificado

## Descripción

```php
bcpowmod(string $num, string $exponent, string $modulus, [int $scale]): string
```php

Usa el método de exponenciación rápida para aumentar `num` a la potencia `exponent` con respecto al módulo `modulus`.

## Parámetros

`num`  
La base, como un string integral (es decir, la escala tiene que ser cero).

`exponent`  
El exponente, como un string integral no negativo (es decir, la escala tiene que ser cero).

`modulus`  
El módulo, como un string integral (es decir, la escala tiene que ser cero).

## Valores devueltos

Devuelve el resultado como un string.

## Errores/Excepciones

Esta función lanza un ValueError en los siguientes casos: `num`, `exponent` o `modulus` no es un string numérico con formato válido de BCMath, `num`, `exponent` o `modulus` tiene una parte fraccionaria, `exponent` es un valor negativo, `scale` está fuera del rango válido

Esta función lanza una excepción DivisionByZeroError si `modulus` es `0`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `scale` ahora es nullable. |
| 8.0.0 | Ahora lanza un ValueError en vez de devolver `false` si `exponent` es un valor negativo. |
| 8.0.0 | Dividiendo por `0` ahora lanza una excepción DivisionByZeroError en vez de devolver `false`. |

## Ejemplos

Los siguientes dos comandos son funcionalmente idénticos. La version `bcpowmod` sin embargo, se ejecuta en menos tiempo y admite mas parametros.

```
<?php
$a = bcpowmod($x, $y, $mod);

$b = bcmod(bcpow($x, $y), $mod);

// $a y $b son iguales el uno al otro.

?>

    
```php

## Notas

> [!NOTE]
> Debido a que este método utiliza la operación módulo, podrían obtenerse resultados inesperados en números enteros no positivos.

## Véase también

`bcpow`, `bcmod`, BcMath\Number::powmod
