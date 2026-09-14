---
title: Random\Randomizer::shuffleArray
description: Devuelve una permutación de un array
source_url: https://www.php.net/manual/es/random-randomizer.shufflearray.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/randomizer/shufflearray.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: true
translation_revision: '826073522'
order: 68230
---

Random\Randomizer::shuffleArray

Devuelve una permutación de un array

## Descripción

```php
public Random\Randomizer::shuffleArray(array $array): array
```php

Devuelve una permutación seleccionada uniformemente del `array` de entrada.

Cada permutación posible del `array` de entrada tiene la misma probabilidad de ser devuelta.

## Parámetros

`array`  
El `array` cuyos valores se mezclan.

El `array` de entrada no será modificado.

## Valores devueltos

Una permutación de los valores de `array`.

Las claves del `array` de entrada no serán preservadas; el `array` devuelto será una lista (`array_is_list`).

## Errores/Excepciones

- Cualquier `Throwable` lanzado por el método Random\Engine::generate del [`Random\Randomizer::$engine`](#random-randomizer.props.engine) subyacente.

## Ejemplos

Ejemplo de `Random\Randomizer::shuffleArray`

```
<?php
$r = new \Random\Randomizer();

$fruits = [ 'red' => '🍎', 'green' => '🥝', 'yellow' => '🍌', 'pink' => '🍑', 'purple' => '🍇' ];

// Mezclar el array:
echo "Ensalada: ", implode(', ', $r->shuffleArray($fruits)), "\n";

// Mezclar nuevamente:
echo "Otra Ensalada: ", implode(', ', $r->shuffleArray($fruits)), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ensalada: 🍎, 🥝, 🍇, 🍌, 🍑
    Otra Ensalada: 🍑, 🍇, 🥝, 🍎, 🍌
