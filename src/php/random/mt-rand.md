---
title: mt_rand
description: Genera un valor aleatorio mediante el generador de números aleatorios
  Mersenne Twister
source_url: https://www.php.net/manual/es/function.mt-rand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/functions/mt-rand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: d6dc2be3c
order: 67880
---

mt_rand

Genera un valor aleatorio mediante el generador de números aleatorios Mersenne Twister

## Descripción

```php
mt_rand(): int
```php

```php
mt_rand(int $min, int $max): int
```

Muchos generadores de números aleatorios provenientes de viejas bibliotecas libcs tienen comportamientos dudosos y son muy lentos. `mt_rand` es una función de reemplazo para `rand`. Utiliza un generador de números aleatorios de característica conocida, el " [Mersenne Twister](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html) " que es 4 veces más rápido que la función estándar libc.

Llamada sin los argumentos opcionales `min` y `max`, `mt_rand` devuelve un número pseudoaleatorio, entre 0 y `mt_getrandmax`. Para obtener un número entre 5 y 15 inclusive, se debe utilizar `mt_rand(5,15)`.

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

`min`  
Valor más bajo que puede ser devuelto (por omisión: 0)

`max`  
Valor más alto que puede ser devuelto (por omisión: `mt_getrandmax`).

## Valores devueltos

Un `int` aleatorio comprendido entre `min` (o 0) y `max` (o `mt_getrandmax`, inclusivo).

## Errores/Excepciones

- Si `max` es inferior a `min`, se lanzará una excepción `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Se lanzará una excepción `ValueError` si `max` es inferior a `min`; anteriormente, se emitía un `E_WARNING` y la función devolvía `false`. |
| 7.2.0 | `mt_rand` [recibió una corrección de error](#migration72.incompatible.rand-mt_rand-output) para un bug de polarización módulo. Esto significa que las secuencias generadas con un valor de inicialización específico pueden diferir de PHP 7.1 en máquinas de 64 bits. |
| 7.1.0 | `rand` [se convirtió](#migration71.incompatible.rand-srand-aliases) en un alias de `mt_rand`. |
| 7.1.0 | `mt_rand` [fue actualizado](#migration71.incompatible.fixes-to-mt_rand-algorithm) para utilizar la versión corregida, correcta, del algoritmo Twister Mersenne. Para volver al comportamiento anterior, utilice `mt_srand` con `MT_RAND_PHP` como segundo parámetro. |

## Ejemplos

Ejemplo con `mt_rand`

```php
<?php
echo mt_rand(), "\n";
echo mt_rand(), "\n";

echo mt_rand(5, 15), "\n";
?>

    
```

Resultado del ejemplo anterior es similar a:

    1604716014
    1478613278
    6

## Notas

> [!WARNING]
> El rango `min` `max` debe estar dentro del rango `mt_getrandmax`. es decir, (`max` - `min`) \<= `mt_getrandmax` de lo contrario, `mt_rand` puede devolver números aleatorios de menor calidad de lo que debería.

## Véase también

`mt_srand`, `mt_getrandmax`, `random_int`, `random_bytes`
