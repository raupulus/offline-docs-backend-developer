---
title: mcrypt_decrypt
description: Descifra un texto con los parámetros dados
source_url: https://www.php.net/manual/es/function.mcrypt-decrypt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mcrypt/functions/mcrypt-decrypt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mcrypt
translation_status: ready
translation_reviewed: true
translation_revision: e849a6c42
order: 45710
---

mcrypt_decrypt

Descifra un texto con los parámetros dados

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.1.0 y ha sido *ELIMINADA* a partir de PHP 7.2.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
mcrypt_decrypt(string $cipher, string $key, string $data, string $mode, [string $iv]): string
```php

Descifra los datos `data` y devuelve los datos descifrados.

## Parámetros

`cipher`  
Una de las constantes `MCRYPT_ciphername`, o el nombre del algoritmo como cadena.

`key`  
La clave utilizada durante el cifrado de los datos. Si el tamaño de la clave proporcionada no es soportado por el cipher, la función emitirá una advertencia y devolverá `false`

`data`  
Los datos que serán descifrados utilizando los parámetros `cipher` y `mode`. Si el tamaño de los datos no corresponde a n \* el tamaño del bloque, los datos serán completados con '`\0`'.

`mode`  
Una de las constantes `MCRYPT_MODE_modename`, o una de las siguientes cadenas: "ecb", "cbc", "cfb", "ofb", "nofb" o "stream".

`iv`  
Utilizado para la inicialización en los modos CBC, CFB, OFB, y en algunos algoritmos en modo STREAM. Si el tamaño del IV proporcionado no es soportado por el modo de encadenamiento o no se proporcionó un IV, pero el modo de encadenamiento requiere uno, la función emitirá una advertencia y devolverá `false`.

## Valores devueltos

Devuelve los datos descifrados en forma de `string` o `false` si ocurre un error.

## Véase también

mcrypt_encrypt
