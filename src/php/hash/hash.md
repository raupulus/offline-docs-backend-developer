---
title: hash
description: Genera un valor de hachado (huella digital)
source_url: https://www.php.net/manual/es/function.hash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: true
translation_revision: df2a77acb
order: 29370
---

hash

Genera un valor de hachado (huella digital)

## Descripción

```php
hash(string $algo, string $data, [bool $binary], [array $options]): string
```php

## Parámetros

`algo`  
Nombre del algoritmo de hachado seleccionado (por ejemplo: `"sha256"`). Para una lista de los algoritmos soportados ver `hash_algos`.

`data`  
Mensaje a hachar.

`binary`  
Cuando vale `true`, la salida será datos binarios sin tratar. Cuando vale `false`, la salida será dígitos hexadecimales en minúscula.

`options`  
Un array de opciones para los diversos algoritmos de hachado. Actualmente, solo el parámetro `"seed"` es soportado para las variantes MurmurHash.

## Valores devueltos

Devuelve un string que contiene la huella digital calculada en dígitos hexadecimales minúsculos a menos que `binary` esté fijado a `true`. En este caso, la representación binaria sin tratar de la huella digital es devuelta.

## Errores/Excepciones

Lanza una excepción ValueError si `algo` es desconocido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `options` ha sido añadido. |
| 8.0.0 | Ahora lanza una excepción ValueError si `algo` es desconocido; anteriormente, `false` era devuelto y se emitía un mensaje `E_WARNING`. |

## Ejemplos

Ejemplo con `hash`

```
<?php
echo hash('sha256', 'The quick brown fox jumped over the lazy dog.');
?>

    
```php

El ejemplo anterior mostrará:

    68b1282b91de2c054c36629cb8dd447f12f096d3e3c587978dc2248444633483

## Véase también

`hash_init`, `hash_file`, `hash_hmac`
