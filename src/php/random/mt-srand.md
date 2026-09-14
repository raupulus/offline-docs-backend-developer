---
title: mt_srand
description: Inicializa el generador de números aleatorios Mersenne Twister
source_url: https://www.php.net/manual/es/function.mt-srand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/functions/mt-srand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: true
translation_revision: 9eb92e5c1
order: 67890
---

mt_srand

Inicializa el generador de números aleatorios Mersenne Twister

## Descripción

```php
mt_srand([int $seed], [int $mode]): void
```php

`mt_srand` inicializa el generador de valores aleatorios con `seed` o con un valor aleatorio si ningún parámetro `seed` es proporcionado.

> [!NOTE]
> No es necesario inicializar el generador de números aleatorios con `srand` o `mt_srand`, esto se hace automáticamente.

> [!CAUTION]
> Dado que el motor Mt19937 ("Mersenne Twister") toma un solo entero de 32 bits como semilla, el número de secuencias aleatorias posibles está limitado a solo 2<sup>32</sup> (por ejemplo 4 294 967 296), a pesar de la enorme período de Mt19937 de 2<sup>19937</sup>-1.
>
> Cuando se confía en una semilla aleatoria implícita o explícita, las duplicaciones aparecerán mucho antes. Las semillas duplicadas son esperadas con una probabilidad del 50% después de menos de 80 000 semillas generadas aleatoriamente según el problema del cumpleaños. Una probabilidad del 10% de una semilla duplicada ocurre después de haber generado aproximadamente 30 000 semillas de manera aleatoria.
>
> Esto hace que Mt19937 sea inadecuado para aplicaciones donde las secuencias duplicadas no deben ocurrir con más que una probabilidad despreciable. Si se requiere una semilla reproducible, tanto el motor `Random\Engine\Xoshiro256StarStar` como `Random\Engine\PcgOneseq128XslRr64` soportan semillas mucho más grandes que son poco propensas a colisionar aleatoriamente. Si la reproductibilidad no es requerida, el motor `Random\Engine\Secure` proporciona datos aleatorios criptográficamente seguros.

## Parámetros

`seed`  
Rellena el estado con valores generados por un generador congruencial lineal que ha sido inicializado con `seed` interpretado como un entero sin signo de 32 bits.

Si `seed` es omitido o `null`, un entero sin signo de 32 bits será utilizado de manera aleatoria.

`mode`  
Utilice una de las constantes siguientes para especificar la implementación del algoritmo a utilizar. `MT_RAND_MT19937`: La implementación correcta de Mt19937, disponible a partir de PHP 7.1.0., `MT_RAND_PHP` Utiliza una implementación incorrecta de Mersenne Twister que era el valor por omisión antes de PHP 7.1.0. Este modo está disponible para asegurar la compatibilidad ascendente.

> [!WARNING]
> Esta característica está *OBSOLETA* a partir de PHP 8.3.0. Depender de esta característica está altamente desaconsejado.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | `seed` es ahora nullable. |
| 7.1.0 | `srand` [ha sido cambiado](#migration71.incompatible.rand-srand-aliases) para ser un alias de `mt_srand`. |
| 7.1.0 | `mt_rand` [ha sido actualizado](#migration71.incompatible.fixes-to-mt_rand-algorithm) para utilizar la versión corregida, correcta del algoritmo de Mersenne Twister. Para volver al comportamiento anterior, utilice `mt_srand` con `MT_RAND_PHP` como segundo parámetro. |

## Véase también

`mt_rand`, `mt_getrandmax`, `srand`
