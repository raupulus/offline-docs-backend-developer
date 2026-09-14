---
title: hash_hmac_algos
description: Devuelve una lista de algoritmos de hash registrados adecuados para hash_hmac
source_url: https://www.php.net/manual/es/function.hash-hmac-algos.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-hmac-algos.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: false
translation_revision: 7f99d5e48
order: 29290
---

hash_hmac_algos

Devuelve una lista de algoritmos de hash registrados adecuados para hash_hmac

## Descripción

```php
hash_hmac_algos(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array indexado numéricamente que contiene la lista de todos los algoritmos de hash disponibles que son adecuados para `hash_hmac`.

## Ejemplos

Ejemplo con `hash_hmac_algos`

```
<?php
print_r(hash_hmac_algos());

   
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
        [29] => haval128,3
        [30] => haval160,3
        [31] => haval192,3
        [32] => haval224,3
        [33] => haval256,3
        [34] => haval128,4
        [35] => haval160,4
        [36] => haval192,4
        [37] => haval224,4
        [38] => haval256,4
        [39] => haval128,5
        [40] => haval160,5
        [41] => haval192,5
        [42] => haval224,5
        [43] => haval256,5
    )

## Notas

> [!NOTE]
> Antes de PHP 7.2.0 la única forma de recuperar una lista de los algoritmos disponibles era llamar a `hash_algos` que también devolvía algoritmos que no son adecuados para `hash_hmac`.

## Véase también

hash_hmac

hash_algos
