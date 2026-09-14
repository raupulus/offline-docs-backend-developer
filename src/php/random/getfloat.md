---
title: Random\Randomizer::getFloat
description: Devuelve un float seleccionado uniformemente
source_url: https://www.php.net/manual/es/random-randomizer.getfloat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/randomizer/getfloat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_revision: 423a1da63
order: 68170
---

Random\Randomizer::getFloat

Devuelve un float seleccionado uniformemente

## Descripción

```php
public Random\Randomizer::getFloat(float $min, float $max, [Random\IntervalBoundary $boundary]): float
```php

Devuelve un float seleccionado uniformemente y equidistribuido de un intervalo solicitado.

Debido a la precisión limitada, no todos los números reales pueden ser representados exactamente como floats. Si un número no puede ser representado exactamente, se redondea al número exactamente representable más cercano. Además, los floats no son igualmente densos en toda la línea de números. Debido a que los floats utilizan un exponente binario, la distancia entre dos floats vecinos se duplica en cada potencia de dos. En otras palabras: Hay el mismo número de floats representables entre `1.0` y `2.0` que entre `2.0` y `4.0`, `4.0` y `8.0`, `8.0` y `16.0`, y así sucesivamente.

Seleccionar un número aleatorio en un intervalo arbitrario, por ejemplo dividiendo dos enteros, podría resultar en una distribución sesgada por esta razón. El redondeo necesario hará que algunos floats sean devueltos con más frecuencia que otros, en particular alrededor de las potencias de dos cuando la densidad de los floats cambia.

Random\Randomizer::getFloat implementa un algoritmo que devolverá un float seleccionado uniformemente del conjunto más grande posible de floats exactamente representables y equidistribuidos en el intervalo solicitado. La distancia entre los floats seleccionables (« paso ») corresponde a la distancia entre los floats con la densidad más baja, es decir, la distancia entre los floats en los límites del intervalo con el valor absoluto más grande. Esto significa que no todos los floats representables en un intervalo dado pueden ser devueltos si el intervalo cruza una o más potencias de dos. El paso comenzará en el límite del intervalo con el valor absoluto más grande para garantizar que los pasos se alineen con los floats exactamente representables.

Los límites de intervalo cerrados siempre estarán incluidos en el conjunto de floats seleccionables. Por lo tanto, si el tamaño del intervalo no es un múltiplo exacto del paso y el límite con el valor absoluto más pequeño es un límite cerrado, la distancia entre este límite y su float más cercano será más pequeña que el paso.

> [!CAUTION]
> El postprocesamiento de los floats devueltos corre el riesgo de romper la equidistribución uniforme, ya que los floats intermedios en una operación matemática sufren un redondeo implícito. El intervalo solicitado debe corresponder lo más estrechamente posible al intervalo deseado y el redondeo solo debe realizarse como una operación explícita justo antes de mostrar el número seleccionado a un usuario.

## Explicaciones del algoritmo utilizando valores de ejemplo

Para dar un ejemplo del funcionamiento del algoritmo, consideremos una representación en coma flotante que utiliza una mantisa de 3 bits. Esto es capaz de representar 8 valores float diferentes entre las potencias de dos consecutivas. Esto significa que entre `1.0` y `2.0` todos los pasos de tamaño `0.125` son exactamente representables y entre `2.0` y `4.0` todos los pasos de tamaño `0.25` son exactamente representables. En realidad, los floats de PHP utilizan una mantisa de 52 bits y pueden representar 2<sup>52</sup> valores diferentes entre cada potencia de dos. Esto significa que `1.0`, `1.125`, `1.25`, `1.375`, `1.5`, `1.625`, `1.75`, `1.875`, `2.0`, `2.25`, `2.5`, `2.75`, `3.0`, `3.25`, `3.5`, `3.75`, `4.0` son los floats exactamente representables entre `1.0` y `4.0`.

Ahora consideremos que `$randomizer->getFloat(1.625, 2.5, IntervalBoundary::ClosedOpen)` es llamado, es decir, que se solicita un float aleatorio comenzando en `1.625` hasta, pero sin incluir, `2.5`. El algoritmo determina primero el paso en el límite con el valor absoluto más grande (`2.5`). El paso en este límite es `0.25`.

Es de notar que el tamaño del intervalo solicitado es `0.875`, que no es un múltiplo exacto de `0.25`. Si el algoritmo comenzara a caminar en el límite inferior `1.625`, encontraría `2.125`, que no es exactamente representable y sufriría un redondeo implícito. Por lo tanto, el algoritmo comienza a caminar en el límite superior `2.5`. Los valores seleccionables son: `2.25`, `2.0`, `1.75`, `1.625` `2.5` no está incluido, ya que el límite superior del intervalo solicitado es un límite abierto. `1.625` está incluido, incluso si su distancia al valor más cercano `1.75` es `0.125`, que es más pequeña que el paso determinado previamente de `0.25`. La razón por la que es así es que el intervalo solicitado está cerrado en el límite inferior (`1.625`) y los límites cerrados siempre están incluidos.

