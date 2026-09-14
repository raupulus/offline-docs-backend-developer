---
title: openssl_random_pseudo_bytes
description: Genera una cadena pseudo-aleatoria de octetos
source_url: https://www.php.net/manual/es/function.openssl-random-pseudo-bytes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-random-pseudo-bytes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: 52c495140
order: 59480
---

openssl_random_pseudo_bytes

Genera una cadena pseudo-aleatoria de octetos

## Descripción

```php
openssl_random_pseudo_bytes(int $length, [bool $strong_result]): string
```php

Genera una `string` pseudo-aleatoria de octetos, cuya longitud es especificada por el argumento `length`.

Indica asimismo si el algoritmo fuerte de criptología ha sido utilizado para producir estos octetos pseudo-aleatorios, utilizando el argumento `strong_result`.

## Parámetros

`length`  
El tamaño deseado para la cadena de octetos. Debe ser un número entero positivo inferior o igual a `2147483647`. PHP intentará convertir este argumento a un entero no nulo para utilizarlo.

`strong_result`  
Si se proporciona, determina si el algoritmo de criptología utilizado era criptológicamente fuerte, es decir, seguro para ser utilizado con GPG, contraseñas, etc. `true` si lo es, `false` en caso contrario.

## Valores devueltos

Devuelve la cadena de octetos generada.

## Errores/Excepciones

`openssl_random_pseudo_bytes` lanza una `Exception` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `strong_result` ahora es nullable. |
| 7.4.0 | La función ya no devuelve `false` en caso de error, sino que lanza una `Exception` en su lugar. |

## Ejemplos

Ejemplo `openssl_random_pseudo_bytes`

```
<?php
for ($i = 1; $i <= 4; $i++) {
    $bytes = openssl_random_pseudo_bytes($i, $cstrong);
    $hex   = bin2hex($bytes);

    echo "Longitud : Octetos : $i y Hex: " . strlen($hex) . PHP_EOL;
    var_dump($hex);
    var_dump($cstrong);
    echo PHP_EOL;
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Longitud : Octetos : 1 y Hex: 2
    string(2) "42"
    bool(true)

    Longitud : Octetos : 2 y Hex: 4
    string(4) "dc6e"
    bool(true)

    Longitud : Octetos : 3 y Hex: 6
    string(6) "288591"
    bool(true)

    Longitud : Octetos : 4 y Hex: 8
    string(8) "ab86d144"
    bool(true)

## Véase también

random_bytes

bin2hex

crypt

random_int
