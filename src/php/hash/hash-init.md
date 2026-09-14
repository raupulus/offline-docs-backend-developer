---
title: hash_init
description: Inicializa un contexto de hachado incremental
source_url: https://www.php.net/manual/es/function.hash-init.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-init.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: true
translation_revision: fe4ff3410
order: 29320
---

hash_init

Inicializa un contexto de hachado incremental

## Descripción

```php
#[\SensitiveParameter] hash_init(string $algo, [int $flags], [string $key], [array $options]): HashContext
```php

## Parámetros

`algo`  
Nombre del algoritmo de hachado seleccionado (por ejemplo: `"sha256"`). Para una lista de los algoritmos soportados ver `hash_algos`.

> [!NOTE]
> Las funciones de hachado no criptográficas no están permitidas si se especifica el flag `HASH_HMAC`.

`flags`  
Configuraciones opcionales para la generación del hachado, actualmente solo soporta una opción: `HASH_HMAC`. Cuando esta opción es especificada, el parámetro `key` *debe* ser especificado.

`key`  
Cuando `HASH_HMAC` es especificada para `flags`, una clave secreta compartida que será utilizada con el método de hachado HMAC debe ser proporcionada en este parámetro.

`options`  
Un array de opciones para los algoritmos diversos de hachado. Actualmente, solo el parámetro `"seed"` es soportado para las variantes MurmurHash.

## Valores devueltos

Retorna el contexto de hachado HashContext para su utilización con `hash_update`, `hash_update_stream`, `hash_update_file` y `hash_final`.

## Errores/Excepciones

- Levanta una excepción `ValueError` si el `algo` es desconocido, si es una función de hachado no criptográfica, o si `key` está vacío.

- Pasar opciones de configuración de tipo incorrecto en `options` emitirá ahora un error `E_DEPRECATED`, ya que pueden ser mal interpretadas. Esto resultará en una excepción ValueError en el futuro.

## Historial de cambios

| Versión | Descripción |  |  |
|----|----|----|----|
| 8.4.0 | Pasar opciones de un tipo incorrecto está ahora desaconsejado. |  |  |
| 8.1.0 | El parámetro `options` ha sido añadido. |  |  |
| 7.2.0 | El uso de funciones de hachado no criptográficas (adler32, crc32, crc32b, fnv132, fnv1a32, fnv164, fnv1a64, joaat) con `HASH_HMAC` ha sido desactivado. |  |  |
| 7.2.0 | Retorna una `HashContext` en lugar de un recurso. | 8.0.0 | Levanta una excepción `ValueError` ahora si el parámetro `algo` es desconocido o no es una función de hachado criptográfica, o si el parámetro `key` está vacío. Anteriormente, `false` era retornado y un mensaje `E_WARNING` era emitido. |

## Ejemplos

Ejemplo de hachado incremental

```
<?php
$hash = hash('sha256', 'The quick brown fox jumped over the lazy dog.');

$ctx = hash_init('sha256');
hash_update($ctx, 'The quick brown fox ');
hash_update($ctx, 'jumped over the lazy dog.');
$incremental_hash = hash_final($ctx);

echo $incremental_hash, PHP_EOL;
var_dump($hash === $incremental_hash);
?>

    
```php

El ejemplo anterior mostrará:

    68b1282b91de2c054c36629cb8dd447f12f096d3e3c587978dc2248444633483
    bool(true)

## Véase también

`hash_algos`, `hash_update`, `hash_update_file`, `hash_update_stream`, `hash_final`