Finalmente, el algoritmo selecciona uniformemente uno de los cuatro valores seleccionables al azar y lo devuelve.

### Por qué dividir dos enteros no funciona

En el ejemplo anterior, hay ocho números float representables entre cada subintervalo delimitado por una potencia de dos. Para dar un ejemplo de por qué dividir dos enteros no funcionaría bien para generar un float aleatorio, consideremos que hay 16 números float uniformemente distribuidos en el intervalo abierto a la derecha de `0.0` hasta, pero sin incluir, `1.0`. La mitad de ellos son los ocho valores exactamente representables entre `0.5` y `1.0`, la otra mitad son los valores entre `0.0` y `1.0` con un paso de `0.0625`. Estos valores pueden generarse fácilmente dividiendo un entero aleatorio entre `0` y `15` por `16` para obtener uno de los siguientes valores: `0.0`, `0.0625`, `0.125`, `0.1875`, `0.25`, `0.3125`, `0.375`, `0.4375`, `0.5`, `0.5625`, `0.625`, `0.6875`, `0.75`, `0.8125`, `0.875`, `0.9375`

Este float aleatorio podría escalarse al intervalo abierto a la derecha de `1.625` hasta, pero sin incluir, `2.75` multiplicándolo por el tamaño del intervalo (`0.875`) y añadiendo el mínimo `1.625`. Esta transformación afín daría los siguientes valores: `1.625` redondeado a `1.625`, `1.679` redondeado a `1.625`, `1.734` redondeado a `1.75`, `1.789` redondeado a `1.75`, `1.843` redondeado a `1.875`, `1.898` redondeado a `1.875`, `1.953` redondeado a `2.0`, `2.007` redondeado a `2.0`, `2.062` redondeado a `2.0`, `2.117` redondeado a `2.0`, `2.171` redondeado a `2.25`, `2.226` redondeado a `2.25`, `2.281` redondeado a `2.25`, `2.335` redondeado a `2.25`, `2.390` redondeado a `2.5`, `2.445` redondeado a `2.5` Es de notar cómo el límite superior de `2.5` sería devuelto, a pesar del hecho de que sea un límite abierto y por lo tanto excluido. También es de notar cómo `2.0` y `2.25` tienen el doble de probabilidades de ser devueltos en comparación con los otros valores.

## Parámetros

`min`  
El límite inferior del intervalo.

`max`  
El límite superior del intervalo.

`boundary`  
Especifica si los límites del intervalo son valores de retorno posibles.

## Valores devueltos

Un valor float seleccionado uniformemente y equidistribuido del intervalo especificado por `min`, `max` y `boundary`. Si `boundary` es `Random\IntervalBoundary::ClosedClosed`, `min` y `max` son valores de retorno posibles.

## Errores/Excepciones

- Si el valor de `min` no es finito (`is_finite`), se lanzará una `ValueError`.

- Si el valor de `max` no es finito (`is_finite`), se lanzará una `ValueError`.

- Si el intervalo solicitado no contiene ningún valor, se lanzará una `ValueError`.

- Cualquier `Throwable` lanzado por el método Random\Engine::generate del [`Random\Randomizer::$engine`](#random-randomizer.props.engine) subyacente.

## Ejemplos

Ejemplo de Random\Randomizer::getFloat

```
<?php
$randomizer = new \Random\Randomizer();

// Es de notar que la granularidad de la latitud es el doble
// de la granularidad de la longitud.
//
// Para la latitud, el valor puede ser tanto -90 como 90.
// Para la longitud, el valor puede ser 180, pero no -180, ya que
// -180 y 180 se refieren a la misma longitud.
printf(
    "Lat: %+.6f Lng: %+.6f",
    $randomizer->getFloat(-90, 90, \Random\IntervalBoundary::ClosedClosed),
    $randomizer->getFloat(-180, 180, \Random\IntervalBoundary::OpenClosed),
);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Lat: +69.244304 Lng: -53.548951

## Notas

> [!NOTE]
> Este método implementa el algoritmo de la sección γ tal como se publicó en [ Dibujar números float aleatorios de un intervalo. Frédéric Goual ](https://dl.acm.org/doi/10.1145/3503512) para obtener las propiedades de comportamiento deseadas.

> [!CAUTION]
> El underflow se deja intencionalmente sin manejar en el algoritmo de sección γ. Esto puede resultar en valores incorrectos para intervalos con límites en el rango subnormal de números de punto flotante, es decir, para límites con un valor absoluto menor que aproximadamente `2-1020` (alrededor de `8.9e-308`).

## Véase también

Random\Randomizer::nextFloat

Random\Randomizer::getInt
