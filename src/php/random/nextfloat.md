---
title: Random\Randomizer::nextFloat
description: Devuelve un float seleccionado del intervalo abierto a la derecha [0.0,
  1.0)
source_url: https://www.php.net/manual/es/random-randomizer.nextfloat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/randomizer/nextfloat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: true
translation_revision: 05579435b
order: 68190
---

Random\Randomizer::nextFloat

Devuelve un float seleccionado del intervalo abierto a la derecha \[0.0, 1.0)

## Descripción

```php
public Random\Randomizer::nextFloat(): float
```php

Devuelve un float seleccionado de manera uniforme y equidistribuida del intervalo abierto a la derecha de `0.0` hasta, pero sin incluir, `1.0`.

La probabilidad de que un float devuelto esté en un subintervalo dado abierto a la derecha es proporcional al tamaño del subintervalo. Esto significa que la probabilidad de que un float sea *menor que* `0.5` es del 50 %, lo cual es igual a la probabilidad de que un float sea *al menos* `0.5`. Del mismo modo, la probabilidad de que un float esté en el intervalo abierto a la derecha de `0.2` hasta, pero sin incluir, `0.25` es exactamente del 5 %.

Esta propiedad permite utilizar fácilmente Random\Randomizer::nextFloat para generar un bool aleatorio con una probabilidad dada verificando si el float devuelto es *menor que* una probabilidad dada.

> [!NOTE]
> El dominio de los floats devueltos por Random\Randomizer::nextFloat es idéntico al de `Randomizer::getFloat(0.0, 1.0, IntervalBoundary::ClosedOpen)`.
>
> La implementación interna de Random\Randomizer::nextFloat es más eficiente.

> [!CAUTION]
> Escalar el valor devuelto a un intervalo diferente utilizando la multiplicación o la adición (una transformación afín) podría resultar en un sesgo en el valor resultante, ya que los floats no son igualmente densos a lo largo de la línea de los números. Como no todos los valores pueden ser representados exactamente por un float, el resultado de la transformación afín podría también resultar en valores fuera del intervalo solicitado debido a redondeos implícitos. Una [explicación detallada](#random-randomizer.getfloat.affine-transformation) de los problemas con la transformación afín se proporciona en la documentación para Random\Randomizer::getFloat.
>
> Utilizar Random\Randomizer::getFloat para generar un float aleatorio en un intervalo arbitrario. Utilizar Random\Randomizer::getInt para generar un integer aleatorio en un intervalo arbitrario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un float seleccionado de manera uniforme en el intervalo abierto a la derecha (`IntervalBoundary::ClosedOpen`) \[0.0, 1.0). `0.0` es un valor de retorno posible, `1.0` no lo es.

## Errores/Excepciones

- Cualquier `Throwable` lanzado por el método Random\Engine::generate del [`Random\Randomizer::$engine`](#random-randomizer.props.engine) subyacente.

## Ejemplos

Ejemplo de Random\Randomizer::nextFloat

```
<?php
$r = new \Random\Randomizer();

// El resultado del bool será verdadero con la probabilidad dada.
$chance = 0.5;

$bool = $r->nextFloat() < $chance;

echo ($bool ? "You won" : "You lost"), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    You won

Escalado incorrecto utilizando una transformación afín

```
<?php
final class MaxEngine implements Random\Engine {
    public function generate(): string {
        return "\xff";
    }
}

$randomizer = new \Random\Randomizer(new MaxEngine);

$min = 3.5;
$max = 4.5;

// NO HACER ESTO:
//
// Esto mostrará 4.5, a pesar de que nextFloat() muestree
// desde un intervalo abierto a la derecha, que nunca devolverá 1.
printf("Wrong scaling: %.17g", $randomizer->nextFloat() * ($max - $min) + $min);

// Correcto:
// $randomizer->getFloat($min, $max, \Random\IntervalBoundary::ClosedOpen);
?>

   
```php

El ejemplo anterior mostrará:

    Wrong scaling: 4.5

## Véase también

Random\Randomizer::getFloat
