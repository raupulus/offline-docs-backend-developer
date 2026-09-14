---
title: hash_algos
description: Devuelve una lista de los algoritmos de hash registrados
source_url: https://www.php.net/manual/es/function.hash-algos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-algos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: false
translation_revision: 71e12e2df
order: 29230
---

hash_algos

Devuelve una lista de los algoritmos de hash registrados

## Descripción

```php
hash_algos(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array indexado numéricamente que contiene la lista de algoritmos de hash disponibles.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Se ha añadido soporte para MurmurHash3 y xxHash. |
| 7.4.0 | Se ha añadido soporte para crc32c. |
| 7.1.0 | Se ha añadido soporte para sha512/224, sha512/256, sha3-224, sha3-256, sha3-384 y sha3-512. |

## Ejemplos

Ejemplo con `hash_algos`

A partir de PHP 8.1.0, `hash_algos` devolverá la siguiente lista de algoritmos:

```
<?php
print_r(hash_algos());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => md2
        [1] => md4
        [2] => md5
        [3] => sha1
        [4] => sha224
        [5] => sha256
        [6] => sha384
        [7] => sha512/224
        [8] => sha512/256
        [9] => sha512
        [10] => sha3-224
        [11] => sha3-256
        [12] => sha3-384
        [13] => sha3-512
        [14] => ripemd128
        [15] => ripemd160
        [16] => ripemd256
        [17] => ripemd320
        [18] => whirlpool
        [19] => tiger128,3
        [20] => tiger160,3
        [21] => tiger192,3
        [22] => tiger128,4
        [23] => tiger160,4
        [24] => tiger192,4
        [25] => snefru
        [26] => snefru256
        [27] => gost
        [28] => gost-crypto
        [29] => adler32
        [30] => crc32
        [31] => crc32b
        [32] => crc32c
        [33] => fnv132
        [34] => fnv1a32
        [35] => fnv164
        [36] => fnv1a64
        [37] => joaat
        [38] => murmur3a
        [39] => murmur3c
        [40] => murmur3f
        [41] => xxh32
        [42] => xxh64
        [43] => xxh3
        [44] => xxh128
        [45] => haval128,3
        [46] => haval160,3
        [47] => haval192,3
        [48] => haval224,3
        [49] => haval256,3
        [50] => haval128,4
        [51] => haval160,4
        [52] => haval192,4
        [53] => haval224,4
        [54] => haval256,4
        [55] => haval128,5
        [56] => haval160,5
        [57] => haval192,5
        [58] => haval224,5
        [59] => haval256,5
    )

## Véase también

hash

hash_hmac_algos
