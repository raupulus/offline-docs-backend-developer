---
title: Random\Engine\Xoshiro256StarStar::jump
description: Avanza el motor de manera eficiente 2^128 pasos
source_url: https://www.php.net/manual/es/random-engine-xoshiro256starstar.jump.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/engine/xoshiro256starstar/jump.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: true
translation_revision: 6756cbedb
order: 68100
---

Random\Engine\Xoshiro256StarStar::jump

Avanza el motor de manera eficiente 2^128 pasos

## Descripción

```php
public Random\Engine\Xoshiro256StarStar::jump(): void
```php

Avanza el estado del algoritmo 2<sup>128</sup> pasos, como si `Random\Engine\Xoshiro256StarStar::generate` fuera llamado 2<sup>128</sup> veces.

El objetivo de un salto es facilitar la creación de un nuevo motor `Random\Engine\Xoshiro256StarStar` a partir de un motor `Random\Engine\Xoshiro256StarStar` existente inicializado. El motor inicializado actúa como un modelo, que puede ser [clonado](#language.oop5.cloning) y saltado varias veces para crear 2<sup>128</sup> secuencias no superpuestas con 2<sup>128</sup> valores cada una.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Random\Engine\Xoshiro256StarStar::jump`

```
<?php
use Random\Engine\Xoshiro256StarStar;
use Random\Randomizer;

$blueprintRng = new Xoshiro256StarStar(0);

$fibers = [];
for ($i = 0; $i < 8; $i++) {
    $fiberRng = clone $blueprintRng;
    $blueprintRng->jump();

    $fiber = new Fiber(static function () use ($fiberRng, $i): void {
        $randomizer = new Randomizer($fiberRng);

        while (true) {
            Fiber::suspend();

            echo "{$i}: ", $randomizer->getInt(0, 100), "\n";
        }
    });
    $fiber->start();

    $fibers[] = $fiber;
}

// Aunque las fibras se ejecuten en un orden aleatorio, imprimirán el mismo valor
// cada vez, ya que cada una tiene su propia instancia única del RNG.
$randomizer = new Randomizer();

$fibers = $randomizer->shuffleArray($fibers);
foreach ($fibers as $fiber) {
    $fiber->resume();
}

$fibers = $randomizer->shuffleArray($fibers);
foreach ($fibers as $fiber) {
    $fiber->resume();
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    4: 89
    3: 10
    2: 63
    1: 75
    6: 41
    5: 56
    0: 16
    7: 60
    7: 34
    6: 58
    1: 74
    4: 63
    3: 3
    5: 42
    2: 45
    0: 86

## Véase también

Random\Engine\Xoshiro256StarStar::jumpLong
