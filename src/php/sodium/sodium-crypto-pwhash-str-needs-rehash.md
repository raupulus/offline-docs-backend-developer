---
title: sodium_crypto_pwhash_str_needs_rehash
description: Determina si una contraseña debe ser rehacheada
source_url: https://www.php.net/manual/es/function.sodium-crypto-pwhash-str-needs-rehash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-crypto-pwhash-str-needs-rehash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 76620
---

sodium_crypto_pwhash_str_needs_rehash

Determina si una contraseña debe ser rehacheada

## Descripción

```php
sodium_crypto_pwhash_str_needs_rehash(string $password, int $opslimit, int $memlimit): bool
```php

Determina si una contraseña debe ser rehacheada, basado en el hash actual `opslimit` y `memlimit`.

## Parámetros

`password`  
El hash de la contraseña

`opslimit`  
La opslimit; ver `sodium_crypto_pwhash_str`

`memlimit`  
La memlimit; ver `sodium_crypto_pwhash_str`

## Valores devueltos

Devuelve `true` si el memlimit/opslimit proporcionado no corresponde a lo que está almacenado en el hash. Devuelve `false` si corresponden.
