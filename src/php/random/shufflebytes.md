---
title: Random\Randomizer::shuffleBytes
description: Devuelve una permutación por octeto de una cadena de caracteres
source_url: https://www.php.net/manual/es/random-randomizer.shufflebytes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/randomizer/shufflebytes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: true
translation_revision: '826073522'
order: 68240
---

Random\Randomizer::shuffleBytes

Devuelve una permutación por octeto de una cadena de caracteres

## Descripción

```php
public Random\Randomizer::shuffleBytes(string $bytes): string
```php

Devuelve una permutación seleccionada uniformemente de los `bytes` de entrada.

Cada permutación posible de los `bytes` de entrada tiene la misma probabilidad de ser devuelta.

## Parámetros

`bytes`  
La `string` cuyos octetos se mezclan.

La `string` de entrada no será modificada.

## Valores devueltos

Una permutación de los octetos de `bytes`.

## Errores/Excepciones

- Cualquier `Throwable` lanzado por el método Random\Engine::generate del [`Random\Randomizer::$engine`](#random-randomizer.props.engine) subyacente.

## Ejemplos

Ejemplo de `Random\Randomizer::shuffleBytes`

```
<?php
$r = new \Random\Randomizer();

// Mezclar los octetos en una cadena:
echo "«", $r->shuffleBytes("PHP is great!"), "»\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    « ga rHs!PPiet»

Mezcla por octeto de caracteres Unicode

```
<?php
$r = new \Random\Randomizer();

$unicode = "🍎, 🥝, 🍌, 🍑, 🍇";
$shuffled = $r->shuffleBytes( $unicode );

// La mezcla por octeto de caracteres no-ASCII los destruye,
// lo que resulta en secuencias inválidas (indicadas por el carácter
// de reemplazo Unicode) o incluso la aparición de caracteres
// completamente diferentes en la salida.
echo "Original: ", $unicode, "\n";
echo "Shuffled: «", $shuffled, "»\n";
echo "Shuffled Bytes: ", bin2hex($shuffled), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Original: 🍎, 🥝, 🍌, 🍑, 🍇
    Shuffled: «� ��,�����🍟,� �� �, �,��»
    Shuffled Bytes: 87208e912c8d9fa5f0f0f09f8d9f2cf09f208c9d20f02c209f2c8d8d
