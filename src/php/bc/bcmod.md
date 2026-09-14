---
title: bcmod
description: Devuelve el resto de una división entre números de gran tamaño
source_url: https://www.php.net/manual/es/function.bcmod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcmod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6280
---

bcmod

Devuelve el resto de una división entre números de gran tamaño

## Descripción

```php
bcmod(string $num1, string $num2, [int $scale]): string
```php

Devuelve el resto de la división entre `num1` utilizando `num2`. El resultado tiene el mismo signo que `num1`.

## 

## Valores devueltos

Devuelve el módulo, en forma de `string`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `scale` ahora es nullable. |
| 8.0.0 | La división por `0` ahora lanza una excepción DivisionByZeroError en lugar de devolver null. |
| 7.2.0 | `num1` y `num2` ya no se truncan a enteros. El comportamiento de `bcmod` sigue a `fmod` en lugar del operador `%`. |
| 7.2.0 | Se ha añadido el parámetro `scale`. |

## Ejemplos

Ejemplo con `bcmod`

```
<?php
bcscale(0);
echo bcmod( '5',  '3'); //  2
echo bcmod( '5', '-3'); //  2
echo bcmod('-5',  '3'); // -2
echo bcmod('-5', '-3'); // -2
?>

   
```php

`bcmod` con decimales

```
<?php
bcscale(1);
echo bcmod('5.7', '1.3'); // 0.5 desde PHP 7.2.0; 0 anteriormente
?>

   
```php

## Véase también

`bcdiv`, `bcdivmod`, BcMath\Number::mod
