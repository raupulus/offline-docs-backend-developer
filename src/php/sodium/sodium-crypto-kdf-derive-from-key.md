---
title: sodium_crypto_kdf_derive_from_key
description: Deriva una subclave
source_url: https://www.php.net/manual/es/function.sodium-crypto-kdf-derive-from-key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-kdf-derive-from-key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76510
---

sodium_crypto_kdf_derive_from_key

Deriva una subclave

## Descripción

```php
#[\SensitiveParameter] sodium_crypto_kdf_derive_from_key(int $subkey_length, int $subkey_id, string $context, string $key): string
```php

Deriva una subclave a partir de una clave raíz y un contexto adicional.

Similar a `hash_hkdf`.

## Parámetros

`subkey_length`  
La longitud de la clave a devolver (en bytes).

`subkey_id`  
Devuelve la subclave N-ésima de una clave raíz dada. Útil para la búsqueda.

`context`  
El contexto específico de la aplicación.

`key`  
La clave raíz a partir de la cual se deriva la subclave.

## Valores devueltos

Una cadena de bytes pseudorandom (binario sin tratar).
