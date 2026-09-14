---
title: sodium_crypto_stream
description: Genera una secuencia de bytes determinista a partir de una semilla
source_url: https://www.php.net/manual/es/function.sodium-crypto-stream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-stream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76990
---

sodium_crypto_stream

Genera una secuencia de bytes determinista a partir de una semilla

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_stream(int $length, string $nonce, string $key): string
```php

Genera una secuencia de bytes determinista a partir de una semilla, utilizando el cifrado de flujo XSalsa20.

## Parámetros

`length`  
El número de bytes a devolver.

`nonce`  
Un número que debe ser utilizado una sola vez, por mensaje. 24 bytes de largo. Es un límite lo suficientemente grande como para ser generado aleatoriamente (i.e. `random_bytes`).

`key`  
La clave de cifrado (256 bits).

## Valores devueltos

Una cadena de bytes pseudoaleatorios.
