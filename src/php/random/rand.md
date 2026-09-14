---
title: rand
description: Genera un valor aleatorio
source_url: https://www.php.net/manual/es/function.rand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/functions/rand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: d6dc2be3c
order: 67900
---

rand

Genera un valor aleatorio

## Descripción

```php
rand(): int
```php

```php
rand(int $min, int $max): int
```

Llamada sin los argumentos `min` y `max`, `rand` devuelve un número pseudoaleatorio entre 0 y `getrandmax`. Si se desea un número aleatorio entre 5 y 15 (inclusive), por ejemplo, se puede utilizar `rand (5, 15)`.

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

> [!NOTE]
> Antes de PHP 7.1.0, `getrandmax` valía solo 32767 en ciertas plataformas (como Windows). Si se necesita un rango superior a 32767, se recomienda especificar un valor límite superior a 32767, al especificar `min` y `max`, se permitirá utilizar un intervalo más grande que `mt_getrandmax`, o bien, utilizar la función `mt_rand` en su lugar.

> [!NOTE]
> A partir de PHP 7.1.0, `rand` utiliza el mismo generador de números aleatorios que `mt_rand`. Para preservar la compatibilidad ascendente, `rand` permite que `max` sea más pequeño que `min` en oposición al retorno `false` de `mt_rand`

## Parámetros

`min`  
El valor más pequeño a devolver (por omisión, 0)

`max`  
El valor más grande a devolver (por omisión, `mt_getrandmax`)

## Valores devueltos

Un valor pseudoaleatorio, comprendido entre `min` (o 0) y `max` (o `mt_getrandmax`, inclusive).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | `rand` [recibió una corrección de error](#migration72.incompatible.rand-mt_rand-output) para un bug de polarización módulo. Esto significa que las secuencias generadas en ciertos casos específicos pueden diferir de PHP 7.1 en las máquinas de 64 bits. |
| 7.1.0 | `rand` [fue hecho](#migration71.incompatible.rand-srand-aliases) un alias de `mt_rand`. |

## Ejemplos

Ejemplo con `rand`

```php
<?php
echo rand(), "\n";
echo rand(), "\n";

echo rand(5, 15), "\n";
?>

    
```

Resultado del ejemplo anterior es similar a:

    7771
    22264
    11

## Notas

> [!WARNING]
> El rango `min` `max` debe situarse dentro del rango `getrandmax`. es decir, abs(`max` - `min`) \<= `getrandmax`. De lo contrario, `rand` puede devolver números aleatorios de mala calidad.

## Véase también

`srand`, `getrandmax`, `mt_rand`, `random_int`, `random_bytes`
