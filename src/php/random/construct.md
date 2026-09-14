---
title: Random\Engine\Mt19937::__construct
description: Construye un nuevo motor Mt19937
source_url: https://www.php.net/manual/es/random-engine-mt19937.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/engine/mt19937/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: 1bcc40f81
order: 67950
---

Random\Engine\Mt19937::\_\_construct

Construye un nuevo motor Mt19937

## Descripción

```php
public Random\Engine\Mt19937::__construct([int $seed], [int $mode])
```php

> [!CAUTION]
> Dado que el motor Mt19937 ("Mersenne Twister") toma un solo entero de 32 bits como semilla, el número de secuencias aleatorias posibles está limitado a solo 2<sup>32</sup> (por ejemplo 4 294 967 296), a pesar de la enorme período de Mt19937 de 2<sup>19937</sup>-1.
>
> Cuando se confía en una semilla aleatoria implícita o explícita, las duplicaciones aparecerán mucho antes. Las semillas duplicadas son esperadas con una probabilidad del 50% después de menos de 80 000 semillas generadas aleatoriamente según el problema del cumpleaños. Una probabilidad del 10% de una semilla duplicada ocurre después de haber generado aproximadamente 30 000 semillas de manera aleatoria.
>
> Esto hace que Mt19937 sea inadecuado para aplicaciones donde las secuencias duplicadas no deben ocurrir con más que una probabilidad despreciable. Si se requiere una semilla reproducible, tanto el motor `Random\Engine\Xoshiro256StarStar` como `Random\Engine\PcgOneseq128XslRr64` soportan semillas mucho más grandes que son poco propensas a colisionar aleatoriamente. Si la reproductibilidad no es requerida, el motor `Random\Engine\Secure` proporciona datos aleatorios criptográficamente seguros.

## Parámetros

`seed`  
Rellena el estado con valores generados con un generador congruencial lineal que fue inicializado con `seed` interpretado como un entero sin signo de 32 bits.

Si `seed` se omite o es `null`, se utilizará un entero sin signo de 32 bits aleatorio.

`mode`  
Utilice una de las siguientes constantes para especificar la implementación del algoritmo a usar. `MT_RAND_MT19937`: La implementación correcta de Mt19937., `MT_RAND_PHP`: Una implementación incorrecta para compatibilidad con versiones anteriores de `mt_srand` anterior a PHP 7.1.0.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.

## Ejemplos

Ejemplo de `Random\Engine\Mt19937::__construct`

```
<?php
// Usa una semilla aleatoria de 32 bits.
$e = new \Random\Engine\Mt19937();

$r = new \Random\Randomizer($e);
?>

   
```php
