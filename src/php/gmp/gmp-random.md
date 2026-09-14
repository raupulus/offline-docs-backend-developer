---
title: gmp_random
description: Número GMP aleatorio
source_url: https://www.php.net/manual/es/function.gmp-random.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-random.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: true
translation_revision: 7916b9cb9
order: 28740
---

gmp_random

Número GMP aleatorio

> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 7.2.0 y ha sido *ELIMINADA* a partir de PHP 8.0.0.

## Descripción

```php
gmp_random([int $limiter]): GMP
```php

Genera un número aleatorio. Este número estará comprendido entre cero y (2 \*\* n) -1, donde n es el número de bits por limb multiplicado por `limiter`. Si `limiter` es negativo, se genera un número negativo.

Un limb es un mecanismo interno de GMP. El número de bits en un limb no es estático, y puede variar entre los sistemas. En general, el número de bits por limb es 32 o 64, pero esto no está garantizado.

> [!CAUTION]
> Esta función no genera valores criptográficamente seguros, y *no debe* ser utilizada con fines criptográficos, o con fines que requieran que los valores devueltos sean indescifrables.
>
> Si se requiere aleatoriedad criptográficamente segura, el `Random\Randomizer` puede ser utilizado con el motor `Random\Engine\Secure`. Para casos de uso simples, las funciones `random_int` y `random_bytes` proporcionan una API práctica y segura que es soportada por el CSPRNG del sistema operativo.

## Parámetros

`limiter`  
El limitador.

Un objeto `GMP`, un `int`, o un `string` que puede ser interpretado como un número siguiendo la misma lógica que si la cadena fuera usada en `gmp_init` con detección automática de la base (es decir cuando `base` es igual a 0).

## Valores devueltos

Un número GMP aleatorio.

## Ejemplos

Ejemplo con `gmp_random`

```
<?php
$rand1 = gmp_random(1); // número aleatorio de 0 a 1 * bits por limb
$rand2 = gmp_random(2); // número aleatorio de 0 a 2 * bits por limb

echo gmp_strval($rand1) . "\n";
echo gmp_strval($rand2) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    1915834968
    8642564075890328087
