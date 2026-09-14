---
title: hash_hkdf
description: Genera una derivación de clave HKDF a partir de una clave de entrada
  proporcionada
source_url: https://www.php.net/manual/es/function.hash-hkdf.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/hash/functions/hash-hkdf.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: hash
translation_status: ready
translation_reviewed: false
translation_revision: a19139232
order: 29280
---

hash_hkdf

Genera una derivación de clave HKDF a partir de una clave de entrada proporcionada

## Descripción

```php
#[\SensitiveParameter] hash_hkdf(string $algo, string $key, [int $length], [string $info], [string $salt]): string
```php

## Parámetros

`algo`  
Nombre del algoritmo hash seleccionado (por ejemplo, `"sha256"`). Para ver una lista de algoritmos soportados, consulte `hash_hmac_algos`.

> [!NOTE]
> No se permiten funciones hash no criptográficas.

`key`  
Material de clave de entrada (binario sin tratar). No puede estar vacío.

`length`  
Longitud deseada de la salida en bytes. No puede ser mayor que 255 veces el tamaño de la función hash elegida.

Si `length` es `0`, la longitud de salida será por omisión el tamaño de la función hash elegida.

`info`  
String de información específica de la aplicación/contexto.

`salt`  
Salt a utilizar durante la derivación.

Aunque es opcional, añadir un salt aleatorio mejora significativamente la robustez de HKDF.

## Valores devueltos

Devuelve un string que contiene una representación binaria sin tratar de la clave derivada (también conocida como material de clave de salida - OKM).

## Errores/Excepciones

Lanza una excepción `ValueError` si `key` está vacío, `algo` es desconocido/no criptográfico, `length` es menor que `0` o demasiado grande (mayor que 255 veces el tamaño de la función hash).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Ahora lanza una excepción `ValueError` en caso de error. Anteriormente, se devolvía `false` y se emitía un mensaje `E_WARNING`. |

## Ejemplos

El ejemplo siguiente produce un par de claves separadas, adecuadas para crear una construcción de tipo encrypt-then-HMAC, utilizando AES-256 y SHA-256 para cifrado y autenticación respectivamente.

Ejemplo de `hash_hkdf`

```
<?php
// Generar una clave aleatoria y un salt para fortalecerla durante la derivación.
$inputKey = random_bytes(32);
$salt = random_bytes(16);

// Derivar un par de claves separadas, utilizando la misma entrada creada arriba.
$encryptionKey = hash_hkdf('sha256', $inputKey, 32, 'aes-256-encryption', $salt);
$authenticationKey = hash_hkdf('sha256', $inputKey, 32, 'sha-256-authentication', $salt);

var_dump($encryptionKey !== $authenticationKey); // bool(true)
?>

    
```php

## Véase también

`hash_pbkdf2`, [RFC 5869](https://datatracker.ietf.org/doc/html/rfc5869), [implementación en espacio de usuario](https://github.com/narfbg/hash_hkdf_compat)
