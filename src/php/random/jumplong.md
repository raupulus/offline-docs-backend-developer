---
title: Random\Engine\Xoshiro256StarStar::jumpLong
description: Avanza de manera eficiente el motor 2^192 pasos
source_url: https://www.php.net/manual/es/random-engine-xoshiro256starstar.jumplong.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/engine/xoshiro256starstar/jumplong.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: true
translation_revision: '826073522'
order: 68110
---

Random\Engine\Xoshiro256StarStar::jumpLong

Avanza de manera eficiente el motor 2^192 pasos

## Descripción

```php
public Random\Engine\Xoshiro256StarStar::jumpLong(): void
```php

Avanza el estado del algoritmo 2<sup>192</sup> pasos, como si `Random\Engine\Xoshiro256StarStar::generate` fuera llamado 2<sup>192</sup> veces.

El objetivo de un salto largo es facilitar la creación de un nuevo `Random\Engine\Xoshiro256StarStar` a partir de un motor `Random\Engine\Xoshiro256StarStar` inicializado existente. El motor inicializado actúa como una plantilla, que puede ser [clonada](#language.oop5.cloning) y saltada repetidamente para crear 2<sup>64</sup> secuencias no superpuestas con 2<sup>192</sup> valores cada una.

Los saltos largos pueden combinarse con `Random\Engine\Xoshiro256StarStar::jump` para dividir aún más cada una de las 2<sup>64</sup> secuencias generadas por un salto largo, en 2<sup>64</sup> secuencias de 2<sup>128</sup> valores cada una.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `Random\Engine\Xoshiro256StarStar::jumpLong`

```
<?php
$blueprintRng = new \Random\Engine\Xoshiro256StarStar(0);

// Cada motor padre tendrá su propio trozo de 2**192 valores.
$parent1 = clone $blueprintRng;
$blueprintRng->jumpLong();

$parent2 = clone $blueprintRng;
$blueprintRng->jumpLong();

// Cada uno de los motores hijos tendrá su propio trozo de 2**128 valores
// tomados del trozo de 2**192 valores de su motor padre.
$child1a = clone $parent1;
$parent1->jump();
$child1b = clone $parent1;
$parent1->jump();

$child2a = clone $parent2;
$parent2->jump();
$child2b = clone $parent2;
$parent2->jump();

echo "Child 1A: ", bin2hex($child1a->generate()), "\n";
echo "Child 1B: ", bin2hex($child1b->generate()), "\n";
echo "Child 2A: ", bin2hex($child2a->generate()), "\n";
echo "Child 2B: ", bin2hex($child2b->generate()), "\n";
?>

   
```php

El ejemplo anterior mostrará:

    Child 1A: b4f275cb365fec99
    Child 1B: 2cd646c8ed156237
    Child 2A: eb3729a722a504e7
    Child 2B: d4208dc85bdd6dc3

## Véase también

Random\Engine\Xoshiro256StarStar::jump
