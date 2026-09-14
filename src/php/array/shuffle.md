---
title: shuffle
description: Mezcla los elementos de un array
source_url: https://www.php.net/manual/es/function.shuffle.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/shuffle.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: d6dc2be3c
order: 5960
---

shuffle

Mezcla los elementos de un array

## Descripción

```php
shuffle(array $array): true
```php

Mezcla los elementos del array `array`.

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

`array`  
El array.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.1.0 | El algoritmo interno de generación aleatoria [ha sido modificado](#migration71.incompatible.rand-srand-aliases) para utilizar el generador de números aleatorios [ Mersenne Twister](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html) en lugar de la función libc rand. |

## Ejemplos

Ejemplo con `shuffle`

```
<?php
$numbers = range(1, 20);
shuffle($numbers);
foreach ($numbers as $number) {
    echo "$number ";
}
?>

    
```php

## Notas

> [!NOTE]
> Esta función asigna nuevas claves a los elementos en `array`. Eliminará todas las claves existentes que hayan podido ser asignadas, en lugar de reordenar las claves.

> [!NOTE]
> Reinicia el puntero interno del array al primer elemento.

## Véase también

`Random\Randomizer::shuffleArray`, `Random\Randomizer::shuffleBytes`, `Random\Randomizer::pickArrayKeys`, Las funciones de [ordenación de arrays](#array.sorting)
