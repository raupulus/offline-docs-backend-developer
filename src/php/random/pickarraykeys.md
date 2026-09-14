---
title: Random\Randomizer::pickArrayKeys
description: Selecciona claves de array aleatorias
source_url: https://www.php.net/manual/es/random-randomizer.pickarraykeys.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/randomizer/pickarraykeys.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: true
translation_revision: '826073522'
order: 68210
---

Random\Randomizer::pickArrayKeys

Selecciona claves de array aleatorias

## Descripción

```php
public Random\Randomizer::pickArrayKeys(array $array, int $num): array
```php

Selecciona de manera uniforme `num` claves de array distintas del `array` de entrada.

Cada clave del `array` de entrada tiene la misma posibilidad de ser retornada.

> [!CAUTION]
> La selección de las claves de array depende de la estructura interna del `array` de entrada. Las claves de array retornadas pueden ser diferentes para dos arrays de entrada iguales y dos `Random\Engine`s con un estado idéntico, en función de la manera en que los arrays de entrada hayan sido creados.

## Parámetros

`array`  
El array cuyas claves de array son seleccionadas.

`num`  
El número de claves de array a retornar; debe estar comprendido entre `1` y el número de elementos en `array`.

## Valores devueltos

Un `array` que contiene `num` claves de array distintas de `array`.

El `array` retornado será una lista (`array_is_list`). Será un subconjunto del `array` retornado por `array_keys`.

## Errores/Excepciones

- Si `num` es inferior a `1` o superior al número de elementos en `array`, se lanzará una `ValueError`.

- Cualquier `Throwable` lanzado por el método Random\Engine::generate del [`Random\Randomizer::$engine`](#random-randomizer.props.engine) subyacente.

## Ejemplos

Ejemplo de `Random\Randomizer::pickArrayKeys`

```
<?php
$r = new \Random\Randomizer();

$fruits = [ 'red' => '🍎', 'green' => '🥝', 'yellow' => '🍌', 'pink' => '🍑', 'purple' => '🍇' ];

// Toma 2 claves de array aleatorias:
echo "Keys: ", implode(', ', $r->pickArrayKeys($fruits, 2)), "\n";

// Toma 3 otras claves:
echo "Keys: ", implode(', ', $r->pickArrayKeys($fruits, 3)), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Keys: yellow, purple
    Keys: red, green, yellow

Tomar valores aleatorios

```
<?php
$r = new \Random\Randomizer();

$fruits = [ 'red' => '🍎', 'green' => '🥝', 'yellow' => '🍌', 'pink' => '🍑', 'purple' => '🍇' ];

$keys = $r->pickArrayKeys($fruits, 2);
// Ver los valores para las claves seleccionadas.
$selection = array_map(
    static fn ($key) => $fruits[$key],
    $keys
);

echo "Values: ", implode(', ', $selection), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Values: 🍎, 🍇

## Véase también

array_keys
