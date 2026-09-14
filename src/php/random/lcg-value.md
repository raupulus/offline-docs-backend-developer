---
title: lcg_value
description: Generador de congruencia lineal combinada
source_url: https://www.php.net/manual/es/function.lcg-value.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/functions/lcg-value.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: 9b1673cf1
order: 67860
---

lcg_value

Generador de congruencia lineal combinada

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.4.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
#[\Deprecated] lcg_value(): float
```php

`lcg_value` devuelve un número pseudoaleatorio, comprendido entre 0 y 1. `lcg_value` combina dos generadores de congruencia, con períodos respectivos de `2^31 - 85` y `2^31 - 249`. El período de esta función es el producto de estos dos números primos (es decir, `(2^31 - 85)*(2^31 - 249)`).

> [!CAUTION]
> Esta función no genera valores criptográficamente seguros, y *no debe* ser utilizada con fines criptográficos, o con fines que requieran que los valores devueltos sean indescifrables.
>
> Si se requiere aleatoriedad criptográficamente segura, el `Random\Randomizer` puede ser utilizado con el motor `Random\Engine\Secure`. Para casos de uso simples, las funciones `random_int` y `random_bytes` proporcionan una API práctica y segura que es soportada por el CSPRNG del sistema operativo.

> [!CAUTION]
> Escalar el valor de retorno a un intervalo diferente utilizando la multiplicación o la adición (una transformación afín) puede provocar un sesgo en el valor resultante, ya que los números de punto flotante no están distribuidos uniformemente en la línea numérica. Como no todos los valores pueden ser representados exactamente por un número de punto flotante, el resultado de la transformación afín también puede dar valores fuera del intervalo solicitado.
>
> Utilice Random\Randomizer::getFloat para generar un número de punto flotante aleatorio en un intervalo arbitrario. Utilice Random\Randomizer::getInt para generar un entero aleatorio en un intervalo arbitrario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un valor pseudoaleatorio, en el intervalo de 0.0 a 1.0 inclusive.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.4.0   | Esta función ha sido deprecada. |

## Véase también

Random\Randomizer::getFloat, Random\Randomizer::getInt, `random_int`
