---
title: mcrypt_list_algorithms
description: Lista todos los algoritmos de cifrado soportados
source_url: https://www.php.net/manual/es/function.mcrypt-list-algorithms.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-list-algorithms.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45900
---

mcrypt_list_algorithms

Lista todos los algoritmos de cifrado soportados

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_list_algorithms([string $lib_dir]): array
```php

Lista todos los algoritmos de cifrado de `lib_dir`.

## Parámetros

`lib_dir`  
Especifica el directorio donde se encuentran los algoritmos. Si se omite, se utiliza el valor de la directiva `mcrypt.algorithms_dir` del fichero `php.ini`.

## Valores devueltos

Devuelve un array con los algoritmos soportados.

## Ejemplos

Ejemplo con `mcrypt_list_algorithms`

```
<?php
$algorithms = mcrypt_list_algorithms();
print_r($algorithms);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => cast-128
        [1] => gost
        [2] => rijndael-128
        [3] => twofish
        [4] => arcfour
        [5] => cast-256
        [6] => loki97
        [7] => rijndael-192
        [8] => saferplus
        [9] => wake
        [10] => blowfish-compat
        [11] => des
        [12] => rijndael-256
        [13] => serpent
        [14] => xtea
        [15] => blowfish
        [16] => enigma
        [17] => rc2
        [18] => tripledes
    )
