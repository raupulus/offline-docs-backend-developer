---
title: sodium_crypto_generichash
description: Devuelve un hash del mensaje
source_url: https://www.php.net/manual/es/function.sodium-crypto-generichash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-generichash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76500
---

sodium_crypto_generichash

Devuelve un hash del mensaje

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_generichash(string $message, [string $key], [int $length]): string
```php

Hachea un mensaje con BLAKE2b.

## Parámetros

`message`  
El mensaje a hachear.

`key`  
(Opcional) Clave criptográfica. Sirve para la misma función que una clave HMAC, pero se utiliza como una sección reservada del estado interno de BLAKE2.

`length`  
El tamaño de la salida.

## Valores devueltos

El hash criptográfico como una cadena binaria bruta. Si se desea una salida hexadecimal, el resultado puede ser pasado a `sodium_bin2hex`.
