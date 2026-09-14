---
title: gmp_random_range
description: Obtener un entero seleccionado uniformemente
source_url: https://www.php.net/manual/es/function.gmp-random-range.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-random-range.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: false
translation_revision: 45c190ae5
order: 28720
---

gmp_random_range

Obtener un entero seleccionado uniformemente

## Descripción

```php
gmp_random_range(GMP $min, GMP $max): GMP
```php

Genera un número aleatorio. El número estará en el intervalo `min` y `max`.

`min` y `max` pueden ser ambos negativos, pero `min` debe ser siempre inferior a `max`.

> [!CAUTION]
> Esta función no genera valores criptográficamente seguros, y *no debe* ser utilizada con fines criptográficos, o con fines que requieran que los valores devueltos sean indescifrables.
>
> Si se requiere aleatoriedad criptográficamente segura, el `Random\Randomizer` puede ser utilizado con el motor `Random\Engine\Secure`. Para casos de uso simples, las funciones `random_int` y `random_bytes` proporcionan una API práctica y segura que es soportada por el CSPRNG del sistema operativo.

## Parámetros

`min`  
Un número GMP que representa el límite inferior para el número aleatorio.

`max`  
Un número GMP que representa el límite superior para el número aleatorio.

## Valores devueltos

Devuelve un objeto `GMP` que contiene un entero seleccionado uniformemente en el intervalo cerrado \[`min`, `max`\]. `min` y `max` son ambos valores de retorno posibles.

## Errores/Excepciones

Si `max` es inferior a `min`, se lanzará una ValueError.

## Ejemplos

Ejemplo con `gmp_random_range`

```
<?php
$rand1 = gmp_random_range(0, 100);    // número aleatorio entre 0 y 100
$rand2 = gmp_random_range(-100, -10); // número aleatorio entre -100 y -10

echo gmp_strval($rand1) . "\n";
echo gmp_strval($rand2) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    42
    -67
