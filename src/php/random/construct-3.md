---
title: Random\Engine\Xoshiro256StarStar::__construct
description: Crea un nuevo motor xoshiro256**
source_url: https://www.php.net/manual/es/random-engine-xoshiro256starstar.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/engine/xoshiro256starstar/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: 1bcc40f81
order: 68070
---

Random\Engine\Xoshiro256StarStar::\_\_construct

Crea un nuevo motor xoshiro256\*\*

## Descripción

```php
public Random\Engine\Xoshiro256StarStar::__construct([string $seed])
```php

## Parámetros

`seed`  
Cómo se inicializa el estado interno de 256 bits (32 bytes) compuesto por cuatro enteros sin signo de 64 bits depende del tipo utilizado como `seed`.

| Tipo | Descripción |
|----|----|
| `null` | Rellena el estado con 32 bytes aleatorios generados usando el CSPRNG. |
| `int` | Rellena el estado con cuatro valores consecutivos generados con el algoritmo SplitMix64 que se inicializó con `seed` interpretado como un entero sin signo de 64 bits. |
| `string` | Rellena el estado interpretando un `string` de 32 bytes como cuatro enteros sin signo de 64 bits en little-endian. |

## Errores/Excepciones

- Si la longitud de un `string` `seed` no es de 32 bytes, se lanzará un `ValueError`.

- Si un `string` `seed` consiste en 32 bytes NUL (`"\x00"`), se lanzará un `ValueError`.

## Ejemplos

`Random\Engine\Xoshiro256StarStar::__construct` ejemplo

```
<?php
// Usa una semilla aleatoria de 256 bits.
$e = new \Random\Engine\Xoshiro256StarStar();

$r = new \Random\Randomizer($e);
?>

   
```php

Derivando una semilla de un `string`

```
<?php
$string = "Mi semilla de string";

// Hashea el string con SHA-256 usando salida binaria para convertir el
// $string en una semilla de 256 bits. Usar el mismo string resultará
// en la misma secuencia de aleatoriedad.
$e = new \Random\Engine\Xoshiro256StarStar(
    hash('sha256', $string, binary: true)
);

echo bin2hex($e->generate()), "\n";
?>

   
```php

El ejemplo anterior mostrará:

    6e013453678388c2
