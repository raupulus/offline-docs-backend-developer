---
title: gmp_random_bits
description: Genera un número aleatorio
source_url: https://www.php.net/manual/es/function.gmp-random-bits.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/functions/gmp-random-bits.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 28710
---

gmp_random_bits

Genera un número aleatorio

## Descripción

```php
gmp_random_bits(int $bits): GMP
```php

Genera un número aleatorio. El número estará en el intervalo `0` y `2$bits - 1`.

El argumento `bits` debe ser mayor que 0, y el valor máximo estará restringido por la memoria disponible.

> [!CAUTION]
> Esta función no genera valores criptográficamente seguros, y *no debe* ser utilizada con fines criptográficos, o con fines que requieran que los valores devueltos sean indescifrables.
>
> Si se requiere aleatoriedad criptográficamente segura, el `Random\Randomizer` puede ser utilizado con el motor `Random\Engine\Secure`. Para casos de uso simples, las funciones `random_int` y `random_bytes` proporcionan una API práctica y segura que es soportada por el CSPRNG del sistema operativo.

## Parámetros

`bits`  
El número de bits a generar.

## Valores devueltos

Un número GMP aleatorio.

## Errores/Excepciones

Si `bits` es menor que `1`, se lanzará una ValueError.

## Ejemplos

Ejemplo con `gmp_random_bits`

```
<?php
$rand1 = gmp_random_bits(3); // número aleatorio entre 0 y 7
$rand2 = gmp_random_bits(5); // número aleatorio entre 0 y 31

echo gmp_strval($rand1) . "\n";
echo gmp_strval($rand2) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    3
    15
