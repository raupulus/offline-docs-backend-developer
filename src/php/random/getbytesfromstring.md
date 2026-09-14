---
title: Random\Randomizer::getBytesFromString
description: Devuelve bytes aleatorios a partir de una cadena
source_url: https://www.php.net/manual/es/random-randomizer.getbytesfromstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/randomizer/getbytesfromstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: true
translation_revision: 6b62527df
order: 68160
---

Random\Randomizer::getBytesFromString

Devuelve bytes aleatorios a partir de una cadena

## Descripción

```php
public Random\Randomizer::getBytesFromString(string $string, int $length): string
```php

Genera una cadena que contiene bytes aleatorios seleccionados uniformemente de la `string` de entrada con la `length` solicitada.

La probabilidad de que un byte sea seleccionado es proporcional a su parte de la `string` de entrada. Si cada byte ocurre el mismo número de veces, cada byte tiene la misma probabilidad de ser seleccionado.

## Parámetros

`string`  
La `string` de entrada a partir de la cual se seleccionan los bytes devueltos.

`length`  
La longitud de la cadena aleatoria `string` que debe ser devuelta en bytes; debe ser `1` o más.

## Valores devueltos

Una `string` que contiene el número solicitado de bytes aleatorios tomados de la entrada `string`.

## Errores/Excepciones

- Si `string` está vacía, se lanzará una `ValueError`.

- Si el valor de `length` es inferior a `1`, se lanzará una `ValueError`.

- Cualquier `Throwable` lanzado por el método Random\Engine::generate del [`Random\Randomizer::$engine`](#random-randomizer.props.engine) subyacente.

## Ejemplos

Ejemplo de Random\Randomizer::getBytesFromString

```
<?php
$randomizer = new \Random\Randomizer();

printf(
    "%s.example.com",
    $randomizer->getBytesFromString('abcdefghijklmnopqrstuvwxyz0123456789', 16)
);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    3zsw04eiubcf82jd.example.com

Generar un código aleatorio para la autenticación multi-factor

```
<?php
// El motor Secure es el motor por omisión, pero se hace explícito, ya que
// los códigos multi-factor son sensibles a la seguridad.
$randomizer = new \Random\Randomizer(new \Random\Engine\Secure());

echo implode('-', str_split($randomizer->getBytesFromString('0123456789', 20), 5));
?>

   
```php

Resultado del ejemplo anterior es similar a:

    11551-80418-27047-42075

Seleccionar a partir de una cadena con una distribución no uniforme

```
<?php
$randomizer = new \Random\Randomizer();

echo $randomizer->getBytesFromString('aaaaabcdef', 20);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    fddacbeaaeaaacaaaaca

## Véase también

Random\Randomizer::getBytes
