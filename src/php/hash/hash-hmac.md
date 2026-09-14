---
title: hash_hmac
description: Genera un valor de clave de hash utilizando el método HMAC
source_url: https://www.php.net/manual/es/function.hash-hmac.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-hmac.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: true
translation_revision: df2a77acb
order: 29310
---

hash_hmac

Genera un valor de clave de hash utilizando el método HMAC

## Descripción

```php
#[\SensitiveParameter] hash_hmac(string $algo, string $data, string $key, [bool $binary]): string
```php

## Parámetros

`algo`  
Nombre del algoritmo de hash seleccionado (por ejemplo: `"sha256"`). Para una lista de los algoritmos soportados ver `hash_hmac_algos`.

> [!NOTE]
> Las funciones de hash no criptográficas no están permitidas.

`data`  
El mensaje que será hasheado.

`key`  
Clave secreta compartida utilizada para generar la variación HMAC de la huella digital.

`binary`  
Cuando es `true`, la salida será datos binarios sin tratar. Cuando es `false`, la salida será dígitos hexadecimales en minúscula.

## Valores devueltos

Retorna un string que contiene la huella digital calculada en dígitos hexadecimales en minúscula a menos que `binary` esté fijado a `true`. En este caso, la representación binaria sin tratar de la huella digital es retornada.

## Errores/Excepciones

Levanta una excepción `ValueError` si el argumento `algo` es desconocido o no es una función de hash criptográfica.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `hash_hmac` ahora levanta una excepción `ValueError` si el `algo` es desconocido o no es una función de hash criptográfica ; anteriormente, `false` era retornado y se emitía un mensaje `E_WARNING`. |
| 7.2.0 | El uso de funciones de hash no criptográficas (adler32, crc32, crc32b, fnv132, fnv1a32, fnv164, fnv1a64, joaat) ha sido desactivado. |

## Ejemplos

Ejemplo con `hash_hmac`

```
<?php
echo hash_hmac('sha256', 'The quick brown fox jumped over the lazy dog.', 'secret');
?>

    
```php

El ejemplo anterior mostrará:

    9c5c42422b03f0ee32949920649445e417b2c634050833c5165704b825c2a53b

## Véase también

`hash_hmac_algos`, `hash_hmac_file`, `hash_equals`
