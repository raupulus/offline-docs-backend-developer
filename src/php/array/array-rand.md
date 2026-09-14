---
title: array_rand
description: Toma una o varias claves, al azar en un array
source_url: https://www.php.net/manual/es/function.array-rand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-rand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_reviewed: false
translation_revision: d6dc2be3c
order: 5520
---

array_rand

Toma una o varias claves, al azar en un array

## Descripción

```php
array_rand(array $array, [int $num]): int
```php

Selecciona uno o varios valores al azar en un array y devuelve la o las claves de estos valores.

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
El array de entrada. No puede estar vacío.

`num`  
Especifica el número de entradas que se desean recuperar. Debe ser mayor a cero e inferior o igual a la longitud de `array`.

## Valores devueltos

Cuando se recupera una sola entrada, la función `array_rand` devuelve la clave de una entrada elegida al azar. De lo contrario, se devolverá un array de claves de entradas aleatorias. Esto permite hacer una selección al azar de claves, o bien de valores. Si se devuelven varias claves, entonces lo serán en el orden en que estaban en el array original.

## Errores/Excepciones

Lanza una `ValueError` si `array` está vacío, o si `num` está fuera de rango.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `array_rand` ahora lanza una `ValueError` si `num` está fuera de rango; anteriormente, se generaba un `E_WARNING` y la función devolvía `null`. |
| 8.0.0 | `array_rand` ahora lanza una `ValueError` si `array` está vacío; anteriormente, se generaba un `E_WARNING` y la función devolvía `null`. |
| 7.1.0 | El algoritmo interno de generación aleatoria [ha sido modificado](#migration71.incompatible.rand-srand-aliases) para usar el generador de números aleatorios [ Mersenne Twister](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html) en lugar de la función aleatoria libc |

## Ejemplos

Ejemplo con `array_rand`

```
<?php
$input = array("Neo", "Morpheus", "Trinity", "Cypher", "Tank");
$rand_keys = array_rand($input, 2);
echo $input[$rand_keys[0]] . "\n";
echo $input[$rand_keys[1]] . "\n";
?>

    
```php

## Véase también

`Random\Randomizer::pickArrayKeys`, `Random\Randomizer::shuffleArray`
