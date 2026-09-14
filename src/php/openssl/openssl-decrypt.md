---
title: openssl_decrypt
description: Descifrar los datos
source_url: https://www.php.net/manual/es/function.openssl-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/functions/openssl-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_reviewed: false
translation_revision: e5ab2937e
order: 59120
---

openssl_decrypt

Descifrar los datos

## Descripción

```php
#[\SensitiveParameter] openssl_decrypt(string $data, string $cipher_algo, string $passphrase, [int $options], [string $iv], [string $tag], [string $aad]): string
```php

Toma una cadena sin tratar o codificada en base64 y la descifra utilizando el método y la frase de contraseña proporcionados.

## Parámetros

`data`  
El mensaje cifrado a descifrar.

`cipher_algo`  
El algoritmo de cifrado. Para obtener la lista de algoritmos de cifrado disponibles, utilizar `openssl_get_cipher_methods`.

`passphrase`  
La frase de contraseña. Si la frase de contraseña es más corta de lo esperado, se completa silenciosamente con caracteres `NUL`; si la frase de contraseña es más larga de lo esperado, se trunca silenciosamente.

> [!CAUTION]
> No se utiliza ninguna función de derivación de clave para el parámetro `passphrase` como su nombre podría sugerir. La única operación utilizada es el relleno con caracteres `NUL` o la truncación si la longitud es diferente de la esperada.

`options`  
El parámetro `options` puede tomar como valor `OPENSSL_RAW_DATA` o `OPENSSL_ZERO_PADDING` o `OPENSSL_DONT_ZERO_PAD_KEY`.

`iv`  
Un vector de inicialización no-`null`. Si el VI es más corto de lo esperado, se completa con caracteres `NUL` y se emite un aviso; si la frase de contraseña es más larga de lo esperado, se trunca y se emite un aviso.

`tag`  
La etiqueta de autenticación en modo de cifrado AEAD. Si es incorrecta, la autenticación falla y la función devuelve `false`.

> [!CAUTION]
> La longitud de `tag` no es verificada por la función. Es responsabilidad del llamador asegurarse de que la longitud del tag coincida con la longitud del tag recibido cuando `openssl_encrypt` fue llamada. De lo contrario, el descifrado puede tener éxito si el inicio del tag proporcionado coincide con el inicio del verdadero tag.

`aad`  
Datos adicionales autenticados.

## Valores devueltos

La cadena descifrada en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si se pasa un algoritmo de cifrado desconocido a través de `cipher_algo`.

Emite un error de nivel `E_WARNING` si se pasa un valor vacío como parámetro `iv`.

## Historial de cambios

| Versión | Descripción                                |
|---------|--------------------------------------------|
| 8.1.0   | `tag` ahora es nullable.                   |
| 7.1.0   | Se añadieron los parámetros `tag` y `aad`. |

## Véase también

`openssl_encrypt`
