---
title: Random\Randomizer::getBytes
description: Devuelve bytes aleatorios
source_url: https://www.php.net/manual/es/random-randomizer.getbytes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/randomizer/getbytes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: true
translation_revision: f08b9a8ae
order: 68150
---

Random\Randomizer::getBytes

Devuelve bytes aleatorios

## Descripción

```php
public Random\Randomizer::getBytes(int $length): string
```php

Genera una cadena que contiene bytes aleatorios seleccionados uniformemente de la `length` solicitada.

Dado que los bytes devueltos se seleccionan de manera completamente aleatoria, la cadena resultante puede contener caracteres no imprimibles o secuencias UTF-8 no válidas. Puede ser necesario codificarla antes de transmitirla o mostrarla.

## Parámetros

`length`  
La longitud de la cadena aleatoria `string` que debe ser devuelta en bytes; debe ser `1` o más.

## Valores devueltos

Una `string` que contiene el número solicitado de bytes aleatorios.

## Errores/Excepciones

- Si el valor de `length` es inferior a `1`, se lanzará una `ValueError`.

- Cualquier `Throwable` lanzado por el método Random\Engine::generate del [`Random\Randomizer::$engine`](#random-randomizer.props.engine) subyacente.

## Ejemplos

Ejemplo de `Random\Randomizer::getBytes`

```
<?php
$r = new \Random\Randomizer();

echo bin2hex($r->getBytes(8)), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    ebdbe93cd56682c2

## Véase también

random_bytes

bin2hex

base64_encode

Random\Randomizer::getBytesFromString
