---
title: Random\Randomizer::nextInt
description: Obtener un entero positivo
source_url: https://www.php.net/manual/es/random-randomizer.nextint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/randomizer/nextint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: 1bcc40f81
order: 68200
---

Random\Randomizer::nextInt

Obtener un entero positivo

## Descripción

```php
public Random\Randomizer::nextInt(): int
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un entero positivo entre 0 y un valor máximo que depende del número de bytes devueltos por Random\Engine::generate. El valor máximo exacto puede calcularse como 2<sup>\$engine_bytes \* 8 - 1</sup> - 1.

## Errores/Excepciones

- Para evitar inconsistencias, PHP de 32 bits lanzará `Random\RandomException` si el tamaño de salida de Random\Engine::generate excede 32 bits, ya que el entero seleccionado no puede devolverse sin pérdida. Esto afecta a los motores nativos de 64 bits `Random\Engine\PcgOneseq128XslRr64` y `Random\Engine\Xoshiro256StarStar`. Cualquier motor de usuario que devuelva más de 4 bytes de aleatoriedad también se ve afectado.

- Cualquier `Throwable` lanzado por el método Random\Engine::generate del [`Random\Randomizer::$engine`](#random-randomizer.props.engine) subyacente.

## Ejemplos

`Random\Randomizer::nextInt` ejemplo

```
<?php
$r = new \Random\Randomizer();

// Entero "next" aleatorio:
echo $r->nextInt(), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    8041689838856078718
