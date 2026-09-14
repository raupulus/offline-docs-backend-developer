---
title: str_shuffle
description: Mezcla los caracteres de un string
source_url: https://www.php.net/manual/es/function.str-shuffle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-shuffle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: d6dc2be3c
order: 89200
---

str_shuffle

Mezcla los caracteres de un string

## Descripción

```php
str_shuffle(string $string): string
```php

`str_shuffle` mezcla los caracteres de un string. Se crea una permutación entre todas las posibles.

> [!CAUTION]
> Esta función no genera valores criptográficamente seguros, y *no debe* ser utilizada con fines criptográficos, o con fines que requieran que los valores devueltos sean indescifrables.
>
> Si se requiere aleatoriedad criptográficamente segura, el `Random\Randomizer` puede ser utilizado con el motor `Random\Engine\Secure`. Para casos de uso simples, las funciones `random_int` y `random_bytes` proporcionan una API práctica y segura que es soportada por el CSPRNG del sistema operativo.

> [!CAUTION]
> Esta función utiliza la instancia global Mt19937 ("Mersenne Twister") como fuente de aleatoriedad y por lo tanto comparte su estado con todas las demás funciones que usan el Mt19937 global. El uso de cualquiera de estas funciones avanza la secuencia para *todas* las demás funciones, independientemente del ámbito.
>
> Generar secuencias repetibles inicializando `mt_srand` o `srand` con un valor conocido también producirá una salida repetible de esta función.
>
> Prefiera utilizar los métodos de `Random\Randomizer` en todo el código nuevo.

## Parámetros

`string`  
El string de entrada.

## Valores devueltos

Devuelve el string mezclado.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.1.0 | El algoritmo de aleatorización [ha sido modificado](#migration71.incompatible.rand-srand-aliases) para utilizar el Generador de Números Aleatorios [Mersenne Twister](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html) en lugar de la función rand de libc. |

## Ejemplos

Ejemplo con `str_shuffle`

```
<?php
$str = 'abcdef';
$shuffled = str_shuffle($str);

// Esto mostrará algo como: bfdaec
echo $shuffled;
?>

    
```php

## Véase también

`Random\Randomizer::shuffleBytes`, `Random\Randomizer::shuffleArray`
