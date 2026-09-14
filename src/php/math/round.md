---
title: round
description: Redondea un número de punto flotante
source_url: https://www.php.net/manual/es/function.round.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/round.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_revision: c142be811
order: 44850
---

round

Redondea un número de punto flotante

## Descripción

```php
round(int $num, [int $precision], [int $mode]): float
```php

Devuelve el valor redondeado de `num` a la precisión `precision` (número de dígitos después del punto decimal). El argumento `precision` puede ser negativo o `null` : es su valor por omisión.

## Parámetros

`num`  
El valor a redondear.

`precision`  
El número opcional de decimales a redondear.

Si el argumento `precision` es positivo, `num` será redondeado utilizando el argumento `precision` para definir el número significativo de dígitos después del punto decimal.

Si el argumento `precision` es negativo, `num` será redondeado utilizando el argumento `precision` para definir el número significativo de dígitos antes del punto decimal, i.e. el múltiplo más cercano de `pow(10, -$precision)`, i.e. para una `precision` de -1, `num` será redondeado a 10, para una `precision` de -2 a 100, etc.

`mode`  
Utilice RoundingMode o una de las constantes siguientes para especificar el método de redondeo.

| Constantes | Descripción |
|----|----|
| `PHP_ROUND_HALF_UP` | Redondea `num` alejándose de cero cuando está a mitad de camino, redondeando así 1.5 a 2, y -1.5 a -2. |
| `PHP_ROUND_HALF_DOWN` | Redondea `num` acercándose a cero cuando está a mitad de camino, redondeando así 1.5 a 1, y -1.5 a -1. |
| `PHP_ROUND_HALF_EVEN` | Redondea `num` al valor par más cercano cuando está a mitad de camino, redondeando así 1.5 y 2.5 a 2. |
| `PHP_ROUND_HALF_ODD` | Redondea `num` al valor impar más cercano cuando está a mitad de camino, redondeando así 1.5 a 1 y 2.5 a 3. |

