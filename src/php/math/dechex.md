---
title: dechex
description: Convierte de decimal a hexadecimal
source_url: https://www.php.net/manual/es/function.dechex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/dechex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 44610
---

dechex

Convierte de decimal a hexadecimal

## Descripción

```php
dechex(int $num): string
```php

Retorna un string que contiene la representación hexadecimal del argumento `num` sin signo.

El número más grande que puede ser convertido es `PHP_INT_MAX``* 2 + 1` (o `-1`) : en plataformas de 32-bit, será `4294967295` en decimal, lo que hará que la función `dechex` retorne `ffffffff`.

## Parámetros

`num`  
El valor decimal a convertir.

Dado que el tipo `int` de PHP es firmado, pero que la función `dechex` solo funciona con enteros sin signo, los enteros negativos serán tratados como si fueran sin signo.

## Valores devueltos

Una representación hexadecimal de `num`.

## Ejemplos

Ejemplo con `dechex`

```
<?php
echo dechex(10) . "\n";
echo dechex(47);
?>

    
```php

El ejemplo anterior mostrará:

    a
    2f

Ejemplo con la función `dechex` con enteros grandes

```
<?php
// La salida a continuación asume que estamos en una plataforma de 32-bit.
// Note que la salida es idéntica para todos los valores.
echo dechex(-1)."\n";
echo dechex(PHP_INT_MAX * 2 + 1)."\n";
echo dechex(pow(2, 32) - 1)."\n";
?>

    
```php

El ejemplo anterior mostrará:

    ffffffff
    ffffffff
    ffffffff

## Véase también

`hexdec`, `decbin`, `decoct`, `base_convert`
