---
title: hash_hmac_file
description: Genera un valor de clave de hash utilizando el método HMAC y el contenido
  de un fichero dado
source_url: https://www.php.net/manual/es/function.hash-hmac-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-hmac-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: true
translation_revision: df2a77acb
order: 29300
---

hash_hmac_file

Genera un valor de clave de hash utilizando el método HMAC y el contenido de un fichero dado

## Descripción

```php
#[\SensitiveParameter] hash_hmac_file(string $algo, string $filename, string $key, [bool $binary]): string
```php

## Parámetros

`algo`  
Nombre del algoritmo de hash seleccionado (por ejemplo: `"sha256"`). Para una lista de los algoritmos soportados ver `hash_hmac_algos`.

> [!NOTE]
> Las funciones de hash no criptográficas no están autorizadas.

`filename`  
URL que indica la ubicación del fichero que será hasheado; Soporta las envolturas `fopen`.

`key`  
Clave secreta compartida utilizada para generar la varianza HMAC de la huella digital.

`binary`  
Cuando vale `true`, la salida será datos brutos binarios. Cuando vale `false`, la salida serán dígitos hexadecimales en minúscula.

## Valores devueltos

Devuelve una cadena de caracteres que contiene la huella digital calculada en dígitos hexadecimales en minúscula a menos que `binary` esté fijado a `true`. En este caso, se devuelve la representación bruta binaria de la huella digital. Devuelve `false` si el fichero `filename` no puede ser leído.

## Errores/Excepciones

Levanta una excepción `ValueError` si el parámetro `algo` es desconocido o no es una función de hash criptográfica.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | El uso de funciones de hash no criptográficas (adler32, crc32, crc32b, fnv132, fnv1a32, fnv164, fnv1a64, joaat) ha sido desactivado. |
| 8.0.0 | Levanta una excepción `ValueError` a partir de ahora si el parámetro `algo` es desconocido o no es una función de hash criptográfica; previamente, `false` era devuelto y se emitía un mensaje `E_WARNING`. |

## Ejemplos

Ejemplo con `hash_hmac_file`

```
<?php
/* Crea un fichero para calcular su huella digital */
file_put_contents('example.txt', 'The quick brown fox jumped over the lazy dog.');

echo hash_hmac_file('sha256', 'example.txt', 'secret');
?>

    
```php

El ejemplo anterior mostrará:

    9c5c42422b03f0ee32949920649445e417b2c634050833c5165704b825c2a53b

## Véase también

`hash_hmac`, `hash_hmac_algos`, `hash_init`, `hash_equals`
