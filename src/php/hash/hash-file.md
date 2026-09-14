---
title: hash_file
description: Genera un valor de hash utilizando el contenido de un fichero dado
source_url: https://www.php.net/manual/es/function.hash-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: true
translation_revision: 05b26e8d7
order: 29260
---

hash_file

Genera un valor de hash utilizando el contenido de un fichero dado

## Descripción

```php
hash_file(string $algo, string $filename, [bool $binary], [array $options]): string
```php

## Parámetros

`algo`  
Nombre del algoritmo de hash seleccionado (por ejemplo: `"sha256"`). Para una lista de los algoritmos disponibles ver `hash_algos`.

`filename`  
URL que indica la ubicación del fichero que será hasheado; Soporta los envolventes `fopen`.

`binary`  
Cuando vale `true`, la salida será datos binarios sin tratar. Cuando vale `false`, la salida será dígitos hexadecimales en minúscula.

`options`  
Un array de opciones para los diversos algoritmos de hash. Actualmente, solo el parámetro `"seed"` es soportado para las variantes MurmurHash.

## Valores devueltos

Devuelve un string que contiene la huella digital calculada en dígitos hexadecimales minúsculos a menos que `binary` esté fijado a `true`. En este caso, la representación binaria sin tratar de la huella digital es devuelta, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                             |
|---------|-----------------------------------------|
| 8.1.0   | El parámetro `options` ha sido añadido. |

## Ejemplos

Ejemplo con `hash_file`

```
<?php
/* Crea un fichero para calcular su huella digital */
file_put_contents('example.txt', 'The quick brown fox jumped over the lazy dog.');

echo hash_file('sha256', 'example.txt');
?>

    
```php

El ejemplo anterior mostrará:

    68b1282b91de2c054c36629cb8dd447f12f096d3e3c587978dc2248444633483

## Véase también

`hash_init`, `hash_hmac_file`