Sin embargo, tenga en cuenta que algunos métodos recién añadidos solo existen en [RoundingMode](#enum.roundingmode).

## Valores devueltos

El valor redondeado a la `precision` dada como `float`.

## Errores/Excepciones

La función lanza una ValueError si `mode` es inválido. Anterior a PHP 8.4.0, un modo inválido era silenciosamente convertido en `PHP_ROUND_HALF_UP`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Cuatro nuevos métodos de redondeo han sido añadidos. |
| 8.4.0 | Ahora lanza una ValueError si `mode` es inválido. |
| 8.0.0 | `num` ya no acepta objetos internos que soporten las conversiones numéricas. |

## Ejemplos

Ejemplo con `round`

```
<?php
var_dump(round(3.4));
var_dump(round(3.5));
var_dump(round(3.6));
var_dump(round(3.6, 0));
var_dump(round(5.045, 2));
var_dump(round(5.055, 2));
var_dump(round(345, -2));
var_dump(round(345, -3));
var_dump(round(678, -2));
var_dump(round(678, -3));
?>

    
```php

El ejemplo anterior mostrará:

```
float(3)
float(4)
float(4)
float(4)
float(5.05)
float(5.06)
float(300)
float(0)
float(700)
float(1000)

    
```php

Cómo `precision` afecta un flotante

```
<?php
$number = 135.79;

var_dump(round($number, 3));
var_dump(round($number, 2));
var_dump(round($number, 1));
var_dump(round($number, 0));
var_dump(round($number, -1));
var_dump(round($number, -2));
var_dump(round($number, -3));
?>

    
```php

El ejemplo anterior mostrará:

```
float(135.79)
float(135.79)
float(135.8)
float(136)
float(140)
float(100)
float(0)

    
```php

Ejemplo con `mode`

```
<?php
echo "Método de redondeo con 9.5" . PHP_EOL;
var_dump(round(9.5, 0, PHP_ROUND_HALF_UP));
var_dump(round(9.5, 0, PHP_ROUND_HALF_DOWN));
var_dump(round(9.5, 0, PHP_ROUND_HALF_EVEN));
var_dump(round(9.5, 0, PHP_ROUND_HALF_ODD));

echo PHP_EOL;
echo "Método de redondeo con 8.5" . PHP_EOL;
var_dump(round(8.5, 0, PHP_ROUND_HALF_UP));
var_dump(round(8.5, 0, PHP_ROUND_HALF_DOWN));
var_dump(round(8.5, 0, PHP_ROUND_HALF_EVEN));
var_dump(round(8.5, 0, PHP_ROUND_HALF_ODD));
?>

    
```php

El ejemplo anterior mostrará:

```
Método de redondeo con 9.5
float(10)
float(9)
float(10)
float(9)

Método de redondeo con 8.5
float(9)
float(8)
float(8)
float(9)

    
```php

Ejemplo con `mode` y `precision`

```
<?php
echo "Uso de PHP_ROUND_HALF_UP con una precisión de una decimal" . PHP_EOL;
var_dump(round( 1.55, 1, PHP_ROUND_HALF_UP));
var_dump(round(-1.55, 1, PHP_ROUND_HALF_UP));

echo PHP_EOL;
echo "Uso de PHP_ROUND_HALF_DOWN con una precisión de una decimal" . PHP_EOL;
var_dump(round( 1.55, 1, PHP_ROUND_HALF_DOWN));
var_dump(round(-1.55, 1, PHP_ROUND_HALF_DOWN));

echo PHP_EOL;
echo "Uso de PHP_ROUND_HALF_EVEN con una precisión de una decimal" . PHP_EOL;
var_dump(round( 1.55, 1, PHP_ROUND_HALF_EVEN));
var_dump(round(-1.55, 1, PHP_ROUND_HALF_EVEN));

echo PHP_EOL;
echo "Uso de PHP_ROUND_HALF_ODD con una precisión de una decimal" . PHP_EOL;
var_dump(round( 1.55, 1, PHP_ROUND_HALF_ODD));
var_dump(round(-1.55, 1, PHP_ROUND_HALF_ODD));
?>

    
```php

El ejemplo anterior mostrará:

```
Uso de PHP_ROUND_HALF_UP con una precisión de una decimal
float(1.6)
float(-1.6)

Uso de PHP_ROUND_HALF_DOWN con una precisión de una decimal
float(1.5)
float(-1.5)

Uso de PHP_ROUND_HALF_EVEN con una precisión de una decimal
float(1.6)
float(-1.6)

Uso de PHP_ROUND_HALF_ODD con una precisión de una decimal
float(1.5)
float(-1.5)

    
```php

Ejemplo de uso de RoundingMode

```
<?php
foreach (RoundingMode::cases() as $mode) {
    foreach ([
        8.5,
        9.5,
        -3.5,
    ] as $number) {
        printf("%-17s: %+.17g -> %+.17g\n", $mode->name, $number, round($number, 0, $mode));
    }
    echo "\n";
}
?>

   
```php

El ejemplo anterior mostrará:

```
HalfAwayFromZero : +8.5 -> +9
HalfAwayFromZero : +9.5 -> +10
HalfAwayFromZero : -3.5 -> -4

HalfTowardsZero  : +8.5 -> +8
HalfTowardsZero  : +9.5 -> +9
HalfTowardsZero  : -3.5 -> -3

HalfEven         : +8.5 -> +8
HalfEven         : +9.5 -> +10
HalfEven         : -3.5 -> -4

HalfOdd          : +8.5 -> +9
HalfOdd          : +9.5 -> +9
HalfOdd          : -3.5 -> -3

TowardsZero      : +8.5 -> +8
TowardsZero      : +9.5 -> +9
TowardsZero      : -3.5 -> -3

AwayFromZero     : +8.5 -> +9
AwayFromZero     : +9.5 -> +10
AwayFromZero     : -3.5 -> -4

NegativeInfinity : +8.5 -> +8
NegativeInfinity : +9.5 -> +9
NegativeInfinity : -3.5 -> -4

PositiveInfinity : +8.5 -> +9
PositiveInfinity : +9.5 -> +10
PositiveInfinity : -3.5 -> -3

   
```php

## Véase también

`ceil`, `floor`, `number_format`
